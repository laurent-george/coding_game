import sys
import numpy as np


def norm(x, y):
    return np.sqrt(x * x + y * y)


def compute_distance(u, v):
    return norm(abs(u[0] - v[0]), abs(u[1] - v[1]))


class Vehicle:
    def __init__(self, mass=0.5, radius=400, friction=0.2):
        self.mass = mass
        self.friction = friction
        self.radius = radius
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.goal_pos = [0, 0]
        self.goal_radius = 0

    def update(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        print("pour info ma vitesse", vx, vy, file=sys.stderr)

    def update_goal(self, x, y, radius=0):
        self.goal_pos = [x, y]
        self.goal_radius = radius

    def command(self):
        if (compute_distance([self.goal_pos[0], self.goal_pos[1]], [self.x, self.y]) < 3*self.radius
        and norm(self.vx, self.vy)) >300:
            x_cmd = self.x - self.vx
            y_cmd = self.y - self.vy
            power = min(300,norm(self.vx, self.vy)/2)
            
        elif compute_distance([self.goal_pos[0], self.goal_pos[1]], [self.x, self.y]) < self.radius:
            x_cmd = self.x - self.vx
            y_cmd = self.y - self.vy
            power = min(300,norm(self.vx, self.vy))
            
        else:
            v_cmd = [self.goal_pos[0] - self.x - self.vx * (1 - self.friction),
                    self.goal_pos[1] - self.y - self.vy * (1 - self.friction)]

            x_cmd = self.x + v_cmd[0]
            y_cmd = self.y + v_cmd[1]
            power = 300

        return str(round(x_cmd)) + " " + str(round(y_cmd)) + " " + "300"


    def get_pos(self):
        return [self.x, self.y]


class Reaper(Vehicle):
    def __init__(self):
        super().__init__()


class


def parse_input(my_reaper):
    all_units = [[] for i in range(5)]

    my_score = int(input())
    enemy_score_1 = int(input())
    enemy_score_2 = int(input())
    my_rage = int(input())
    enemy_rage_1 = int(input())
    enemy_rage_2 = int(input())
    unit_count = int(input())

    for i in range(unit_count):
        unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, extra_2 = input().split()
        unit_id = int(unit_id)
        unit_type = int(unit_type)
        player = int(player)
        mass = float(mass)
        radius = int(radius)
        x = int(x)
        y = int(y)
        vx = int(vx)
        vy = int(vy)
        extra = int(extra)
        extra_2 = int(extra_2)

        all_units[unit_type] += [
            {"unit_id": unit_id, "unit_type": unit_type, "player": player, "mass": mass, "radius": radius, "x": x,
             "y": y, "vx": vx, "vy": vy, "extra": extra, "extra_2": extra_2}]

        if (player == 0 and unit_type == 0):
            my_reaper.update(x, y, vx, vy)

    return all_units


def get_closest_wreck(my_reaper, all_units):
    my_pos = my_reaper.get_pos()
    distance = -1
    closest_wreck = {"x": 0, "y": 0, "radius": 0}
    for wreck in all_units[4]:
        wreck_pos = [wreck["x"], wreck["y"]]
        tmp_dis = compute_distance(my_pos, wreck_pos)
        if distance == -1 or tmp_dis < distance:
            closest_wreck = wreck
    return closest_wreck


# game loop
while True:
    my_reaper = Reaper()

    all_units = parse_input(my_reaper)

    closest_wreck = get_closest_wreck(my_reaper, all_units)

    my_reaper.update_goal(closest_wreck["x"], closest_wreck["y"], closest_wreck["radius"])

    print(my_reaper.command())
    print(my_reaper.command(), file=sys.stderr)
    print("WAIT")
    print("WAIT")


























