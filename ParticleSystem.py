import math
import random
import time

v = (2, 3)
k = 5
dt = 0.01
t = 0
max_time = 5
ground_y = 0.0
restitution = 0.8
rest_threshold = 0.05



def add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])



def scale(v, k):
    return (v[0] * k, v[0])



def magnitude(v):
    return math.sqrt(v[0]**2 + v[1]**2)



def normalize(v):
    mag = magnitude(v)
    if mag == 0:
        return (0,0)
    return (v[0] / mag, v[1] / mag)



particle = {

    "position": (0.0, 0.0),
    "velocity": (5.0, 8.0),
    "acceleration": (0.0, -9.8)

}




def update(p, dt):
    p["velocity"] = add(p["velocity"], scale(p["acceleration"], dt))
    p["position"] = add(p["position"], scale(p["velocity"], dt))
    
    if p["position"][1] <= 0:   
        p["position"] = (p["position"][0], ground_y)

        vx, vy = p["velocity"]

        if abs(vy) < rest_threshold:
            p["velocity"] = (vx, ground_y   )
        else:
            p["velocity"] = (vx, -vy * restitution)
      





while particle["position"][1] >= 0 and t < max_time:
    update(particle, dt)
    t  += dt
    print(particle["position"])
    time.sleep(0.10)



particles = []

for _ in range(10):
    particles.append({

        "position": (0.0, 0.0),
        "velocity": (5.0, 10.0),
        "acceleration": (0.0, -9.8)


    })



for p in particles:
    update(p, dt)



def random_velocity(angle, speed):
    angle = random.uniform(0, math.pi)
    speed = random.uniform(5, 12)
    return scale((math.cos(angle), math.sin(angle), speed))




particles.append({

    "position": (0.0 , 0.0),
    "velocity": random_velocity(),
    "acceleration": (0.0, -9.8)

})




print(f"t={t:.1f}  pos={particle['position']}  vel={particle['velocity']}")


