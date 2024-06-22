from pytom3d.core import Topography
from pytom3d.util import printer
# from util import summation, distance, distance2
from matplotlib import pyplot as plt
from typing import List, Tuple, Dict
import matplotlib
from matplotlib import ticker
import matplotlib.cm as cm
from matplotlib.gridspec import GridSpec
from matplotlib.colors import BoundaryNorm #Normalize
import numpy as np


class Viewer:
    
    def __init__(self, name: str = "unnamed") -> None:
        """
        Initialize a new instance of YourClass.
    
        Parameters
        ----------
        name : str, optional
            The name to be assigned to the instance. Default is "unnamed".
    
        Attributes
        ----------
        name : str
            The name of the instance.
        x_lim : List[float] or None
            The limits for the x-axis.
        y_lim : List[float] or None
            The limits for the y-axis.
        z_lim : List[float] or None
            The limits for the z-axis.
            
        Returns
        -------
            None

        """
        self.name = name
        self.x_lim = None
        self.y_lim = None
        self.z_lim = None
        self.config()
        self.config_3d()

    def config(self, save: bool = False, folder: str = "./", fmt: str = "png", dpi: int = 300) -> None:
        """
        Configure settings for saving plots.

        Borrowed from https://github.com/aletgn/b-fade/

        Parameters
        ----------
        save : bool, optional
            Flag indicating whether to save plots. The default is False.
        folder : str, optional
            Folder path where plots will be saved. The default is "./".
        fmt : str, optional
            Format for saving plots. The default is "png".
        dpi : int, optional
            Dots per inch for saving plots. The default is 300.

        Returns
        -------
        None

        """
        self.save = save
        self.folder = folder
        self.fmt = fmt
        self.dpi = dpi

    def config_3d(self, point_size: float = 0.3, cmap: str = "RdYlBu_r",
                  xlabel: str = r'$x_g$ [mm]',
                  ylabel: str = r'$y_g$ [mm]',
                  zlabel: str = r'$u(x_g, y_g)$ [mm]',
                  cbarlabel: str = "Aux",
                  x_lim: List = [-110, 110],
                  y_lim: List = [-38, 38],
                  z_lim: List = None,
                  zticks: int = 10,
                  zoom: float = 1) -> None:
        """
        Configure the 3D plot parameters.

        Parameters
        ----------
        point_size : float, optional
            Size of the points in the plot (default is 0.3).
        cmap : str, optional
            Colormap for the plot (default is "RdYlBu_r").
        xlabel : str, optional
            Label for the x-axis (default is r'$x_g$ [mm]').
        ylabel : str, optional
            Label for the y-axis (default is r'$y_g$ [mm]').
        zlabel : str, optional
            Label for the z-axis (default is r'$u(x_g, y_g)$ [mm]').
        cbarlabel : str, optional
            Label for the colourbar (default is 'Aux').
        x_lim : list of int, optional
            Limits for the x-axis (default is [-110, 110]).
        y_lim : list of int, optional
            Limits for the y-axis (default is [-38, 38]).
        z_lim : list of int or None, optional
            Limits for the z-axis (default is None).
        zticks : int, optional
            Number of ticks on the z-axis (default is 10).
        zoom : float, optional
            Zoom level for the plot (default is 1).

        Returns
        -------
        None

        """
        self.point_size = point_size
        self.cmap = cmap
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.zlabel = zlabel
        self.cbarlabel = cbarlabel
        self.x_lim = x_lim
        self.y_lim = y_lim
        self.z_lim = z_lim
        self.zticks = zticks
        self.zoom = zoom


    def set_limits(self, x: List[float] = None, y: List[float] = None, z: List[float] = None) -> None:
        """
        Set the limits for the x, y, and z axes.
    
        Parameters
        ----------
        x : List[float], optional
            The limits for the x-axis.
        y : List[float], optional
            The limits for the y-axis.
        z : List[float], optional
            The limits for the z-axis.
    
        Returns
        -------
        None

        """
        self.x_lim = x
        self.y_lim = y
        self.z_lim = z

    def views2D(self, *data: List[Topography]) -> None:
        """
        Generate 2D scatter plots for the XY, XZ, and YZ planes of multiple Topography objects.

        Parameters
        ----------
        data : List[Topography]
            A list of Topography objects for which 2D scatter plots will be generated.

        Returns
        -------
        None

        """
        plt.figure(dpi=300)
        for d in data:
            # XY plane
            plt.subplot(221)
            plt.scatter(d.P[:, 0], d.P[:, 1], s=1, alpha=1)
            plt.title('xy plane')
            plt.xlabel('x')
            plt.ylabel('y')

            # XZ plane
            plt.subplot(222)
            plt.scatter(d.P[:, 0], d.P[:, 2], s=1, alpha=1)
            plt.title('xz plane')
            plt.xlabel('x')
            plt.ylabel('z')

            # YZ plane
            plt.subplot(223)
            plt.scatter(d.P[:, 1], d.P[:, 2], s=1, alpha=1)
            plt.title('yz plane')
            plt.xlabel('y')
            plt.ylabel('z')
        plt.gcf().tight_layout(pad=1)
        plt.show()

    @printer
    def scatter3D(self, *data: List[Topography]) -> None:
        """
        Generate a 3D scatter plot for the given Topography data.

        Parameters
        ----------
        data : List[Topography]
            A list of Topography objects for which a 3D scatter plot will be generated.
        x_lim : List[float], optional
            Limits for the x-axis. Default is None.
        y_lim : List[float], optional
            Limits for the y-axis. Default is None.
        z_lim : List[float], optional
            Limits for the z-axis. Default is None.

        Returns
        -------
        None

        """
        fig = plt.figure(dpi=300)
        ax = fig.add_subplot(1, 1, 1, projection='3d')

        if self.x_lim is not None:
            ax.set_xlim(self.x_lim)
        if self.y_lim is not None:
            ax.set_ylim(self.y_lim)
        if self.z_lim is not None:
            ax.set_zlim(self.z_lim)
            vmin = self.z_lim[0]
            vmax = self.z_lim[1]
        else:
            vmin = np.array([h.m[2] for h in data]).min()
            vmax = np.array([h.M[2] for h in data]).max()
            ax.set_zlim([vmin, vmax])

        ax.set_xlabel(self.xlabel)
        ax.set_ylabel(self.ylabel)
        ax.set_zlabel(self.zlabel)

        ax.xaxis.pane.set_color('w')
        ax.yaxis.pane.set_edgecolor('w')
        ax.zaxis.pane.set_edgecolor('w')
        ax.xaxis.pane.set_color('w')
        ax.yaxis.pane.set_color('w')
        ax.zaxis.pane.set_color('w')

        plt.gca().xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.0f}"))
        plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.0f}"))
        plt.gca().zaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.2f}"))
    
        ax.xaxis._axinfo['grid'].update(color = 'grey', linestyle = ':', linewidth = 0.5)
        ax.yaxis._axinfo['grid'].update(color = 'grey', linestyle = ':', linewidth = 0.5)
        ax.zaxis._axinfo['grid'].update(color = 'grey', linestyle = ':', linewidth = 0.5)

        for d in data:
            sc = ax.scatter(d.P[:, 0], d.P[:, 1], d.P[:, 2], s=self.point_size, alpha=1,
                              vmin=vmin, vmax=vmax, c=d.P[:, 2],  marker="o",
                              cmap=self.cmap)

        # cbar = fig.colorbar(sc, ax=ax, orientation="vertical",
        #                     pad=0.12, format="%.2f",
        #                     ticks=list(np.linspace(vmin,
        #                                            vmax, 11)),
        #                     label=self.zlabel)
        # cbar.ax.tick_params(direction='in', right=1, left=1, size=2.5)

        # ax.axis('tight')
        ax.set_box_aspect(None, zoom=self.zoom)
        return fig, self.name

    @printer
    def scatter3DRegressorUnc(self, *data: List):
        """
        Create a 3D scatter plot of the regressor uncertainties.

        Parameters
        ----------
        data : List
            Set of Topographies.

        Returns
        -------
        matplotlib.figure.Figure
            The created figure.
        str
            The name of the plot.

        """
        fig = plt.figure(dpi=300)
        ax = fig.add_subplot(1, 1, 1, projection='3d')
        vmin = np.array([d.unc for d in data]).min()
        vmax = np.array([d.unc for d in data]).max()

        ax.set_xlabel(self.xlabel)
        ax.set_ylabel(self.ylabel)
        ax.set_zlabel(self.zlabel)

        ax.xaxis.pane.set_color('w')
        ax.yaxis.pane.set_edgecolor('w')
        ax.zaxis.pane.set_edgecolor('w')
        ax.xaxis.pane.set_color('w')
        ax.yaxis.pane.set_color('w')
        ax.zaxis.pane.set_color('w')

        plt.gca().xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.0f}"))
        plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.0f}"))
        plt.gca().zaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.2f}"))

        ax.xaxis._axinfo['grid'].update(color = 'grey', linestyle = ':', linewidth = 0.5)
        ax.yaxis._axinfo['grid'].update(color = 'grey', linestyle = ':', linewidth = 0.5)
        ax.zaxis._axinfo['grid'].update(color = 'grey', linestyle = ':', linewidth = 0.5)

        for d in data:
            sc = ax.scatter(d.P[:, 0], d.P[:, 1], d.P[:, 2], s=self.point_size, alpha=1,
                                vmin=vmin, vmax=vmax, c=d.unc,  marker="o",
                                cmap=self.cmap)

        cbar = fig.colorbar(sc, ax=ax, orientation="vertical",
                            pad=0.12, format="%.2e",
                            ticks=list(np.linspace(vmin,
                                                    vmax, 11)),
                            label=self.cbarlabel)
        cbar.ax.tick_params(direction='in', right=1, left=1, size=2.5)

        return fig, self.name

    def scatter3DRegression(self, regression: Topography, reference: Topography = None) -> None:
        fig = plt.figure(dpi=300)
        ax = fig.add_subplot(1, 1, 1, projection='3d')

        ax.set_xlabel("x [mm]")
        ax.set_ylabel("y [mm]")
        ax.set_zlabel("z [mm]")

        ax.xaxis.pane.set_color('w')
        ax.yaxis.pane.set_edgecolor('w')
        ax.zaxis.pane.set_edgecolor('w')
        ax.xaxis.pane.set_color('w')
        ax.yaxis.pane.set_color('w')
        ax.zaxis.pane.set_color('w')

        plt.gca().xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.0f}"))
        plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.1f}"))
        plt.gca().zaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.2f}"))

        ax.grid(True)
        vmin = regression.unc.min()
        vmax = regression.unc.max()

        # ax.scatter3D(regression.P[:, 0], regression.P[:, 1], regression.P[:, 2], s=2, alpha=1, c=regression.unc)
        ax.plot_trisurf(regression.P[:, 0], regression.P[:, 1], regression.P[:, 2],
                             alpha=1, cmap="RdYlBu", edgecolor=None, antialiased=True)

        sm = plt.cm.ScalarMappable(cmap="RdYlBu")
        sm.set_array(regression.unc)

        cbar = fig.colorbar(sm, ax=ax, orientation="vertical",
                            pad=0.12, format="%.3f",
                            ticks=list(np.linspace(vmin, vmax, 11)),
                            label='Uncertainty')
        cbar.ax.tick_params(direction='in', right=1, left=1, size=2.5)

        if reference is not None:
            ax.scatter3D(reference.P[:, 0], reference.P[:, 1], reference.P[:, 2], s=2, alpha=1)

        ax.axis('tight')
        plt.show()

    def contour(self, topography):
        fig, ax = plt.subplots(dpi=300)
        ax.tricontourf(topography.P[:, 0], topography.P[:, 1], topography.P[:, 2])
        plt.show()


class PostViewer:

    def __init__(self, **kwargs) -> None:

        try:
            self.name = kwargs.pop("name")
        except KeyError:
            self.name = "Untitled"

        self.config()
        self.config_scan_view()
        self.config_canvas()

    def config(self, save: bool = False, folder: str = "./", fmt: str = "png", dpi: int = 300) -> None:
        """
        Configure settings for saving plots.

        Borrowed from https://github.com/aletgn/b-fade/

        Parameters
        ----------
        save : bool, optional
            Flag indicating whether to save plots. The default is False.
        folder : str, optional
            Folder path where plots will be saved. The default is "./".
        fmt : str, optional
            Format for saving plots. The default is "png".
        dpi : int, optional
            Dots per inch for saving plots. The default is 300.

        Returns
        -------
        None

        """
        self.save = save
        self.folder = folder
        self.fmt = fmt
        self.dpi = dpi

    def config_scan_view(self, xlabel=r'$x$ [mm]', ylabel=r'$y$ [mm]', x_lim=[-20, 20], 
                         y_lim=[-70, 70], legend_config = None):

        self.xlabel = xlabel
        self.ylabel = ylabel
        self.x_lim = x_lim
        self.y_lim = y_lim
        self.legend_config = legend_config

    def config_canvas(self, cmap: str = "RdYlBu_r", levels: int = 8,
                      x_lim: List[float] = [-100, 100], y_lim_top: List[float] = [10,20],
                      y_lim_bot: List[float] = [-10,-20], y_lim_scan: str = [-140, 140],
                      cbar_lim: List[float] = [-140, 140], loc: str = "best",
                      bbox_to_anchor: List[float] = None) -> None:
        """
        Configure canvas for plotting.

        Parameters
        ----------
        cmap : str, optional
            Colormap to use for plotting. Default is "RdYlBu_r".
        levels : int, optional
            Number of levels for the colorbar. Default is 8.
        x_lim : List[float], optional
            Limits for the x-axis. Default is [-100, 100].
        y_lim_top : List[float], optional
            Limits for the top part of the y-axis. Default is [10, 20].
        y_lim_bot : List[float], optional
            Limits for the bottom part of the y-axis. Default is [-10, -20].
        y_lim_scan : List[float], optional
            Limits for the y-axis for scan data. Default is [-140, 140].
        cbar_lim : List[float], optional
            Limits for the color bar. Default is [-140, 140].
        loc : str, optional
            Location of the legend. Default is "best".
        bbox_to_anchor : List[float], optional
            Anchor point for the legend bounding box. Default is None.

        Returns
        -------
        None
            This function does not return anything. It only sets instance attributes.
        """
        self.cmap = cmap
        self.levels = levels

        self.x_lim = x_lim
        self.y_lim_top = y_lim_top
        self.y_lim_bot = y_lim_bot
        self.y_lim_scan = y_lim_scan

        self.mean_lim = cbar_lim
        self.std_lim = cbar_lim

        self.loc = loc
        self.bbox_to_anchor = bbox_to_anchor

    def config_colourbar(self, top = None, bot = None) -> None:
        """
        Configure color bar limits based on top and bottom bounds.

        Parameters
        ----------
        top : Tuple
            Tuple containing data for the top bounds. It should contain the mean and standard deviation.
        bot : Tuple
            Tuple containing data for the bottom bounds. It should contain the mean and standard deviation.

        Returns
        -------
        None
            This function does not return anything. It only sets the instance attributes for color bar limits.

        """
        self.mean_lim =  cbar_bounds(bot[2], top[2])
        self.std_lim = cbar_bounds(bot[3], top[3])

    def scan_view(self, swap: bool = False, *scan: List) -> None:
        """
        Plot scan data.

        Parameters
        ----------
        swap : bool, optional
            If True, swap x and y axes in the plot. Default is False.
        *scan : List
            List of scan data to plot. Each scan data should be provided as a list-like object.

        Returns
        -------
        None

        """
        fig, ax = plt.subplots(dpi=300)
        for s in scan:
            if swap:
                ax.plot(s.y, s.x)

            else:
                ax.plot(s.x, s.y)

        plt.show()

    def scan_view_and_fill(self, swap: bool = False, *scan: List) -> None:
        """
        Plot scan data with filled error regions.

        Parameters
        ----------
        swap : bool, optional
            If True, swap x and y axes in the plot. Default is False.
        *scan : List
            List of scan data to plot. Each scan data should be provided as a list-like object.

        Returns
        -------
        None

        """
        fig, ax = plt.subplots(dpi=300)
        for s in scan:
            if swap:
                if s.y_err is not None:
                    ax.fill_betweenx(s.x, s.y-s.y_err, s.y+s.y_err, alpha=0.5, edgecolor="none")
                ax.plot(s.y, s.x)

            else:
                if s.y_err is not None:
                    ax.fill_between(s.x, s.y-s.y_err, s.y+s.y_err, alpha=0.5, edgecolor="none")
                ax.plot(s.x, s.y)

        plt.show()

    @printer
    def scan_view_and_bar(self, swap: bool = False, strip: Dict = None, *scan: List) -> None:
        """
        Plot scan data with error bars.

        Parameters
        ----------
        swap : bool, optional
            If True, swap x and y axes in the plot. Default is False.
        scan : List
            List of scan data to plot. Each scan data should be provided as a list-like object.
        strip : Dict
            Dictionary containing the information to draw a strip over the plot.

        Example
        -------
            strip = {"xs": [-10, 10], "label": "FILL", "color": "grey", "alpha": 0.2,
                 "labelleft": "LEFT", "labelright": "RIGHT", "epsh": 5, "epsv": 10}
        Returns
        -------
        None

        """
        fig, ax = plt.subplots(dpi=300)
        for s in scan:
            if swap:
                if s.y_err is not None:
                    ax.errorbar(s.y, s.x, xerr=s.y_err, yerr=None, fmt="o",
                                markersize=3, capsize=3, capthick=1, linewidth=0.8)
                pass

            else:
                if s.y_err is not None:
                    ax.errorbar(s.x, s.y, xerr=None, yerr=s.y_err, fmt="o", c=s.color,
                                linestyle=s.line, markersize=3, capsize=3, capthick=1, linewidth=0.8, label=s.name)

        ax.set_xlabel(self.xlabel)
        ax.set_ylabel(self.ylabel)
        ax.set_xlim(self.x_lim)
        ax.set_ylim(self.y_lim)
        ax.tick_params(direction="in", top=1, right=1, color="k")

        if strip is not None:
            ax.fill_betweenx(self.y_lim, strip["xs"][0], strip["xs"][1], edgecolor="none", linewidth=0,
                            color=strip["color"], alpha=strip["alpha"], zorder=0)
            ax.text(0.5*strip["xs"][0]+0.5*strip["xs"][1], self.y_lim[1]-strip["epsv"], strip["label"],
                    horizontalalignment='center', verticalalignment='center')
            ax.text(strip["xs"][0]-strip["epsh"], self.y_lim[0]+strip["epsv"], strip["labelleft"],
                    horizontalalignment='center', verticalalignment='center')
            ax.text(strip["xs"][1]+strip["epsh"], self.y_lim[0]+strip["epsv"], strip["labelright"],
                    horizontalalignment='center', verticalalignment='center')

        try:
            ax.legend(**self.legend_config)
        except:
            pass

        return fig, self.name

    @printer
    def scan_compare(self, fills: List, bars: List, regular: List = None, strip: Dict = None) -> Tuple:
        """
        Compare scans by plotting filled regions and error bars.

        Parameters
        ----------
        fills : list of scans
            List of data for the filled regions.
        bars : list of scans
            List of data for the error bars.
        regular : list of scans
            List of data for without fills and bars. The default is None

        Returns
        -------
        fig : Figure
            The matplotlib figure object.
        name : str
            The name associated with the plot.
        strip : Dict
            Dictionary containing the information to draw a strip over the plot.

        Example
        -------
            strip = {"xs": [-10, 10], "label": "FILL", "color": "grey", "alpha": 0.2,
                 "labelleft": "LEFT", "labelright": "RIGHT", "epsh": 5, "epsv": 10}

        """
        fig, ax = plt.subplots(dpi=300)
        for f in fills:
            ax.fill_between(f.x, f.y-f.y_err, f.y+f.y_err, color=f.color, alpha=f.alpha, edgecolor="none", zorder=1)
            ax.plot(f.x, f.y, color=f.color, label=f.name)
        for b in bars:
            ax.errorbar(b.x, b.y, xerr=None, yerr=b.y_err, fmt="o", c=b.color,
                                    linestyle=b.line, markersize=3, capsize=3,
                                    capthick=1, linewidth=0.8, label=b.name, zorder=2)
        if regular is not None:
            for r in regular:
                ax.plot(r.x, r.y, color=r.color, marker=r.marker, markersize=3, label=r.name)

        ax.set_xlim(self.x_lim)
        ax.set_ylim(self.y_lim)
        ax.set_xlabel(self.xlabel)
        ax.set_ylabel(self.ylabel)

        if strip is not None:
            ax.fill_betweenx(self.y_lim, strip["xs"][0], strip["xs"][1], edgecolor="none", linewidth=0,
                            color=strip["color"], alpha=strip["alpha"], zorder=0)
            ax.text(0.5*strip["xs"][0]+0.5*strip["xs"][1], self.y_lim[1]-strip["epsv"], strip["label"],
                    horizontalalignment='center', verticalalignment='center')
            ax.text(strip["xs"][0]-strip["epsh"], self.y_lim[0]+strip["epsv"], strip["labelleft"],
                    horizontalalignment='center', verticalalignment='center')
            ax.text(strip["xs"][1]+strip["epsh"], self.y_lim[0]+strip["epsv"], strip["labelright"],
                    horizontalalignment='center', verticalalignment='center')
        ax.tick_params(direction="in", top=1, right=1, color="k")
        ax.legend(**self.legend_config)

        return fig, self.name

    @printer
    def basic_contour(self, top_cnt, bot_cnt, cbarlabeltop: str = "Expected Value") -> Tuple:
        fig = plt.figure(dpi=self.dpi, figsize=(4,2))
        gs = GridSpec(2, 2, figure=fig,
                        width_ratios=[0.975, 0.025],
                        height_ratios=[0.5, 0.5])
        ax1 = fig.add_subplot(gs[0, 0])
        ax2 = fig.add_subplot(gs[1, 0])
        ax3 = fig.add_subplot(gs[0:2, 1])

        im12, norm12 = discrete_colorbar(self.cmap, self.mean_lim[0], self.mean_lim[1], self.levels)
        a1 = ax1.tricontourf(top_cnt.P[:,0], top_cnt.P[:,1], top_cnt.P[:,2], levels=self.levels, cmap=self.cmap, norm=norm12)
        a2 = ax2.tricontourf(bot_cnt.P[:,0], bot_cnt.P[:,1], bot_cnt.P[:,2], levels=self.levels, cmap=self.cmap, norm=norm12)
        cb1 = fig.colorbar(im12, ax=[a1,a2], cax=ax3, orientation='vertical', label=cbarlabeltop, format="%.0f", pad=0.1, fraction=0.5,
                        ticks=(np.linspace(self.mean_lim[0], self.mean_lim[1], self.levels)))

        for a in [ax1, ax2]:
            a.tick_params(direction="in", top=1, right=1, color="k") # pad=5
            a.set_xlabel(self.xlabel)
            a.set_xticks([-50, 0, 50])
            a.set_ylabel(self.ylabel)

        cb1.ax.tick_params(direction='in', right=1, left=1, size=1.5, labelsize=8)

        plt.tight_layout()
        return fig, self.name

    @printer
    def contour(self, top_cnt, bot_cnt, cbarlabeltop: str = "Expected Value", cbarlabelbot: str = "Uncertainty") -> Tuple:
        """
        Create contour plots for the provided data.

        Parameters
        ----------
        top_cnt : Topography object
            Data for the top contour plot.
        bot_cnt : Topography object
            Data for the bottom contour plot.
        cbarlabeltop : str
            Label of the top colour bar
        cbarlabelbot : str
            Label of the bot colour bar

        Returns
        -------
        fig : Figure
            The matplotlib figure object.
        name : str
            The name associated with the plot.

        """
        fig = plt.figure(dpi=self.dpi, figsize=(4,4))
        gs = GridSpec(4, 2, figure=fig,
                        width_ratios=[0.975, 0.025],
                        height_ratios=[0.25, 0.25, 0.25, 0.25])
        ax1 = fig.add_subplot(gs[0, 0])
        ax2 = fig.add_subplot(gs[1, 0])
        ax3 = fig.add_subplot(gs[0:2, 1])
        ax4 = fig.add_subplot(gs[2, 0])
        ax5 = fig.add_subplot(gs[3, 0])
        ax6 = fig.add_subplot(gs[2:4, 1])

        im12, norm12 = discrete_colorbar(self.cmap, self.mean_lim[0], self.mean_lim[1], self.levels)
        a1 = ax1.tricontourf(top_cnt.P[:,0], top_cnt.P[:,1], top_cnt.P[:,2], levels=self.levels, cmap=self.cmap, norm=norm12)
        a2 = ax2.tricontourf(bot_cnt.P[:,0], bot_cnt.P[:,1], bot_cnt.P[:,2], levels=self.levels, cmap=self.cmap, norm=norm12)
        cb1 = fig.colorbar(im12, ax=[a1,a2], cax=ax3, orientation='vertical', label=cbarlabeltop, format="%.0f", pad=0.1, fraction=0.5,
                        ticks=(np.linspace(self.mean_lim[0], self.mean_lim[1], self.levels)))

        im45, norm45 = discrete_colorbar(self.cmap, self.std_lim[0], self.std_lim[1], self.levels)
        a4 = ax4.tricontourf(top_cnt.P[:,0], top_cnt.P[:,1], top_cnt.unc, levels=self.levels, cmap=self.cmap, norm=norm45)
        a5 = ax5.tricontourf(bot_cnt.P[:,0], bot_cnt.P[:,1], bot_cnt.unc, levels=self.levels, cmap=self.cmap, norm=norm45)
        cb2 = fig.colorbar(im45, cax=ax6, orientation='vertical', label=cbarlabelbot, format="%.0f", pad=0.1,
                        ticks=list(np.linspace(self.std_lim[0], self.std_lim[1], self.levels)))

        for a in [ax1, ax2, ax4, ax5]:
            a.tick_params(direction="in", top=1, right=1, color="k") # pad=5
            a.set_xlabel(self.xlabel)
            a.set_ylabel(self.ylabel)

        for c in [cb1, cb2]:
            c.ax.tick_params(direction='in', right=1, left=1, size=1.5, labelsize=8)

        plt.tight_layout()
        return fig, self.name

    def contour_and_scan_2(self, top_cnt, bot_cnt, top_scan = None, bot_scan = None,
                           top_err = None, bot_err = None) -> None:
        """
        Plot contour and scan data.

        Parameters
        ----------
        top_cnt : object
            Object containing data for the top contours.
        bot_cnt : object
            Object containing data for the bottom contours.
        top_scan : object, optional
            Object containing data for the top scan. Default is None.
        bot_scan : object, optional
            Object containing data for the bottom scan. Default is None.
        top_err : object, optional
            Object containing data for the top scan. Default is None.
        bot_err : object, optional
            Object containing data for the bottom scan. Default is None.

        Returns
        -------
        None
            This function does not return anything. It only displays the plot.

        """
        fig = plt.figure(dpi=self.dpi)
        gs = GridSpec(6, 2, figure=fig,
                        width_ratios=[0.975, 0.025],
                        height_ratios=[0.1, 0.1, 0.1, 0.1, 0.3, 0.3])
        ax1 = fig.add_subplot(gs[0, 0])
        ax2 = fig.add_subplot(gs[1, 0])
        ax3 = fig.add_subplot(gs[0:2, 1])
        ax4 = fig.add_subplot(gs[2, 0])
        ax5 = fig.add_subplot(gs[3, 0])
        ax6 = fig.add_subplot(gs[2:4, 1])
        ax7 = fig.add_subplot(gs[4, 0])
        ax8 = fig.add_subplot(gs[5, 0])

        top_ = [ax1, ax4]
        bot_ = [ax2, ax5]
        mean_cnt = [ax1, ax2]
        std_cnt = [ax4, ax5]
        scans = [ax7, ax8]
        all_axs = [ax1, ax2, ax4, ax5, ax7, ax8]

        im12, norm12 = discrete_colorbar(self.cmap, self.mean_lim[0], self.mean_lim[1], self.levels)
        a1 = ax1.tricontourf(top_cnt.P[:,0], top_cnt.P[:,1], top_cnt.P[:,2], levels=self.levels, cmap=self.cmap, norm=norm12)
        a2 = ax2.tricontourf(bot_cnt.P[:,0], bot_cnt.P[:,1], bot_cnt.P[:,2], levels=self.levels, cmap=self.cmap, norm=norm12)
        # ax1.tricontour(top_cnt.P[:,0], top_cnt.P[:,1], top_cnt.P[:,2], levels=levels, colors="k", linewidths=0.2, linestyles="-", alpha=0.5)
        # ax2.tricontour(bot_cnt.P[:,0], bot_cnt.P[:,1], bot_cnt.P[:,2], levels=levels, colors="k", linewidths=0.2, linestyles="-", alpha=0.5)
        cb1 = fig.colorbar(im12, ax=[a1,a2], cax=ax3, orientation='vertical', label="Expected Value", pad=0.1, fraction=0.5,
                        ticks=(np.linspace(self.mean_lim[0], self.mean_lim[1], self.levels)))

        im45, norm45 = discrete_colorbar(self.cmap, self.std_lim[0], self.std_lim[1], self.levels)
        a4 = ax4.tricontourf(top_cnt.P[:,0], top_cnt.P[:,1], top_cnt.unc, levels=self.levels, cmap=self.cmap, norm=norm45)
        a5 = ax5.tricontourf(bot_cnt.P[:,0], bot_cnt.P[:,1], bot_cnt.unc, levels=self.levels, cmap=self.cmap, norm=norm45)
        # ax4.tricontour(top_cnt.P[:,0], top_cnt.P[:,1], top_cnt.unc, levels=levels, colors="k", linewidths=0.2, linestyles="-", alpha=0.5)
        # ax5.tricontour(bot_cnt.P[:,0], bot_cnt.P[:,1], bot_cnt.unc, levels=levels, colors="k", linewidths=0.2, linestyles="-", alpha=0.5)
        cb2 = fig.colorbar(im45, cax=ax6, orientation='vertical', label="Uncertainty", pad=0.1,
                        ticks=list(np.linspace(self.std_lim[0], self.std_lim[1], self.levels)))

        ax7.plot(top_scan.x, top_scan.y, top_scan.color, zorder=0, label=top_scan.name)
        ax7.fill_between(top_scan.x, top_scan.y-top_scan.y_err, top_scan.y+top_scan.y_err,
                        color=top_scan.color, alpha=top_scan.alpha, zorder=-1, edgecolor="none")
        if top_err is not None:
            ax7.errorbar(top_err.x, top_err.y, top_err.y_err, c=top_err.color, label=top_err.name,
                         markersize=3, capsize=3, capthick=1, linewidth=0.8)

        ax8.plot(bot_scan.x, bot_scan.y, bot_scan.color, zorder=0, label=bot_scan.name)
        ax8.fill_between(bot_scan.x, bot_scan.y-bot_scan.y_err, bot_scan.y+bot_scan.y_err,
                        color=bot_scan.color, alpha=bot_scan.alpha, zorder=-1, edgecolor="none")

        if bot_err is not None:
            ax8.errorbar(bot_err.x, bot_err.y, bot_err.y_err, c=bot_err.color, label=bot_err.name,
                         markersize=3, capsize=3, capthick=1, linewidth=0.8)

        for a in all_axs:
            a.tick_params(direction="in", top=1, right=1, color="k") # pad=5
            a.set_xlim(self.x_lim)
            a.set_xticks(np.linspace(self.x_lim[0], self.x_lim[1], 10))

        for t in top_:
            t.set_ylim(self.y_lim_top)
            t.set_yticks(self.y_lim_top)

        for b in bot_:
            b.set_ylim(self.y_lim_bot)
            b.set_yticks(self.y_lim_bot)

        for s in scans:
            s.set_yticks(np.linspace(self.y_lim_scan[0], self.y_lim_scan[1], 5))
            s.set_ylim(self.y_lim_scan)

        for c in [cb1, cb2]:
            c.ax.tick_params(direction='in', right=1, left=1, size=1.5, labelsize=8)

        if self.bbox_to_anchor is None:
            # fig.legend(loc=self.loc)
            pass
        else:
            fig.legend(loc=self.loc, bbox_to_anchor=self.bbox_to_anchor)
        plt.tight_layout()
        plt.show()
        # plt.savefig("/home/ale/Desktop/exp/test.png", dpi=300, format="png")


def cfg_matplotlib(font_size: int = 12, font_family: str = 'sans-serif', use_latex: bool = False, interactive: bool = False) -> None:
    """
    Set Matplotlib RC parameters for font size, font family, and LaTeX usage.

    Borrowed from https://github.com/aletgn/b-fade/blob/master/src/bfade/util.py

    Parameters
    ----------
    font_size : int, optional
        Font size. The default is 12.

    font_family : str, optional
        Font family. The default is 'sans-serif'.

    use_latex : bool, optional
        Enable LaTeX text rendering. The default is False.

    interactive: bool, optional
        Whether to keep matplotlib windows open.

    Returns
    -------
    None

    """
    matplotlib.rcParams['font.size'] = font_size
    matplotlib.rcParams['font.family'] = font_family
    matplotlib.rcParams['text.usetex'] = use_latex
    matplotlib.rcParams["interactive"] = interactive


def cbar_bounds(v: np.ndarray, w: np.ndarray) -> Tuple[float]:
    """
    Calculate the lower and upper bounds for color bar.

    Parameters
    ----------
    v : np.ndarray
        First array for comparison.
    w : np.ndarray
        Second array for comparison.

    Returns
    -------
    Tuple[float]
        A tuple containing the lower and upper bounds for the color bar.

    """
    return min(v.min(), w.min()), max(v.max(), w.max())


def discrete_colorbar(cmap: str, lower_bound: float, upper_bound: float, levels: int) -> Tuple[cm.ScalarMappable, BoundaryNorm]:
    """
    Create a discrete colorbar with custom colormap and bounds.

    Parameters
    ----------
    cmap : str
        Name of the colormap to use.
    lower_bound : float
        Lower bound for the colorbar.
    upper_bound : float
        Upper bound for the colorbar.
    levels : int
        Number of discrete levels for the colorbar.

    Returns
    -------
    Tuple[plt.ScalarMappable, BoundaryNorm]
        A tuple containing the ScalarMappable object for mapping scalar data to colors,
        and the BoundaryNorm object for normalizing scalar data to the colormap's range.

    """
    cmap = getattr(plt.cm, cmap) # get cmap
    cmaplist = [cmap(i) for i in range(cmap.N)] # get cmap colours
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list('Custom cmap', cmaplist, cmap.N)
    bounds = np.linspace(lower_bound, upper_bound, levels)
    norm = BoundaryNorm(bounds, cmap.N)
    cbar = cm.ScalarMappable(norm=norm, cmap=cmap)
    return cbar, norm