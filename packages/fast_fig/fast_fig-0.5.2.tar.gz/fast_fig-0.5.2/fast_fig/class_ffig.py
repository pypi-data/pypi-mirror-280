"""fast_fig simplifies figure handling with mpl.

Key functions:
- predefinied templates
- figure instantiation in a class object
- simplified handling (e.g. plot with vectors)

import fast_fig
# very simple example
fig = fast_fig.FFig()
fig.plot()
fig.show()

# more complex example
fig = fast_fig.FFig("l", nrows=2, sharex=True)  # create figure with template l=large
fig.plot([1, 2, 3, 1, 2, 3, 4, 1, 1])  # plot first data set
fig.title("First data set")  # set title for subplot
fig.subplot()  # set focus to next subplot/axis
fig.plot([0, 1, 2, 3, 4], [0, 1, 1, 2, 3], label="random")  # plot second data set
fig.legend()  # generate legend
fig.grid()  # show translucent grid to highlight major ticks
fig.xlabel("Data")  # create xlabel for second axis
fig.save("fig1.png", "pdf")  # save figure to png and pdf

# The following handlers can be used to access all matplotlib functionality:
# - fig.handler_fig
# - fig.handler_plot
# - fig.handler_axis
# - fig.current_axis

"""

# %%
__author__ = "Fabian Stutzki"
__email__ = "fast@fast-apps.de"
__version__ = "0.2.6"


import logging
from pathlib import Path
from typing import List, Optional, Tuple, Union

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler
from packaging import version

from .presets import define_presets


# %%
class FFig:
    """FFig simplifies handling of matplotlib figures.

    Use as
    from fast_fig import FFig
    fig = FFig('m')
    fig.plot([0,1,2,3,4],[0,1,1,2,3])
    fig.save('test.png')

    @author: fstutzki

    """

    def __init__(
        self: "FFig",
        *args: Union[int, str],
        template: str = "m",
        nrows: int = 1,
        ncols: int = 1,
        **kwargs: Union[int, str],
    ) -> None:
        """Set default values and create figure.

        fig = FFig("OL", nrows=2, ncols=2)
        """
        # Enable logger
        self.logger = logging.getLogger(self.__class__.__name__)

        # Assign unnamed arguments
        if len(args) == 1:
            if isinstance(args[0], int):
                nrows = args[0]
            else:
                template = args[0]
        elif len(args) == 2:
            if isinstance(args[0], int):
                nrows = args[0]
                ncols = args[1]
            else:
                template = args[0]
                nrows = args[1]
        elif len(args) == 3:
            template = args[0]
            nrows = args[1]
            ncols = args[2]
        elif len(args) > 3:
            error_message = "Too many arguments for FFig(), max 3 unnamed arguments."
            raise ValueError(error_message)

        kwargs.setdefault("isubplot", 0)
        kwargs.setdefault("sharex", False)
        kwargs.setdefault("sharey", False)
        kwargs.setdefault("show", True)
        kwargs.setdefault("vspace", None)
        kwargs.setdefault("hspace", None)
        kwargs.setdefault("presets", None)

        # Initialize dictionary with presets
        self.presets = define_presets(kwargs["presets"])

        # Check if template exists (ignoring case), otherwise set template m (default)
        template = template.lower()
        if template not in self.presets:
            template = "m"

        # Fill undefined kwargs with presets
        for key in ["width", "height", "fontfamily", "fontsize", "linewidth"]:
            kwargs.setdefault(key, self.presets[template][key])

        # Apply parameters to matplotlib
        mpl.rc("font", size=kwargs["fontsize"])
        mpl.rc("font", family=kwargs["fontfamily"])
        mpl.rc("lines", linewidth=kwargs["linewidth"])

        # Convert colors to ndarray and scale to 1 instead of 255
        self.colors = {}
        for iname, icolor in self.presets["colors"].items():
            if np.max(icolor) > 1:
                self.colors[iname] = np.array(icolor) / 255

        # Define cycle with colors, color_seq and linestyle_seq
        self.set_cycle(self.colors, self.presets["color_seq"], self.presets["linestyle_seq"])

        # Store global variables
        self.figshow = kwargs["show"]  # show figure after saving
        self.subplot_index = 0
        self.handle_bar = None
        self.handle_plot = None
        self.handle_surface = None
        self.linewidth = kwargs["linewidth"]

        # Create figure
        self.handle_fig = plt.figure()
        self.handle_fig.set_size_inches(kwargs["width"] / 2.54, kwargs["height"] / 2.54)
        self.subplot(
            nrows=nrows,
            ncols=ncols,
            index=kwargs["isubplot"],
            sharex=kwargs["sharex"],
            sharey=kwargs["sharey"],
            vspace=kwargs["vspace"],
            hspace=kwargs["hspace"],
        )

    def subplot(
        self: "FFig",
        *args: Union[int, Tuple[int, int, int]],
        nrows: Optional[int] = None,
        ncols: Optional[int] = None,
        index: Optional[int] = None,
        sharex: Union[bool, str] = False,
        sharey: Union[bool, str] = False,
        vspace: Optional[float] = None,
        hspace: Optional[float] = None,
    ) -> None:
        """Set current axis/subplot.

        fig.subplot(0) # for first subplot
        fig.subplot() # for next subplot
        """
        num_args = len(args)
        if num_args == 0:
            # Increase current axe handle by 1
            self.subplot_index += 1
        elif num_args == 1:
            # Define current axe handle
            self.subplot_index = args[0]
        elif num_args in (2, 3):
            # Generate new subplot
            nrows = args[0]
            ncols = args[1]
        else:
            error_message = "subplot() takes 0 to 3 unnamed arguments"
            raise ValueError(error_message)

        if nrows is not None or ncols is not None:
            # Generate new subplot
            if nrows is None:
                nrows = 1
            if ncols is None:
                ncols = 1
            self.subplot_nrows = nrows
            self.subplot_ncols = ncols
            self.subplot_sharex = sharex
            self.subplot_sharey = sharey
            self.subplot_vspace = vspace
            self.subplot_hspace = hspace
            if num_args == 3:
                self.subplot_index = args[2]
            else:
                self.subplot_index = 0

            self.handle_fig.clf()
            self.handle_fig, self.handle_axis = plt.subplots(
                nrows=self.subplot_nrows,
                ncols=self.subplot_ncols,
                num=self.handle_fig.number,
                sharex=self.subplot_sharex,
                sharey=self.subplot_sharey,
            )

        # Overwrite subplot_index with named argument
        if index is not None:
            self.subplot_index = index

        # Set current axe handle
        self.subplot_index = self.subplot_index % (self.subplot_nrows * self.subplot_ncols)
        if self.subplot_nrows == 1 and self.subplot_ncols == 1:
            self.current_axis = self.handle_axis
        elif self.subplot_nrows > 1 and self.subplot_ncols > 1:
            isuby = self.subplot_index // self.subplot_ncols
            isubx = self.subplot_index % self.subplot_ncols
            self.current_axis = self.handle_axis[isuby][isubx]
        else:
            self.current_axis = self.handle_axis[self.subplot_index]

    def suptitle(self: "FFig", *args, **kwargs) -> None:
        """Set super title for the whole figure."""
        self.handle_fig.suptitle(*args, **kwargs)

    def bar_plot(self: "FFig", *args, **kwargs) -> None:
        """Generate bar plot."""
        self.handle_bar = self.current_axis.bar(*args, **kwargs)
        return self.handle_bar

    def plot(
        self: "FFig",
        mat=np.array([[1, 2, 3, 4, 5, 6, 7], np.random.randn(7), 2 * np.random.randn(7)]),
        *args,
        **kwargs,
    ) -> None:
        """Generate a line plot."""
        if np.ndim(mat) > 1:
            if np.shape(mat)[0] > np.shape(mat)[1]:
                mat = mat.T
            for imat in mat[1:]:
                self.handle_plot = self.current_axis.plot(mat[0, :], imat, *args, **kwargs)
        else:
            self.handle_plot = self.current_axis.plot(mat, *args, **kwargs)
        return self.handle_plot

    def semilogx(self: "FFig", *args, **kwargs) -> None:
        """Semi-log plot on x axis."""
        self.plot(*args, **kwargs)
        self.xscale("log")

    def semilogy(self: "FFig", *args, **kwargs) -> None:
        """Semi-log plot on y axis."""
        self.plot(*args, **kwargs)
        self.yscale("log")

    def fill_between(
        self: "FFig",
        *args,
        color: Optional[list] = None,
        alpha: float = 0.1,
        linewidth: float = 0,
        **kwargs,
    ) -> None:
        """Fill area below or between lines."""
        if color is None:
            color = self.last_color()
        self.current_axis.fill_between(
            *args,
            color=color,
            alpha=alpha,
            linewidth=linewidth,
            **kwargs,
        )

    def last_color(self: "FFig") -> None:
        """Return last color code used by plot."""
        return self.handle_plot[0].get_color()

    def pcolor(self: "FFig", *args, **kwargs) -> None:
        """2D area plot."""
        if "cmap" not in kwargs:
            kwargs["cmap"] = "nipy_spectral"
        self.handle_surface = self.current_axis.pcolormesh(*args, **kwargs)
        return self.handle_surface

    def pcolor_log(
        self: "FFig",
        *args,
        vmin: Optional[float] = False,
        vmax: Optional[float] = False,
        **kwargs,
    ) -> None:
        """2D area plot with logarithmic scale."""
        if "cmap" not in kwargs:
            kwargs["cmap"] = "nipy_spectral"
        kwargs_log = {}
        if vmin is not False:
            kwargs_log["vmin"] = vmin
        if vmax is not False:
            kwargs_log["vmax"] = vmax
        kwargs["norm"] = mpl.colors.LogNorm(**kwargs_log)
        self.handle_surface = self.current_axis.pcolormesh(*args, **kwargs)
        return self.handle_surface

    def pcolor_square(self: "FFig", *args, **kwargs) -> None:
        """2D area plot with axis equal and off."""
        if "cmap" not in kwargs:
            kwargs["cmap"] = "nipy_spectral"
        self.handle_surface = self.current_axis.pcolormesh(*args, **kwargs)
        self.current_axis.axis("off")
        self.current_axis.set_aspect("equal")
        self.current_axis.set_xticks([])
        self.current_axis.set_yticks([])
        return self.handle_surface

    def contour(self: "FFig", *args, **kwargs) -> None:
        """2D contour plot."""
        self.handle_surface = self.current_axis.contour(*args, **kwargs)
        return self.handle_surface

    def scatter(self: "FFig", *args, **kwargs) -> None:
        """Plot scattered data."""
        self.handle_surface = self.current_axis.scatter(*args, **kwargs)
        return self.handle_surface

    def colorbar(self: "FFig", *args, **kwargs) -> None:
        """Add colorbar to figure."""
        self.handle_fig.colorbar(*args, self.handle_surface, ax=self.current_axis, **kwargs)

    def axis(self: "FFig", *args, **kwargs) -> None:
        """Access axis properties such as 'off'."""
        self.current_axis.axis(*args, **kwargs)

    def axis_aspect(self: "FFig", *args, **kwargs) -> None:
        """Access axis aspect ration."""
        self.current_axis.set_aspect(*args, **kwargs)

    def grid(self: "FFig", *args, color: str = "grey", alpha: float = 0.2, **kwargs) -> None:
        """Access axis aspect ration."""
        self.current_axis.grid(*args, color=color, alpha=alpha, **kwargs)

    def annotate(self: "FFig", *args, **kwargs) -> None:
        """Annotation to figure."""
        self.current_axis.annotate(*args, **kwargs)

    def text(self: "FFig", *args, **kwargs) -> None:
        """Text to figure."""
        self.current_axis.text(*args, **kwargs)

    def title(self: "FFig", *args, **kwargs) -> None:
        """Set title for current axis."""
        self.current_axis.set_title(*args, **kwargs)

    def xscale(self: "FFig", *args, **kwargs) -> None:
        """Set x-axis scaling."""
        self.current_axis.set_xscale(*args, **kwargs)

    def yscale(self: "FFig", *args, **kwargs) -> None:
        """Set y-axis scaling."""
        self.current_axis.set_yscale(*args, **kwargs)

    def xlabel(self: "FFig", *args, **kwargs) -> None:
        """Set xlabel for current axis."""
        self.current_axis.set_xlabel(*args, **kwargs)

    def ylabel(self: "FFig", *args, **kwargs) -> None:
        """Set ylabel for current axis."""
        self.current_axis.set_ylabel(*args, **kwargs)

    def xlim(self: "FFig", xmin: float = np.inf, xmax: float = -np.inf) -> None:
        """Set limits for current x-axis.

        xlim(0,1) # limit set to 0 and 1
        xlim() # set limit to min and max
        """
        try:
            if np.size(xmin) == 2:
                xmax = xmin[1]
                xmin = xmin[0]
            elif xmin == np.inf and xmax == -np.inf:
                for iline in self.current_axis.lines:
                    xdata = iline.get_xdata()
                    xmin = np.minimum(xmin, np.nanmin(xdata))
                    xmax = np.maximum(xmax, np.nanmax(xdata))
            if version.parse(mpl.__version__) >= version.parse("3"):
                if np.isfinite(xmin):
                    self.current_axis.set_xlim(left=xmin)
                if np.isfinite(xmax):
                    self.current_axis.set_xlim(right=xmax)
            else:
                if np.isfinite(xmin):
                    self.current_axis.set_xlim(xmin=xmin)
                if np.isfinite(xmax):
                    self.current_axis.set_xlim(xmax=xmax)
        except (ValueError, TypeError):
            self.logger.exception()

    def ylim(self: "FFig", ymin: float = np.inf, ymax: float = -np.inf) -> None:
        """Set limits for current y-axis.

        ylim(0,1) # set limit to 0 and 1
        ylim() # set limit to min and max
        """
        try:
            if np.size(ymin) == 2:
                ymax = ymin[1]
                ymin = ymin[0]
            elif ymin == np.inf and ymax == -np.inf:
                for iline in self.current_axis.lines:
                    ydata = iline.get_ydata()
                    ymin = np.minimum(ymin, np.nanmin(ydata))
                    ymax = np.maximum(ymax, np.nanmax(ydata))
            if version.parse(mpl.__version__) >= version.parse("3"):
                if np.isfinite(ymin):
                    self.current_axis.set_ylim(bottom=ymin)
                if np.isfinite(ymax):
                    self.current_axis.set_ylim(top=ymax)
            else:
                if np.isfinite(ymin):
                    self.current_axis.set_ylim(ymin=ymin)
                if np.isfinite(ymax):
                    self.current_axis.set_ylim(ymax=ymax)
        except (ValueError, TypeError):
            self.logger.exception()

    def legend(self: "FFig", *args, labels: Optional[str] = None, **kwargs) -> None:
        """Insert legend based on labels given in plot(x,y,label='Test1') etc."""
        if labels is not None:
            for ilabel, iline in enumerate(self.current_axis.lines):
                iline.set_label(labels[ilabel])
        _, labels = self.current_axis.get_legend_handles_labels()
        if np.size(self.current_axis.lines) != 0 and len(labels) != 0:
            self.current_axis.legend(*args, **kwargs)

    def legend_entries(self: "FFig") -> None:
        """Return handle and labels of legend."""
        handles, labels = self.current_axis.get_legend_handles_labels()
        return handles, labels

    def legend_count(self: "FFig") -> None:
        """Return number of legend entries."""
        handles, _ = self.current_axis.get_legend_handles_labels()
        return np.size(handles)

    def set_cycle(
        self: "FFig", colors: list, color_seq: List[str], linestyle_seq: List[str]
    ) -> None:  # ,linewidth=False):
        """Set cycle for colors and linestyles (will be used in this order)."""
        # generate cycle from color_seq and linestyle_seq
        color_list = [colors[icolor] for icolor in color_seq if icolor in colors]
        cyc_color = np.tile(color_list, (np.size(linestyle_seq), 1))
        cyc_linestyle = np.repeat(linestyle_seq, np.shape(color_list)[0])
        try:
            mpl.rc(
                "axes",
                prop_cycle=(cycler("color", cyc_color) + cycler("linestyle", cyc_linestyle)),
            )
            if hasattr(self, "axeC"):
                self.current_axis.set_prop_cycle(
                    cycler("color", cyc_color) + cycler("linestyle", cyc_linestyle)
                )
        except (ValueError, TypeError):
            self.logger.exception("set_cycle(): Cannot set cycle for color and linestyle")

    def set_parameters(self: "FFig") -> None:
        """Set useful figure parameters, called automatically by save and show function."""
        try:
            self.handle_fig.tight_layout()
        except (ValueError, TypeError):
            self.logger.exception("set_parameters(): Tight layout cannot be set!")

        if self.subplot_hspace is not None and self.subplot_nrows > 1:
            self.handle_fig.subplots_adjust(hspace=self.subplot_hspace)
        if self.subplot_vspace is not None and self.subplot_ncols > 1:
            self.handle_fig.subplots_adjust(vspace=self.subplot_vspace)

    def watermark(
        self: "FFig",
        img: str,
        *args,
        xpos: float = 100,
        ypos: float = 100,
        alpha: float = 0.15,
        zorder: float = 1,
        **kwargs,
    ) -> None:
        """Include watermark image to plot."""
        if Path(img).is_file():
            self.handle_fig.figimage(img, xpos, ypos, alpha=alpha, zorder=zorder, *args, **kwargs)
        else:
            FileNotFoundError("watermark(): File not found")

    def show(self: "FFig") -> None:
        """Show figure in interactive console (similar to save)."""
        self.set_parameters()
        plt.show()

    def save(self: "FFig", filename: str, *args, **kwargs) -> None:
        """Save figure as image (png, pdf...).

        save('test.png',600,'pdf') # save test.png and test.pdf with 600dpi
        """
        dpi = 300
        fileparts = filename.split(".")
        fileformat = set()
        fileformat.add(fileparts[-1])
        filename = filename.replace("." + fileparts[-1], "")
        for attribute in args:
            if isinstance(attribute, int):
                dpi = attribute
            else:
                fileformat.add(attribute)
        if "dpi" not in kwargs:
            kwargs["dpi"] = dpi

        self.set_parameters()
        for iformat in fileformat:
            try:
                Path(filename).parent.mkdir(parents=True, exist_ok=True)
                self.handle_fig.savefig(f"{filename}.{iformat}", **kwargs)
            except (FileNotFoundError, PermissionError, OSError):
                except_message = f"save(): Figure cannot be saved to {filename}.{iformat}"
                self.logger.exception(except_message)
        if self.figshow:
            plt.show()  # block=False)
        else:
            plt.draw()

    def clear(self: "FFig", *args, **kwargs) -> None:
        """Clear figure content in order to reuse figure."""
        self.handle_fig.clf(*args, **kwargs)

    def close(self: "FFig") -> None:
        """Close figure."""
        try:
            plt.close(self.handle_fig)
        except (ValueError, TypeError, AttributeError):
            self.logger.exception("close(): Figure cannot be closed")


# %%
if __name__ == "__main__":
    fig = FFig()
    fig.plot()
    fig.show()
