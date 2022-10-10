import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def Figure(P, P1a, P2a, P3a, P1b, P2b, P3b, P4b, P1c, P2c, P3c, P4c, a):
    d3 = plt.figure()
    ax1 = plt.axes(projection='3d')
    ax1 = d3.add_subplot(111, projection='3d')

    ax1.plot([P1a[0],P2a[0]],[P1a[1],P2a[1]],[P1a[2],P2a[2]],color="purple", linewidth=1, linestyle="-")
    ax1.plot([P2a[0],P3a[0]],[P2a[1],P3a[1]],[P2a[2],P3a[2]],color="purple", linewidth=1, linestyle="-")
    ax1.plot([P3a[0]],[P3a[1]],[P3a[2]],color="purple", linewidth=1, linestyle="-")

    ax1.scatter([P[0],P1a[0]],[P[1],P1a[1]],[P[2],P1a[2]])
    ax1.scatter([P1a[0],P2a[0]],[P1a[1],P2a[1]],[P1a[2],P2a[2]])
    ax1.scatter([P2a[0],P3a[0]],[P2a[1],P3a[1]],[P2a[2],P3a[2]])
    ax1.scatter([P3a[0]],[P3a[1]],[P3a[2]])

    ax1.plot([P1b[0],P2b[0]],[P1b[1],P2b[1]],[P1b[2],P2b[2]],color="r", linewidth=1, linestyle="-")
    ax1.plot([P2b[0],P3b[0]],[P2b[1],P3b[1]],[P2b[2],P3b[2]],color="r", linewidth=1, linestyle="-")
    ax1.plot([P3b[0],P4b[0]],[P3b[1],P4b[1]],[P3b[2],P4b[2]],color="r", linewidth=1, linestyle="-")

    ax1.scatter([P[0],P1b[0]],[P[1],P1b[1]],[P[2],P1b[2]])
    ax1.scatter([P1b[0],P2b[0]],[P1b[1],P2b[1]],[P1b[2],P2b[2]])
    ax1.scatter([P2b[0],P3b[0]],[P2b[1],P3b[1]],[P2b[2],P3b[2]])
    ax1.scatter([P3b[0],P4b[0]],[P3b[1],P4b[1]],[P3b[2],P4b[2]])

    ax1.plot([P1c[0],P2c[0]],[P1c[1],P2c[1]],[P1c[2],P2c[2]],color="b", linewidth=1, linestyle="-")
    ax1.plot([P2c[0],P3c[0]],[P2c[1],P3c[1]],[P2c[2],P3c[2]],color="b", linewidth=1, linestyle="-")
    ax1.plot([P3c[0],P4c[0]],[P3c[1],P4c[1]],[P3c[2],P4c[2]],color="b", linewidth=1, linestyle="-")

    ax1.scatter([P[0],P1c[0]],[P[1],P1c[1]],[P[2],P1c[2]])
    ax1.scatter([P1c[0],P2c[0]],[P1c[1],P2c[1]],[P1c[2],P2c[2]])
    ax1.scatter([P2c[0],P3c[0]],[P2c[1],P3c[1]],[P2c[2],P3c[2]])
    ax1.scatter([P3c[0],P4c[0]],[P3c[1],P4c[1]],[P3c[2],P4c[2]])

    ax1.set_title('Robot 3/2')
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.set_zlabel("z")
    ax1.set_xlim3d(-(a[ 0 ] + a[ 1 ]),(a[ 0 ] + a[ 1 ]))
    ax1.set_ylim3d(-(a[ 0 ] + a[ 1 ]),(a[ 0 ] + a[ 1 ]))
    ax1.set_zlim3d(-(0),(a[ 0 ] + a[ 1 ]))

    for angle in range(0, 360*4 + 1):
        angle_norm = (angle + 180) % 360 - 180

        elev = azim = roll = 0
        if angle <= 360:
            elev = angle_norm
        elif angle <= 360*2:
            azim = angle_norm
        elif angle <= 360*3:
            roll = angle_norm
        else:
            elev = azim = roll = angle_norm

        ax1.view_init(elev, azim, roll)

        plt.draw()
        plt.pause(.001)
