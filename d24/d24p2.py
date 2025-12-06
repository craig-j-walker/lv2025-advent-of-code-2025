from sympy import Matrix, linsolve, symbols
import numpy as np

def d24p2(hailstones):

    x,y,z,vx,vy,vz = symbols("x,y,z,vx,vy,vz")

    [x1,y1,z1,vx1,vy1,vz1] = hailstones[0]
    [x2,y2,z2,vx2,vy2,vz2] = hailstones[1]
    [x3,y3,z3,vx3,vy3,vz3] = hailstones[2]

    A = Matrix([[vy1-vy2, vx2-vx1, 0, y2-y1, x1-x2, 0],
                [vy2-vy3, vx3-vx2, 0, y3-y2, x2-x3, 0],
                [vy3-vy1, vx1-vx3, 0, y1-y3, x3-x1, 0],
                [0, vz1-vz2, vy2-vy1, 0, z2-z1, y1-y2],
                [0, vz2-vz3, vy3-vy2, 0, z3-z2, y2-y3],
                [0, vz3-vz1, vy1-vy3, 0, z1-z3, y3-y1],
                [vz2-vz1, 0, vx1-vx2, z1-z2, 0, x2-x1],
                [vz3-vz2, 0, vx2-vx3, z2-z3, 0, x3-x2],
                [vz1-vz3, 0, vx3-vx1, z3-z1, 0, x1-x3]])

    b = Matrix([y2*vx2+x1*vy1-y1*vx1-x2*vy2,
                y3*vx3+x2*vy2-y2*vx2-x3*vy3,
                y1*vx1+x3*vy3-y3*vx3-x1*vy1,
                z2*vy2+y1*vz1-z1*vy1-y2*vz2,
                z3*vy3+y2*vz2-z2*vy2-y3*vz3,
                z1*vy1+y3*vz3-z3*vy3-y1*vz1,
                x2*vz2+z1*vx1-x1*vz1-z2*vx2,
                x3*vz3+z2*vx2-x2*vz2-z3*vx3,
                x1*vz1+z3*vx3-x3*vz3-z1*vx1])

    X=linsolve((A,b),[x,y,z,vx,vy,vz])

    [x,y,z,vx,vy,vz] = next(iter(X))

    return [x,y,z,vx,vy,vz]
