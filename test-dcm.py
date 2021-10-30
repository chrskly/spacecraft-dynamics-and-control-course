#!/usr/bin/env python

import logging
from ea import EulerAngle
from dcm import directionCosineMatrix

logging.basicConfig(level=logging.DEBUG)

ea1 = EulerAngle("321", [10, 0, 20])
ea1.show()
dcm1 = ea1.to_direction_cosine_matrix()

print(dcm1.to_euler_angles())
