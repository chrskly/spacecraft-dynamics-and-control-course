#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def tilde(v):
    """
    [
        0 -x3  x2
       x3   0 -x1
      -x2  x1   0
    ]
    """
    return [ [ 0, -v[0][2], v[0][1] ],
             [ v[0][2], 0, -v[0][0] ],
             [ -v[0][1], v[0][0], 0 ]  ]
