

# Implementation of what was in the handout on 2x2 matrix inversion is needed.

# The reason is that Newton's method in two dimensions involves inverting a
# 2x2 Hessian.


def invert_2x2(a, b, c, d):
    det = (1 / (a*d-c*b))
    e = det * d
    f = det * -b
    g = det * -c
    h = det * a
    return e, f, g, h
