import numpy as np

def getSqrt( F, A, B, C ):
    return [
        np.sqrt([(F[0] ** 2) + (F[1] ** 2) + (F[2] ** 2)]),
        np.sqrt([(np.absolute(F[0] - A[0]) ** 2) + (F[1] ** 2) + (F[2] ** 2)]),
        np.sqrt([(F[0] ** 2) + (np.absolute(F[1] - B[1]) ** 2) + (F[2] ** 2)]),
        np.sqrt([(np.absolute(F[0] - C[0]) ** 2) + (F[1] ** 2) + (F[2] ** 2)])
    ]

def getAngle ( h1, h2, h3, hf, d ):
    return [
        np.arccos((d**2 + h1**2 - hf**2) / (2 * d * h1)),
        np.arccos((d**2 + h2**2 - hf**2) / (2 * d * h2)),
        np.arccos((d**2 + h3**2 - hf**2) / (2 * d * h3))
    ]

def getHabc( F, A, B, C, d ):
    return getAngle( np.sqrt([(F[0] + A[0]) ** 2 + (F[1] - A[1]) ** 2]),
        np.sqrt([(F[0] - B[0]) ** 2 + (F[1] + B[1]) ** 2]),
        np.sqrt([(F[0] + C[0]) ** 2 + (F[1] - C[1]) ** 2]), 
        np.sqrt([F[0] ** 2 + F[1] ** 2]), d )

def getTrasG( a, H, d ):
    return [
        [
            np.arccos((a[0]**2 + H[1]**2 - a[1]**2) / (2 * H[1] * a[0])),
            np.arccos((d**2 + H[1]**2 - H[0]**2) / (2 * H[1] * d)),
            np.arccos((a[0]**2 + a[1]**2 - H[1]**2) / (2 * a[0] * a[1]))
        ],
        [
            np.arccos((a[0]**2 + H[2]**2 - a[1]**2) / (2 * H[2] * a[0])),
            np.arccos((d**2 + H[2]**2 - H[0]**2) / (2 * H[2] * d)),
            np.arccos((a[0]**2 + a[1]**2 - H[2]**2) / (2 * a[0] * a[1]))
        ],
        [
            np.arccos((a[0]**2 + H[3]**2 - a[1]**2) / (2 * H[3] * a[0])),
            np.arccos((d**2 + H[3]**2 - H[0]**2) / (2 * H[3] * d)),
            np.arccos((a[0]**2 + a[1]**2 - H[3]**2) / (2 * a[0] * a[1]))
        ]
    ]