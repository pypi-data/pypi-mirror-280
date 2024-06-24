# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: 2015-2023 Tanguy Fardet
# SPDX-License-Identifier: GPL-3.0-or-later
# nngt/core/spatial_graph.py

""" SpatialGraph class for spatial graph generation and management """

import numpy as np

import nngt
from nngt.lib import InvalidArgument, nonstring_container

from .connections import Connections
from .graph import Graph


# ------------ #
# SpatialGraph #
# ------------ #

class SpatialGraph(Graph):

    """
    The detailed class that inherits from :class:`~nngt.Graph` and implements
    additional properties to describe spatial graphs (i.e. graph where the
    structure is embedded in space.
    """

    # ------------------------------------------------------------------------
    # Class properties

    __num_graphs = 0
    __max_id = 0

    # ------------------------------------------------------------------------
    # Constructor, destructor, attributes

    def __init__(self, nodes=0, name="SpatialGraph", weighted=True,
                 directed=True, copy_graph=None, shape=None, positions=None,
                 **kwargs):
        '''
        Initialize SpatialClass instance.

        .. versionchanged: 2.4
            Move `from_graph` to `copy_graph` to reflect changes in Graph.

        Parameters
        ----------
        nodes : int, optional (default: 0)
            Number of nodes in the graph.
        name : string, optional (default: "Graph")
            The name of this :class:`Graph` instance.
        weighted : bool, optional (default: True)
            Whether the graph edges have weight properties.
        directed : bool, optional (default: True)
            Whether the graph is directed or undirected.
        shape : :class:`~nngt.geometry.Shape`, optional (default: None)
            Shape of the neurons' environment (None leads to a square of
            side 1 cm)
        positions : :class:`numpy.array` (N, 2), optional (default: None)
            Positions of the neurons; if not specified and `nodes` is not 0,
            then neurons will be reparted at random inside the
            :class:`~nngt.geometry.Shape` object of the instance.
        **kwargs : keyword arguments for :class:`~nngt.Graph` or
            :class:`~nngt.geometry.Shape` if no shape was given.

        Returns
        -------
        self : :class:`~nggt.SpatialGraph`
        '''
        self.__id = self.__class__.__max_id
        self.__class__.__num_graphs += 1
        self.__class__.__max_id += 1

        self._shape = None
        self._pos = None

        super().__init__(nodes, name=name, weighted=weighted,
                         directed=directed, copy_graph=copy_graph, **kwargs)

        self._init_spatial_properties(shape, positions, **kwargs)

    def __del__(self):
        if hasattr(self, '_shape'):
            if self._shape is not None:
                self._shape._parent = None
            self._shape = None

        super().__del__()

        self.__class__.__num_graphs -= 1

    @property
    def shape(self):
        ''' The environment's spatial structure. '''
        return self._shape

    # -------------------------------------------------------------------------
    # Init tool

    def _init_spatial_properties(self, shape, positions=None, **kwargs):
        '''
        Create the positions of the neurons from the graph `shape` attribute
        and computes the connections distances.
        '''
        positions = None if positions is None else np.asarray(positions)

        self.new_edge_attribute('distance', 'double')

        if positions is not None and len(positions) != self.node_nb():
            raise InvalidArgument("Wrong number of neurons in `positions`.")

        if shape is not None:
            shape.set_parent(self)
            self._shape = shape
        else:
            if positions is None or not np.any(positions):
                if 'height' in kwargs and 'width' in kwargs:
                    self._shape = nngt.geometry.Shape.rectangle(
                        kwargs['height'], kwargs['width'], parent=self)
                elif 'radius' in kwargs:
                    self._shape = nngt.geometry.Shape.disk(
                        kwargs['radius'], parent=self)
                elif 'radii' in kwargs:
                    self._shape = nngt.geometry.Shape.ellipse(
                        kwargs['radii'], parent=self)
                elif 'polygon' in kwargs:
                    self._shape = nngt.geometry.Shape.from_polygon(
                        kwargs['polygon'], min_x=kwargs.get('min_x', -5000.),
                        max_x=kwargs.get('max_x', 5000.),
                        unit=kwargs.get('unit', 'um'), parent=self)
                else:
                    raise RuntimeError('SpatialGraph needs a `shape` or '
                                       'keywords arguments to build one, or '
                                       'at least `positions` so it can create '
                                       'a square containing them')
            else:
                minx, maxx = np.min(positions[:, 0]), np.max(positions[:, 0])
                miny, maxy = np.min(positions[:, 1]), np.max(positions[:, 1])

                height, width = 1.01*(maxy - miny), 1.01*(maxx - minx)

                centroid = (0.5*(maxx + minx), 0.5*(maxy + miny))

                if height == 0:
                    height = 0.1*width

                if width == 0:
                    width = 0.1*height

                self._shape = nngt.geometry.Shape.rectangle(
                    height, width, centroid=centroid, parent=self)

        b_rnd_pos = True if not self.node_nb() or positions is None else False
        self._pos = self._shape.seed_neurons() if b_rnd_pos else positions

        Connections.distances(self)

    # ------------------------------------------------------------------------
    # Positions

    def get_positions(self, nodes=None):
        '''
        Returns a copy of the nodes' positions as a (N, 2) array.

        Parameters
        ----------
        nodes : int or array-like, optional (default: all nodes)
            List of the nodes for which the position should be returned.
        '''
        if nodes is not None:
            if nonstring_container(nodes):
                # numpy slicing does not work with everything
                nodes = np.asarray(nodes)

                return np.array(self._pos[nodes])
            else:
                return self._pos[nodes]

        return np.array(self._pos)

    def set_positions(self, positions, nodes=None):
        '''
        Set the nodes' positions as a (N, 2) array.

        Parameters
        ----------
        positions : array-like
            List of positions, of shape (N, 2).
        nodes : int or array-like, optional (default: all nodes)
            List of the nodes for which the position should be set.
        '''
        if nodes is not None:
            self._pos[nodes] = positions
        else:
            if len(positions) != self.node_nb():
                raise ValueError("One position per node is required.")
            self._pos = np.array(positions)
