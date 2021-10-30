#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import logging
import numpy as np

import ea

class directionCosineMatrix:

    def __init__(self, m):
        self.m = m

    def show(self):
        pass

    def is_valid(self):
        pass

    def normalise(self):
        pass

    def add(self, other_dcm):
        return dot(self.m, other_dcm)

    def subtract(self, other_dcm):
        pass

    def to_euler_angles(self):
        theta1 = np.arctan(self.m[0,1] / self.m[0,0])
        theta2 = np.arcsin(self.m[0,2])
        theta3 = np.arctan(self.m[1,2] / self.m[2,2])
        logging.debug("theta1: %s, theta2: %s, theta3: %s" % (theta1, theta2, theta3))
        return ea.EulerAngle("321", [theta1, theta2, theta3])

    def to_principle_rotation_vector(self):
        pass
