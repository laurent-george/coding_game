


import sys
import math

import math
import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


TYPE_REAPER = 0
TYPE_WRECK = 4


def print_debug(s):
    print(s, file=sys.stderr)


def distance_euclid(x, y, dest_x, dest_y):
    dist = math.sqrt((x - dest_x) ** 2 + (y - dest_y) ** 2)
    return dist

class Vehicle(object):
    def __init__(self, id=None, radius=None, pos_x=None, pos_y=None, vx=None, vy=None, mass=None):
        self.update(id=id, radius=radius, pos_x=pos_x, pos_y=pos_y, vx=vx, vy=vy, mass=mass)

    def update(self, id=None, radius=None, pos_x=None, pos_y=None, vx=None, vy=None, mass=None):
        self.radius = radius
        self.id = id
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vx = vx
        self.vy = vy
        self.mass = mass
        self.friction = 0

    def move_to(self, dest_x, dest_y, radius=0):
        # marin formulae
        dist =  distance_euclid(self.pos_x, self.pos_y, dest_x, dest_y)
        if dist < radius:
            opposite_x = self.pos_x - self.vx
            opposite_y = self.pos_y - self.vy
            throttle = int(min(300, math.sqrt(self.vx**2 + self.vy**2)))
            print_debug("Breaking")
            return opposite_x, opposite_y, int(throttle)
        else:
            print_debug("Accelerating to destination")

            v_cmd = [dest_x - self.pos_x - self.vx * (1 - self.friction),
                     dest_y - self.pos_y - self.vy * (1 - self.friction)]

            x_cmd = self.pos_x + v_cmd[0]
            y_cmd = self.pos_y + v_cmd[1]
            power = 300
            #throttle = int(min(300, distance_euclid(self.pos_x, self.pos_y, dest_x, dest_y)))
            return x_cmd, y_cmd, int(power)



class Ripper(Vehicle):
    """
    Class for our own vehicles
    """
    def __init__(self, *args, **kwargs):
        super().__init__(kwargs)
        self.friction = 0.2

class Destroyer(Vehicle):
    def __init__(self, *args, **kwargs):
        super().__init__(kwargs)
        self.friction = 0.2

    def move_to(self, dest_x, dest_y, radius=0):
        



class Wrecks(object):
    def __init__(self, id=None, radius=None, pos_x=None, pos_y=None, extra=None):
        # TODO: add inheritance to avoid copy
        self.radius = radius
        self.id = id
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.extra = extra


class Game(object):
    def __init__(self):
        self.active_wrecks = {}
        self.my_rippers = {}
        self.ennemy_rippers = {}

        self.active_ids = []

    def update_state(self, unit_count=None):
        old_ids = self.active_ids

        # we recreate wrecks each time
        self.active_wrecks = {}

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

            self.active_ids.append(unit_id)

            if unit_type == TYPE_REAPER:
                print_debug("Updating ripper {}".format(unit_id))
                dict_obj = self.my_rippers if player == 0 else self.ennemy_rippers

                obj = dict_obj.get(unit_id)
                if obj is None:
                    obj = Ripper()
                    dict_obj[unit_id] = obj

                obj.update(id=unit_id, radius=radius, pos_x=x, pos_y=y, vx=vx, vy=vy, mass=mass)

            if unit_type == TYPE_WRECK:
                obj = Wrecks(id=unit_id, radius=radius, pos_x=x, pos_y=y)
                self.active_wrecks[unit_id] = obj

    def compute_cmd(self):
        for unit_id, ripper in self.my_rippers.items():
            print_debug("Getting move for {}".format(unit_id))
            wreck = self.find_best_destination(ripper)
            if wreck:
                x, y, throttle = ripper.move_to(wreck.pos_x, wreck.pos_y, radius=wreck.radius)
            else:
                x, y, throttle = ripper.move_to(0, 0, radius=3000)
            print("{} {} {}".format(x, y, throttle))
        print("Wait")
        print("Wait")

    def find_best_destination(self, ripper_obj):
        return self.closest_wreck(ripper_obj)

    def closest_wreck(self, moving_object):
        """
        return closest wreck to the id
        :param object: an object with field pos_x and field pos_y
        :return:
        """
        pos_x = moving_object.pos_x
        pos_y = moving_object.pos_y

        min_distance = None
        closest_wreck_object = None
        for wreck_id, wreck in self.active_wrecks.items():
            cur_dist = distance_euclid(pos_x, pos_y, wreck.pos_x, wreck.pos_y)
            if min_distance is None or cur_dist < min_distance:
                min_distance = cur_dist
                closest_wreck_object = wreck

        return closest_wreck_object


game = Game()

while True:
    my_score = int(input())
    enemy_score_1 = int(input())
    enemy_score_2 = int(input())
    my_rage = int(input())
    enemy_rage_1 = int(input())
    enemy_rage_2 = int(input())
    unit_count = int(input())

    game.update_state(unit_count)
    game.compute_cmd()

