from main import *

d = 10
#xf, yf, zf
F = [ 1, 1, 1 ]
#a1, a2
a = [ 5, 10 ]
#xa, ya, za
A = [ -10, 0, 0 ]
#xb, yb, zb
B = [ 0, -10, 0 ]
#xc, yc, zc
C = [ 10, 0, 0 ]

for i in range(-18, 18):
    init( A, B, C , F, a, d, i)

