#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import numpy as np

from mrp import ModifiedRodriguesParameters

logging.basicConfig(level=logging.DEBUG)

## Question 1

# Spacecraft inertia tensor about center of mass in the body frame
# B[Ic]
B_I_c = np.array([
            [10, 1, -1],
            [1,  5,  1],
            [-1, 1,  8] ])

# Orientation of docking port D relative to body
# MRP σ_D/B
sigma_D_B = ModifiedRodriguesParameters( np.array([[0.1, 0.2, 0.3]]) )

# express orientation of body as DCM
body_dcm = sigma_D_B.to_direction_cosine_matrix()

