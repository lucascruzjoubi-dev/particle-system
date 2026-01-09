import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from vector import Vector2   

plt.close('all')

num_particles = 30
arrow_scale = 0.3
dt = 0.1

position = Vector2(0, 0)
velocity = Vector2(2, 5)
acceleration = Vector2(0, -0.2)
gravity = Vector2(0, -9.8)


x_vals = []
y_vals = []



for _ in range(100):
    velocity = velocity + acceleration
    position = position + velocity
    x_vals.append(position.x)
    y_vals.append(position.y)
    


particles = []

for _ in range(100):
    position = Vector2(0, 0)
    velocity = Vector2(
        random.uniform(-3, 3),
        random.uniform(2, 6)
    )
    particles.append((position, velocity))



paths_x = [[] for _ in particles]
paths_y = [[] for _ in  particles]

for _ in range(60):
    for i in range(len(particles)):
        position, velocity = particles[i]
        velocity = velocity + gravity
        position = position + velocity
        particles[i] = (position, velocity)

        paths_x[i].append(position.x)
        paths_y[i].append(position.y)


for i in range(len(paths_x)):
    plt.plot(paths_x[i], paths_y[i], alpha=0.5)

x_vals = [p[0].x for p in particles]
y_vals = [p[0].y for p in particles]




def new_paricle():
    return{
        "pos": Vector2(0, 40),
        "vel": Vector2(random.uniform(-3, 3), random.uniform(4, 8)),
        "life": random.uniform(2, 4)
    }


particles = [new_paricle() for _ in range(num_particles)]

0
fig, ax = plt.subplots()


x0 = [0] * num_particles
y0 = [0] * num_particles
u0 = [0] * num_particles
v0 = [0] * num_particles

scat = ax.scatter(x0, y0)
quiver = ax.quiver(x0, y0, u0, v0, angles='xy', scale_units='xy', scale=1)




ax.set_xlim(-30, 30)
ax.set_ylim(-10, 50)
ax.grid()


def update(frame):
    x, y = [], []
    u, v = [], []


    for i, p in enumerate(particles):
        
        p["life"] -= dt

        if p["life"] <= 0:
            particles[i] = new_paricle()
            p = particles[i]


        p["vel"] = p["vel"] + gravity * dt
        p["pos"] = p["pos"] + p["vel"] * dt


        x.append(p["pos"].x)
        y.append(p["pos"].y)
        u.append(p["vel"].x * arrow_scale)
        v.append(p["vel"].y * arrow_scale)
    

    scat.set_offsets(list(zip(x, y)))
    quiver.set_offsets(list(zip(x, y)))
    quiver.set_UVC(u, v)

    return scat, quiver



ani = FuncAnimation(fig, update, frames=100, interval=50)
plt.show()


plt.grid()
plt.iof()
plt.show()
