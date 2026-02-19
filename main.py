from math import pi

# everything is in cm
GRAVITY = 980 #cm/s^2
DRAG_COEFFICIENT = 0.8
AIR_DENSITY = 0.001225 #g/cm^3

PARACHUTE_DIAMETER = 90 #cm
PARACHUTE_MASS = 34 + 46 #g
STARTING_HEIGHT = 1000 #cm

EPS = 0.1

class Parachute:
    def __init__(self):
        self.velocity = 0
        self.y = STARTING_HEIGHT

        self.reached_terminal = False
        self.elapsed = 0

    def step_physics(self, dt):
        self.elapsed += dt

        drag_force = DRAG_COEFFICIENT * AIR_DENSITY * (self.velocity ** 2) * (pi / 8) * (PARACHUTE_DIAMETER ** 2)
        weight_force = PARACHUTE_MASS * GRAVITY
        net_force = drag_force - weight_force

        if not self.reached_terminal and abs(net_force) < EPS: 
            self.reached_terminal = True
            print(f"[{self.elapsed:.2f} s] | [{(STARTING_HEIGHT - self.y)/100:.2f} m] | Velocidade terminal: {-self.velocity / 100:.2f} m/s")

        acceleration = net_force / PARACHUTE_MASS if not self.reached_terminal else 0

        self.velocity += acceleration * dt

        self.y += self.velocity * dt

        if self.y <= 0:
            print(f"[{self.elapsed:.2f} s] | [{(STARTING_HEIGHT - self.y)/100:.2f} m] | Paraquedas atingiu o chão")
            return True
        
        return False

def main():
    new_parachute = Parachute()
    hit_ground = False
    while not hit_ground:
        hit_ground = new_parachute.step_physics(0.001)

if __name__ == "__main__":
    main()
