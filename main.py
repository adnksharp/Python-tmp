from numpy import pi as pi
import numpy as np
from Base.Basic import *
from Base.funciones import *
from Base.tB import *

def init(A, B, C, F, a, d, g):
    H = getSqrt( F, A, B, C )
    Angle = getHabc( F, A, B, C, d )
    """
        ta, ra, aa
        sb, gb, rb
        tc, ec, trc
    """
    tst = getTrasG( a, H, d )
    Q = [
        [tst[0][0] + tst[0][1], pi - tst[0][2]],
        [tst[1][0] + tst[1][1], pi - tst[1][2]],
        [tst[2][0] + tst[2][1], pi - tst[2][2]],
    ]
    B = [
        pi - (tst[0][2] + tst[0][0]),
        pi - (tst[0][1] + (pi/2)),
        pi - (tst[1][1] + (pi/2)),
        pi - (tst[1][2] + tst[1][0])
    ]
    B.append( sum(B) )

    if F[1] < 0:
        Angle[0] = -Angle[0]
        Angle[1] = -Angle[1]
    if F[0] < 0:
        Angle[2] = -Angle[2]

    Af = [
        Rz(pi) @ Tx(d) @ Rz(pi) @ Rz (Angle[0]),
        Ry(-Q[0][0]) @ Tx(a[0]),
        Ry(Q[0][1]) @ Tx(a[1])
    ]
    Af.append( Af[0] @ Af[1] @ Af[2] )

    Bf = [
        Rz(-pi / 2) @ Tx(d) @ Rz(pi),
        Rz(-Angle[1]),
        Ry(-Q[1][0]) @ Tx(a[0]),
        Ry(Q[1][1]) @ Tx(a[1])
    ]
    Bf.append( Bf[0] @ Bf[1] @ Bf[2] @ Bf[3] )

    Cf = [
        Tx(d) @ Rz(pi),
        Rz(-Angle[2]),
        Ry(-Q[2][0]) @ Tx(a[0]),
        Ry(Q[2][1]) @ Tx(a[1])
    ]
    Cf.append( Cf[0] @ Cf[1] @ Cf[2] @ Cf[3] )

    P = np.array([0, 0, 0, 1])
    P1a = Af[0] @ P 
    P2a = Af[0] @ Af[1] @ P
    P3a = Af[0] @ Af[1] @ Af[2] @ P 
    P1b = Bf[0] @ P
    P2b = Bf[0] @ Bf[1] @ P
    P3b = Bf[0] @ Bf[1] @ Bf[2] @ P
    P4b = Bf[0] @ Bf[1] @ Bf[2] @ Bf[3] @ P
    P1c = Cf[0] @ P
    P2c = Cf[0] @ Cf[1] @ P
    P3c = Cf[0] @ Cf[1] @ Cf[2] @ P
    P4c = Cf[0] @ Cf[1] @ Cf[2] @ Cf[3] @ P

    print( "H: ", H, "\nAngulos: ", Angle, "\nTa, Ra...: ", tst, "\nQ: ", Q )

    print( "A: ", P1a, P2a, P3a )
    print( "B: ", P1b, P2b, P3b, P4b )
    print( "C: ", P1c, P2c, P3c, P4c )

    Figure(P, P1a, P2a, P3a, P1b, P2b, P3b, P4b, P1c, P2c, P3c, P4c, a, g)
