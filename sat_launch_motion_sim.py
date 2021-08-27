import matplotlib.pyplot as plt 
import matplotlib.animation as animation 
import numpy as np 

h = float(input("Enter a desired height: "))

fig = plt.figure()
ax = plt.axes()

G = 6.674 * 10**(-11)
M = 5.972 * 10**24
R = 6378000

# plots the earth

a = np.arange(-0.1, 2*np.pi, 0.1)

x1 = R*np.cos(a)
y1 = R*np.sin(a)

ax.plot(x1,y1)

# create initial conditions

x = 0
y = R

v_x = ((2*G*M*(R+h))/(R*(h+(2*R))))**0.5
v_y = 0

a_x = 0
a_y = -1*G*M/(R**2)

v_f_init = -1*((2*G*M*R)/((R+h)*((2*R)+h)))**0.5
v_f_final = -1*((G*M)/(R+h))**0.5

b = True

scat = ax.scatter([0],[R], s=20)

def animate(i):
    ot = 1
    global G
    global M
    global x
    global y
    global v_x
    global v_y
    global a_x
    global a_y
    global v_f_final
    global v_f_init
    global b

    if(x<0 and b and v_x>v_f_final):
        v_x = v_x + 0.2*(v_f_final-v_f_init)
        v_y = 0
        b = False

    elif(x>0):
        b = True

    print((1-((x**2+y**2)**0.5/(R+h)))*100)

    x = x + (v_x * ot) + (0.5* a_x * (ot**2))
    y = y + (v_y * ot) + (0.5* a_y * (ot**2))
    v_x = v_x + (a_x * ot)
    v_y = v_y + (a_y * ot)
    a_x = -1*G*M*x/((x**2 + y**2)**1.5)
    a_y = -1*G*M*y/((x**2 + y**2)**1.5)
    scat.set_offsets([x,y])
    return(scat)

anim = animation.FuncAnimation(fig, animate, frames = 200000000, interval = 20)

ax.set_aspect('equal')
ax.set_xlim(-4*R,4*R)
ax.set_ylim(-4*R,4*R)

plt.show()
