#!/usr/bin/env python
# -*- coding: utf-8 -*-

class EulerParameters:
    """
    Euler Parameters, a.k.a. quaternions, are defined by a four element vector
    β where:
        β0 = cos(φ/2)
        β1 = e1 sin(φ/2)
        β2 = e2 sin(φ/2)
        β3 = e3 sin(φ/2)

    β0^2 + β1^2 + β2^2 + β3^2 = 1

    Describes a four-dimensional unit shpere. Each attitude has two sets of EPs
    which describe that attitude. (e, φ) and (-e, -φ) are the same.
    """

    def __init__(self, beta):
        self.beta = beta

    def to_dcm(self):
        """
        [C] = [
            β0^2+β1^2-β2^2-β3^2, 2(β1β2+β0β3),        2(β1β3-β0β2)
            2(β1β2-β0β3),        β0^2-β1^2+β2^2-β3^2, 2(β2β3+β0β1)
            2(β1β3+β0β2),        2(β2β3-β0β1),        β0^2-β1^2-β2^2+β3^2
            ]
        """
        # make things a bit more legible
        b0 = self.beta[0]
        b1 = self.beta[1]
        b2 = self.beta[2]
        b3 = self.beta[3]

        b0_sq = b0^2
        b1_sq = b1^2
        b2_sq = b2^2
        b3_sq = b3^2

        c = np.matrix((
            ( (b0_sq + b1_sq - b2_sq - b3_sq), 2 * (b1 * b2 + b0 * b3), 2 * (b1 * b3 - b0 * b2) ),
            ( 2 * (b1 * b2 - b0 * b3), (b0_sq - b1_sq + b2_sq - b3_sq), 2 * (b2 * b3 + b0 * b1) ),
            ( 2 * (b1 * b3 + b0 * b2), 2 * (b2 * b3 - b0 * b1), (b0_sq - b1_sq - b2_sq + b3_sq) )
        ))

        return c
