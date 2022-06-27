from differentiate import differentiate
import sympy
from functools import cache

@cache
def nrMethod(polynomial : str, points : int = 2, offset : int = 0, increment : int = 1, threshold : int = 0.03) -> list[str]:
    """
    newton raphson method\n
    don't worry about sanitizing the input, the function sanitizes it for you\n
    estimates the root of a polynomial using points points on a 2d graph with intervals of increment starting from offset units away from origin\n
    offset is the amount of units away from the origin to start placing down points at intervals e.g. if offset is 4, points will start 4 units away from origin\n
    increment states the spacing/distance between each point e.g. if increment is 0.3, each point will be 0.3 units apart\n 
    threshold is the margin of error allowed from y=0
    """
    if points < 1:
        raise Exception("Must have at least one point!")
    fprime = differentiate(polynomial)
    x = sympy.Symbol("x")
    polynomial = "*x".join(polynomial.split("x"))
    fprime = "*x".join(fprime.split("x"))
    f = sympy.sympify(polynomial.replace("^", "**"))
    fprime = sympy.sympify(fprime.replace("^", "**"))
    f = sympy.lambdify(x, f)
    fprime = sympy.lambdify(x, fprime)
    deriv = 1
    prev = 0
    roots = []
    higher = offset 
    lower = -higher
    value = offset
    pointlist = [-value, value]
    flag = 1
    for i in range(points-2):
        value += increment
        flag = -1 if flag else 1
        pointlist.append(flag * value)
            
    while pointlist:
        dellist = []
        
        for i in range(len(pointlist)):
            pointlist[i] -= (f(pointlist[i])/fprime(pointlist[i]))
            if f(pointlist[i]) < threshold:
                roots.append(pointlist[i])
                dellist.append(i)
        dellist.sort(reverse=True)
        for i in dellist:
            del pointlist[i]
            
    return set(roots) 
