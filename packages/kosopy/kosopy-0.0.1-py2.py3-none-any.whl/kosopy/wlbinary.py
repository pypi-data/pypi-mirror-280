import os
import numpy as np
import h5py as h5
import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
import tqdm as tq
from matplotlib import gridspec

__all__ = ['WLMask', 'WLBinary']


class WLMask:
    """
    A class to handle white-light (WL) mask data from HDF5 files.

    Attributes:
        filename (str): The filename of the HDF5 file containing the WL mask data.
        key (str): The key to access the specific dataset within the HDF5 file.

    Methods:
        __repr__(): Provides a string representation of the WLMask object.
        crmask(): Property to access the Carrington Frame mask data.
        fdmask(): Property to access the full-disk mask data.
        info(): Property to access metadata information of the full-disk mask.
        plot(data="crmask", **kwargs): Plots the mask data (cosmic ray mask, full-disk mask, or both).
    """

    x = np.arange(-511.5, 512, 1.0)
    x, y = np.meshgrid(x, x)
    disk = np.hypot(x, y)

    def __init__(self, filename, key):
        """
        Initializes the WLMask object with the specified filename and key.

        Parameters
        ----------
        filename : str
            The filename of the HDF5 file containing the WL mask data.
        key : str
            The key to access the specific dataset within the HDF5 file.
        """
        self.filename = filename
        self.key = key

    def __repr__(self):
        """
        Provides a string representation of the WLMask object.

        Returns
        -------
        str
            String representation of the WLMask object.
        """
        return f'WLMask(filename={os.path.basename(self.filename)}, key={self.key})'

    @property
    def crmask(self):
        """
        Property to access the Carrigton Rotation mask data.

        Returns
        -------
        np.ndarray
            Cosmic ray mask data array.
        """
        with h5.File(self.filename, 'r') as f:
            crmask = f[f"{self.key}/crmask"][()]
        return crmask

    @property
    def fdmask(self):
        """
        Property to access the full-disk mask data.

        Returns
        -------
        np.ndarray
            Full-disk mask data array.
        """
        with h5.File(self.filename, 'r') as f:
            fdmask = f[f"{self.key}/diskmask"][()]
        return fdmask

    @property
    def info(self):
        """
        Property to access metadata information of the full-disk mask.

        Returns
        -------
        dict
            Dictionary containing metadata attributes of the full-disk mask.
        """
        inf = {}
        with h5.File(self.filename, 'r') as f:
            for _key in f[f"{self.key}/diskmask"].attrs.keys():
                inf[_key] = f[f"{self.key}/diskmask"].attrs[_key]
        return inf

    def plot(self, data="crmask", outfile=None,  **kwargs):
        """
        Plots the mask data (cosmic ray mask, full-disk mask, or both).

        Parameters
        ----------
        data : str, optional
            The type of mask data to plot. Options are "crmask", "fdmask", or "both".
            Defaults to "crmask".
        kwargs : dict
            Additional keyword arguments to pass to the imshow function.
        """
        fig = None
        if data == "crmask":
            fig, ax = plt.subplots(figsize=(10, 5))
            kwg = {"cmap": "YlOrBr", "extent": (0, 360, -90, 90), "origin": "lower"}
            kwg.update(kwargs)
            ax.imshow(self.crmask, **kwg)
            ax.set(xlabel="Longitude", ylabel="Latitude", title=self.info["DATE-OBS"])
        elif data == "fdmask":
            fig, ax = plt.subplots(figsize=(5, 5))
            kwg = {"cmap": "YlOrBr", "extent": (-512, 512, -512, 512), "origin": "lower"}
            kwg.update(kwargs)
            disk = np.where(self.disk < self.info["radius"], 1, 0)
            ax.imshow(self.fdmask + disk, **kwg)
            ax.contour(disk, extent=kwg["extent"], colors="k", linewidths=0.2, linestyles="--")
            ax.set(xlabel="Pixels", ylabel="Pixels", title=self.info["DATE-OBS"])
        elif data == "both":
            fig = plt.figure(figsize=(10, 5))
            ax1 = fig.add_axes([0.05, 0.05, 0.25, 0.5])
            kwg = {"cmap": "YlOrBr", "extent": (-512, 512, -512, 512), "origin": "lower"}
            kwg.update(kwargs)
            disk = np.where(self.disk < self.info["RADIUS"], 1, 0)
            ax1.imshow(self.fdmask + disk, **kwg)
            ax1.contour(disk, extent=kwg["extent"], colors="k", linewidths=0.2, linestyles="--")
            ax1.set(xlabel="Pixels", ylabel="Pixels", title=self.info["DATE-OBS"])

            ax2 = fig.add_axes([0.4, 0.05, 0.5, 0.5])
            ax2.set(xlabel="Longitude", ylabel="Latitude", title=self.info["DATE-OBS"])
            kwg = {"cmap": "YlOrBr", "extent": (0, 360, -90, 90), "origin": "lower"}
            kwg.update(kwargs)
            ax2.imshow(self.crmask, **kwg)
        if outfile is not None:
            plt.savefig(outfile)
            plt.close()
        else:
            plt.show()


class WLBinary(object):
    """
    A class to handle and load white-light (WL) mask data from HDF5 files in a specified directory or single file.

    Attributes:
        fileinfo (dict): Dictionary containing file type mappings.
        filename (list): List of filenames to process.
        path (str): Path to the directory or file.
        filetype (str): Type of file to look for (default is 'hdf5').
        verbose (bool): Flag to print verbose output.
        count (int): Counter for the number of files found.
        _input_path (bool): Flag indicating if path input is provided.
        _input_file (bool): Flag indicating if filename input is provided.
        datalist (DataFrame): DataFrame containing the loaded data information.

    Methods:
        _file_search(): Searches for files in the provided directory path.
        load(reload=False): Loads data from the found files and generates a CSV file with metadata.
        get_data(date=None): Retrieves data for a specified date.
    """

    fileinfo = {
        "hdf5": "h5"
    }

    def __init__(self, filename=None, path=None, filetype="hdf5", verbose=False):
        """
        Initializes the WLBinary object with the specified parameters.

        Parameters
        ----------
        filename : str, optional
            Filename of a single HDF5 file to process.
        path : str, optional
            Directory path containing multiple HDF5 files to process.
        filetype : str, optional
            Type of file to look for (default is 'hdf5').
        verbose : bool, optional
            Flag to print verbose output (default is False).
        """
        self.filename = []
        self.path = path
        self.filetype = filetype
        self.verbose = verbose
        self.count = 0
        self._input_path = True if path is not None else False
        self._input_file = True if filename is not None else False

        # Check the input
        if filename is None and path is None:
            raise ValueError("Error: Neither filename nor file path is provided.")
        if (filename is not None) and (path is not None):
            raise ValueError("Error: Both Filename and Path should not be provided at the same time.")
        if (filename is not None) and (path is None):
            if os.path.isfile(filename):
                self.filename = np.array([filename])
                self.path = os.path.basename(filename)
            else:
                raise FileNotFoundError(f"Either {filename} does not exist or it is a directory.")

        if (filename is None) and (path is not None):
            if os.path.isdir(path):
                self._file_search()
            else:
                raise FileNotFoundError(f"{filename} does not exist.")
        self.load(reload=True)
        self.datalist = pd.read_csv("KoSO_WL_mask_list.csv",
                                    names=["Date", "Year", "Month", "Filename", "Key"])
        print(f"'KoSO_WL_mask_list.csv' is created in your directory based on the input.")

    def _file_search(self):
        """
        Searches for files in the provided directory path.
        """
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith(self.fileinfo[self.filetype]):
                    self.count += 1
                    self.filename.append(os.path.join(root, file))
        self.filename = np.sort(np.array(self.filename))

    def load(self, reload=False):
        """
        Loads data from the found files and generates a CSV file with metadata.

        Parameters
        ----------
        reload : bool, optional
            Flag to reload data and regenerate the CSV file (default is False).
        """
        print("Hold on! Going through your data to find out all the observation.")
        if reload is True:
            fl = open("KoSO_WL_mask_list.csv", "w")
            for h5file in self.filename:
                yr = os.path.basename(h5file)[13:17]
                with h5.File(h5file, "r") as f:
                    for mo in f.keys():
                        moh5 = f[mo]
                        for da in moh5.keys():
                            times = f"{yr}-{mo}-{da[0:2]}"
                            _relpath = os.path.relpath(h5file, start = self.path)
                            fl.write(f"{times},{yr},{mo},{_relpath},{mo}/{da}\n")
            fl.close()

    def get_data(self, date=None):
        """
        Retrieves data for a specified date.

        Parameters
        ----------
        date : str, optional
            The date for which to retrieve data in 'YYYY', 'YYYY-MM', or 'YYYY-MM-DD' format.

        Returns
        -------
        list of WLMask
            List of WLMask objects for the specified date.
        """
        fmt = 0
        if date is None:
            ind = np.arange(len(self.datalist.Date))
        elif len(date) == 4:
            _date = dt.datetime.strptime(date, "%Y")
            ind = np.where(self.datalist.Year.astype(str) == date)
        elif len(date) == 7:
            _date = dt.datetime.strptime(date, "%Y-%m")
            ind = np.where((self.datalist.Year.astype(str) == date[0:4])\
                           & (self.datalist.Month == int(date[5:7])))
        elif len(date) == 10:
            _date = dt.datetime.strptime(date, "%Y-%m-%d")
            ind = np.where(self.datalist.Date == date)
        else:
            raise ValueError("Invalid date")

        if ind[0].size == 0:
            print("Oops! It was a Cloudy day at KoSO! No data available.")
            print("\"The sun always shines above the clouds.\" ― Paul F. Davis.")
            return None
        else:
            _datalist = self.datalist.iloc[ind]
            out = []
            for _filename, key in zip(_datalist.Filename, _datalist.Key):
                _filename = os.path.join(self.path, _filename)
                out.append(WLMask(_filename, key))
        if self.verbose:
            print(f"Total Number of Observation: {ind[0].size}")
        return out

    def makepng(self, date=None, outpath=None, data="both"):
        if outpath is None:
            os.makedirs("./png", exist_ok=True)
            outpath = os.path.abspath("./png")
        masks = self.get_data(date)
        for _mask in tq.tqdm(masks):
            _times = _mask.info["DATE-OBS"]
            _filepath = _times[0:7].replace("-", "/")
            os.makedirs(os.path.join(outpath, _filepath), exist_ok=True)
            _filename = f"KoSO_WL_mask_{_times.replace("-", "").replace(":", "")}.png"
            outfile = os.path.join(outpath, _filepath, _filename)
            _mask.plot(data=data, outfile=outfile)


