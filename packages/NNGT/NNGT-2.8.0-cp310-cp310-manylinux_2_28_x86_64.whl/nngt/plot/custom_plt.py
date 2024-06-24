# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: 2015-2023 Tanguy Fardet
# SPDX-License-Identifier: GPL-3.0-or-later
# nngt/plot/custom_plt.py

""" Matplotlib customization """

import logging

import matplotlib as mpl
from matplotlib.colors import Colormap
from matplotlib.markers import MarkerStyle as MS

import nngt
from nngt.lib.logger import _log_message


logger = logging.getLogger(__name__)

# ---------------- #
# Customize PyPlot #
# ---------------- #

with_seaborn = False


def get_cmap(colormap, n=None):
    '''
    Get a colormap.

    Parameters
    ----------
    colormap : str or colormap
        Colormap to return.
    n : int, optional
        Take `n` samples from the colormap.
    '''
    if not isinstance(colormap, Colormap):
        colormap = mpl.colormaps[colormap]

    if n is None:
        return colormap

    return colormap.resampled(n)


def palette_continuous(numbers=None):
    pal = get_cmap(nngt._config["palette_continuous"])
    if numbers is None:
        return pal
    else:
        return pal(numbers)


def palette_discrete(numbers=None):
    pal = get_cmap(nngt._config["palette_discrete"])
    if numbers is None:
        return pal
    else:
        return pal(numbers)


# markers list
markers = [m for m in MS.filled_markers if m != '.']

if nngt._config["color_lib"] == "seaborn":
    try:
        import seaborn as sns
        with_seaborn = True
        sns.set_style("whitegrid")

        def sns_palette(c):
            if isinstance(c, float):
                pal = sns.color_palette(nngt._config["palette"], 100)
                return pal[int(c*100)]
            else:
                return sns.color_palette(nngt._config["palette"], len(c))

        palette_continuous = sns_palette
    except ImportError as e:
        _log_message(logger, "WARNING",
                     "`seaborn` requested but could not set it: {}.".format(e))


if not with_seaborn:
    try:
        mpl.rcParams['font.size'] = 12
        mpl.rcParams['font.family'] = 'serif'
        if nngt._config['use_tex']:
            mpl.rc('text', usetex=True)
        mpl.rcParams['axes.labelsize'] = mpl.rcParams['font.size']
        mpl.rcParams['axes.titlesize'] = 1.2*mpl.rcParams['font.size']
        mpl.rcParams['legend.fontsize'] = mpl.rcParams['font.size']
        mpl.rcParams['xtick.labelsize'] = mpl.rcParams['font.size']
        mpl.rcParams['ytick.labelsize'] = mpl.rcParams['font.size']
        mpl.rcParams['savefig.dpi'] = 300
        mpl.rcParams['savefig.format'] = 'pdf'
        mpl.rcParams['xtick.major.size'] = 3
        mpl.rcParams['xtick.minor.size'] = 3
        mpl.rcParams['xtick.major.width'] = 1
        mpl.rcParams['xtick.minor.width'] = 1
        mpl.rcParams['ytick.major.size'] = 3
        mpl.rcParams['ytick.minor.size'] = 3
        mpl.rcParams['ytick.major.width'] = 1
        mpl.rcParams['ytick.minor.width'] = 1
        mpl.rcParams['legend.frameon'] = False
        mpl.rcParams['legend.numpoints'] = 1
        mpl.rcParams['axes.linewidth'] = 1
        mpl.rcParams['axes.grid'] = True
        mpl.rcParams['grid.linestyle'] = ':'
        mpl.rcParams['path.simplify'] = True
    except Exception as e:
        _log_message(logger, "WARNING",
                     "Error configuring `matplotlib`: {}.".format(e))


def format_exponent(ax, axis='y', pos=(1.,0.), valign="top", halign="right"):
    import matplotlib.pyplot as plt
    # Change the ticklabel format to scientific format
    ax.ticklabel_format(axis=axis, style='sci', scilimits=(-3, 2))
    # Get the appropriate axis
    if axis == 'y':
        ax_axis = ax.yaxis
    else:
        ax_axis = ax.xaxis
    # Run plt.tight_layout() because otherwise the offset text doesn't update
    plt.tight_layout()
    ##### THIS IS A BUG
    ##### Well, at least it's sub-optimal because you might not
    ##### want to use tight_layout(). If anyone has a better way of
    ##### ensuring the offset text is updated appropriately
    ##### please comment!

    # Get the offset value
    offset = ax_axis.get_offset_text().get_text()
    if len(offset) > 0:
        # Get that exponent value and change it into latex format
        minus_sign = u'\u2212'
        expo = float(offset.replace(minus_sign, '-').split('e')[-1])
        offset_text = r'x$\mathregular{10^{%d}}$' %expo
        # Turn off the offset text that's calculated automatically
        ax_axis.offsetText.set_visible(False)
        ax.text(pos[0], pos[1], offset_text, transform=ax.transAxes,
               horizontalalignment=halign,
               verticalalignment=valign)
    return ax
