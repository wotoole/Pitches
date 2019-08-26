'''
Liam O'Toole
pitchwithspin.py
model the flight of a baseball pitch with spin
9 October, 2014
''' 

#import libraries
from numpy import array
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import sin, cos, sqrt, pi, exp

#define value of done
done = 0

#define drag coefficient ala Giordano
def kD(v):
    delta = 5.0
    vd = 35.0
    return 0.0039 + 0.0058/(1.0 + exp((v-vd)/delta))

def euler(vx,vy,vz):
    x = 0
    y = 0
    z = input("Enter pitcher's release height: ")
    t = 0
    dt = 0.001
    kL = 4.1E-4
    omega = 1800    #rotation rate in rpm
    omega = omega*2*pi/60.0     #converts spin to rad/s

    while x <= 18.44:   #loop while ball is away from plate
        X.append(x)
        Y.append(y)
        Z.append(z)
        
        v = sqrt(vx**2 + vy**2 + vz**2)

        ax = -kD(v)*v*vx + kL*omega*(vz*sin(phi) - vy*cos(phi))
        ay = -kD(v)*v*vy + kL*omega*vx*cos(phi)
        az = -kD(v)*v*vz - kL*omega*vx*sin(phi) - g

        vx += ax*dt     #this means vx = vz + ax*dt
        vy += ay*dt
        vz += az*dt

        x += vx*dt
        y += vy*dt
        z += vz*dt

while not done:     #use a loop to get pitch type and more initial parameters
    X = []
    Y = []
    Z = []
    #need lists to get nice graph in 3D

    TYPE = raw_input("Type of pitch (Fastball[f]/Curveball[c]/Slider[s]/Screwball[w]: ")

    if TYPE == "f":
        v = 41.6
        phi = 80*pi/180.0
    elif TYPE == "c":
        v = 34.5              #pitch speed
        phi = 45*pi/180.0     #spin direction converted to rad
    elif TYPE == "s":
        v = 37.5
        phi = 90.0
    elif TYPE == "w":
        v = 34.5
        phi = 135*pi/180.0


    theta = 3.0*pi/180.0    #set throwing angle as 3 degrees above horizontal
    vx = v*cos(theta)
    vy = 0.0
    vz = v*sin(theta)
    g = 9.80665

    euler(vx,vy,vz)         #call euler to do calculations
    fig = plt.figure()
    Ax = Axes3D(fig)
    Ax.plot(X,Y,Z)              #plot trajectory of ball
    Ax.set_xlim3d(0,18.44)
    Ax.set_ylim3d(-1,1)
    Ax.set_zlim3d(0,2)
    Ax.plot_wireframe(array([[18.4,18.4], [18.4,18.4]]),array([[-0.22,0.22], [-0.22,0.22]]),array([[0.5,0.5],[1.1,1.1]]), color = 'r')
    plt.show()
    print "Y (ft) = ", Y[-1]
    print "Z (ft) = ", Z[-1]
    reply = raw_input("Pitch again? ")   #Get input to continue or end program
    if reply == 'n' or reply == 'N':
        print "Inning Over"
        done = 1



    

    

