from numpy import exp, sin, pi

################################################################
def func1(t, p):
    (a1, b1, c1, d1) = p
    return (a1*exp(-b1*t)*sin(2*pi*c1*t+d1))

def residual1(p, y, t):
    return y-func1(t, p)

################################################################
def func2(t, p):
    (a1, b1, c1, d1,
     a2, b2, c2, d2) = p
    return (a1*exp(-b1*t)*sin(2*pi*c1*t+d1) +
            a2*exp(-b2*t)*sin(2*pi*c2*t+d2))

def residual2(p, y, t):
    return y-func2(t, p)

################################################################
def func3(t, p):
    (a1, b1, c1, d1,
     a2, b2, c2, d2,
     a3, b3, c3, d3) = p
    return (a1*exp(-b1*t)*sin(2*pi*c1*t+d1) +
            a2*exp(-b2*t)*sin(2*pi*c2*t+d2) +
            a3*exp(-b3*t)*sin(2*pi*c3*t+d3))

def residual3(p, y, t):
    return y-func3(t, p)

################################################################
def func4(t, p):
    (a1, b1, c1, d1,
     a2, b2, c2, d2,
     a3, b3, c3, d3,
     a4, b4, c4, d4) = p
    return (a1*exp(-b1*t)*sin(2*pi*c1*t+d1) +
            a2*exp(-b2*t)*sin(2*pi*c2*t+d2) +
            a3*exp(-b3*t)*sin(2*pi*c3*t+d3) +
            a4*exp(-b4*t)*sin(2*pi*c4*t+d4))

def residual4(p, y, t):
    return y-func4(t, p)

################################################################
def func5(t, p):
    (a1, b1, c1, d1,
     a2, b2, c2, d2,
     a3, b3, c3, d3,
     a4, b4, c4, d4,
     a5, b5, c5, d5) = p
    return (a1*exp(-b1*t)*sin(2*pi*c1*t+d1) +
            a2*exp(-b2*t)*sin(2*pi*c2*t+d2) +
            a3*exp(-b3*t)*sin(2*pi*c3*t+d3) +
            a4*exp(-b4*t)*sin(2*pi*c4*t+d4) +
            a5*exp(-b5*t)*sin(2*pi*c5*t+d5))

def residual5(p, y, t):
    return y-func5(t, p)

################################################################
def func6(t, p):
    (a1, b1, c1, d1,
     a2, b2, c2, d2,
     a3, b3, c3, d3,
     a4, b4, c4, d4,
     a5, b5, c5, d5,
     a6, b6, c6, d6) = p
    return (a1*exp(-b1*t)*sin(2*pi*c1*t+d1) +
            a2*exp(-b2*t)*sin(2*pi*c2*t+d2) +
            a3*exp(-b3*t)*sin(2*pi*c3*t+d3) +
            a4*exp(-b4*t)*sin(2*pi*c4*t+d4) +
            a5*exp(-b5*t)*sin(2*pi*c5*t+d5) +
            a6*exp(-b6*t)*sin(2*pi*c6*t+d6))

def residual6(p, y, t):
    return y-func6(t, p)

################################################################
def func7(t, p):
    (a1, b1, c1, d1,
     a2, b2, c2, d2,
     a3, b3, c3, d3,
     a4, b4, c4, d4,
     a5, b5, c5, d5,
     a6, b6, c6, d6,
     a7, b7, c7, d7) = p
    return (a1*exp(-b1*t)*sin(2*pi*c1*t+d1) +
            a2*exp(-b2*t)*sin(2*pi*c2*t+d2) +
            a3*exp(-b3*t)*sin(2*pi*c3*t+d3) +
            a4*exp(-b4*t)*sin(2*pi*c4*t+d4) +
            a5*exp(-b5*t)*sin(2*pi*c5*t+d5) +
            a6*exp(-b6*t)*sin(2*pi*c6*t+d6) +
            a7*exp(-b7*t)*sin(2*pi*c7*t+d7))

def residual7(p, y, t):
    return y-func7(t, p)

################################################################
def func8(t, p):
    (a1, b1, c1, d1,
     a2, b2, c2, d2,
     a3, b3, c3, d3,
     a4, b4, c4, d4,
     a5, b5, c5, d5,
     a6, b6, c6, d6,
     a7, b7, c7, d7,
     a8, b8, c8, d8) = p
    return (a1*exp(-b1*t)*sin(2*pi*c1*t+d1) +
            a2*exp(-b2*t)*sin(2*pi*c2*t+d2) +
            a3*exp(-b3*t)*sin(2*pi*c3*t+d3) +
            a4*exp(-b4*t)*sin(2*pi*c4*t+d4) +
            a5*exp(-b5*t)*sin(2*pi*c5*t+d5) +
            a6*exp(-b6*t)*sin(2*pi*c6*t+d6) +
            a7*exp(-b7*t)*sin(2*pi*c7*t+d7) +
            a8*exp(-b8*t)*sin(2*pi*c8*t+d8))

def residual8(p, y, t):
    return y-func8(t, p)

################################################################
def func9(t, p):
    (a1, b1, c1, d1,
     a2, b2, c2, d2,
     a3, b3, c3, d3,
     a4, b4, c4, d4,
     a5, b5, c5, d5,
     a6, b6, c6, d6,
     a7, b7, c7, d7,
     a8, b8, c8, d8,
     a9, b9, c9, d9) = p
    return (a1*exp(-b1*t)*sin(2*pi*c1*t+d1) +
            a2*exp(-b2*t)*sin(2*pi*c2*t+d2) +
            a3*exp(-b3*t)*sin(2*pi*c3*t+d3) +
            a4*exp(-b4*t)*sin(2*pi*c4*t+d4) +
            a5*exp(-b5*t)*sin(2*pi*c5*t+d5) +
            a6*exp(-b6*t)*sin(2*pi*c6*t+d6) +
            a7*exp(-b7*t)*sin(2*pi*c7*t+d7) +
            a8*exp(-b8*t)*sin(2*pi*c8*t+d8) +
            a9*exp(-b9*t)*sin(2*pi*c9*t+d9))

def residual9(p, y, t):
    return y-func9(t, p)

################################################################
def func10(t, p):
    (a1, b1, c1, d1,
     a2, b2, c2, d2,
     a3, b3, c3, d3,
     a4, b4, c4, d4,
     a5, b5, c5, d5,
     a6, b6, c6, d6,
     a7, b7, c7, d7,
     a8, b8, c8, d8,
     a9, b9, c9, d9,
     a10, b10, c10, d10) = p
    return (a1*exp(-b1*t)*sin(2*pi*c1*t+d1) +
            a2*exp(-b2*t)*sin(2*pi*c2*t+d2) +
            a3*exp(-b3*t)*sin(2*pi*c3*t+d3) +
            a4*exp(-b4*t)*sin(2*pi*c4*t+d4) +
            a5*exp(-b5*t)*sin(2*pi*c5*t+d5) +
            a6*exp(-b6*t)*sin(2*pi*c6*t+d6) +
            a7*exp(-b7*t)*sin(2*pi*c7*t+d7) +
            a8*exp(-b8*t)*sin(2*pi*c8*t+d8) +
            a9*exp(-b9*t)*sin(2*pi*c9*t+d9) +
            a10*exp(-b10*t)*sin(2*pi*c10*t+d10))

def residual10(p, y, t):
    return y-func10(t, p)

################################################################
def func11(t, p):
    (a1, b1, c1, d1,
     a2, b2, c2, d2,
     a3, b3, c3, d3,
     a4, b4, c4, d4,
     a5, b5, c5, d5,
     a6, b6, c6, d6,
     a7, b7, c7, d7,
     a8, b8, c8, d8,
     a9, b9, c9, d9,
     a10, b10, c10, d10,
     a11, b11, c11, d11) = p
    return (a1*exp(-b1*t)*sin(2*pi*c1*t+d1) +
            a2*exp(-b2*t)*sin(2*pi*c2*t+d2) +
            a3*exp(-b3*t)*sin(2*pi*c3*t+d3) +
            a4*exp(-b4*t)*sin(2*pi*c4*t+d4) +
            a5*exp(-b5*t)*sin(2*pi*c5*t+d5) +
            a6*exp(-b6*t)*sin(2*pi*c6*t+d6) +
            a7*exp(-b7*t)*sin(2*pi*c7*t+d7) +
            a8*exp(-b8*t)*sin(2*pi*c8*t+d8) +
            a9*exp(-b9*t)*sin(2*pi*c9*t+d9) +
            a10*exp(-b10*t)*sin(2*pi*c10*t+d10) +
            a11*exp(-b11*t)*sin(2*pi*c11*t+d11))

def residual11(p, y, t):
    return y-func11(t, p)

