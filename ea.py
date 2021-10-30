#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import logging
import numpy as np

import dcm


class EulerAngle:

    def __init__(self, axes, angles):
        self.angles = [ math.radians(angle) for angle in angles ]
        self.axes = [ int(a) for a in axes ]

    def show(self):
        print("axes: %s" % self.axes)
        print("angles: %s" % self.angles)

    def __str__(self):
        return "EulerAngle -- axes: %s, angles: %s" % (self.axes, self.angles)

    def get_single_axis_rotation_matrix(self, axis, angle):
        logging.debug("Getting rotation matrix about axis %s by angle %s" % (axis, angle))
        if axis == 1:
            return np.matrix((
                       (1, 0, 0),
                       (0, np.cos(angle), np.sin(angle)),
                       (0, -np.sin(angle), np.cos(angle)) ))
        elif axis == 2:
            return np.matrix((
                       (np.cos(angle), 0, -np.sin(angle)),
                       (0, 1, 0),
                       (np.sin(angle), 0, np.cos(angle)) ))
        elif axis == 3:
            return np.matrix((
                       (np.cos(angle), np.sin(angle), 0),
                       (-np.sin(angle), np.cos(angle), 0),
                       (0, 0, 1) ))
        else:
            raise Exception

    def to_direction_cosine_matrix(self):
        """ Convert this Euler Angle set into its corresponding DCM """
        m3 = self.get_single_axis_rotation_matrix(self.axes[0], self.angles[0])
        m2 = self.get_single_axis_rotation_matrix(self.axes[1], self.angles[1])
        m1 = self.get_single_axis_rotation_matrix(self.axes[2], self.angles[2])
        dcm_m = np.dot(np.dot(m1, m2), m3)
        return dcm.directionCosineMatrix(dcm_m)

