# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
import math
import random

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

cardinal_points = [(-6000,0),(0,6000),(6000,0),(0,-6000)]

def dist(pos1, pos2):
    rep_dist = math.sqrt((pos2[0]-pos1[0])**2+(pos2[1]-pos1[1])**2)
#    print("Distance = "+str(rep_dist), file=sys.stderr)
    return rep_dist

def norm(pos1):
    return math.sqrt((pos1[0])**2+(pos1[1])**2)
   
# game loop
tab_coord_epave = []

rep_x = 0
rep_y = 0
acc = 300

my_position = (0,0)
my_speed = (0,0)
my_destroyer_position = (0,0)
my_doof_position = (0,0)

best_ennemi_position = (0,0)

position_bigger_tanker = (0,0)
best_ennemi = -1
best_ennemi_score = 0

current_cardinal_doof = 2

min_dist_reach_destination = 1000
max_range_grenade = 2000
diff_score_launch_grenade = 10

dist_to_acc_factor = 0.2

radius_factor_to_be_on_it = 1.5

dist_equal_to_one_water = 2000


def play_reaper(position_current_epave, my_position, my_speed, radius_current_epave):
    if dist(position_current_epave, my_position) < radius_current_epave:
        x_cmd = my_position[0] - my_speed[0]
        y_cmd = my_position[1] - my_speed[1]
        power = min(300,norm(my_speed))
   
    else:
        v_cmd = (position_current_epave[0] - my_position[0] - my_speed[0] * (1 - 0.2), position_current_epave[1] - my_position[1] - my_speed[1] * (1 - 0.2))
        x_cmd = my_position[0] + v_cmd[0]
        y_cmd = my_position[1] + v_cmd[1]
        power = 300
    print(str(int(x_cmd))+" "+str(int(y_cmd))+" " +str(int(power)))

def play_destroyer(my_rage, my_score, best_ennemi_score, best_ennemi_position, best_ennemi_speed, my_destroyer_position, position_bigger_tanker, acc = 300):
    if (my_rage > 280 or my_score < best_ennemi_score + diff_score_launch_grenade) and (my_rage > 60) and dist(best_ennemi_position, my_destroyer_position)<max_range_grenade:
        print("SKILL "+str(best_ennemi_position[0]+best_ennemi_speed[0])+ " "+ str(best_ennemi_position[1]+best_ennemi_speed[1]))
    else:
        print(str(position_bigger_tanker[0]) + " " + str(position_bigger_tanker[1])+ " " + str(acc))

def play_doof(acc = 300):
    global current_cardinal_doof
    if dist(my_doof_position,cardinal_points[current_cardinal_doof]) < min_dist_reach_destination:
        current_cardinal_doof = (current_cardinal_doof + 1)%len(cardinal_points)
    print(str(cardinal_points[current_cardinal_doof][0])+ " " + str(cardinal_points[current_cardinal_doof][1]) + " " + str(acc))

while True:
    my_score = int(input())
    enemy_score_1 = int(input())
    enemy_score_2 = int(input())
    if enemy_score_1 > enemy_score_2:
        best_ennemi = 1
        best_ennemi_score = enemy_score_1
    else:
        best_ennemi = 2
        best_ennemi_score = enemy_score_2
    my_rage = int(input())
    enemy_rage_1 = int(input())
    enemy_rage_2 = int(input())
    unit_count = int(input())
    dist_min = 12000
    bigger_water_tanker = -10
    bigger_water_epave = -10
   
    id_current_epave = -1
    position_current_epave = (0,0)
    dist_to_current_epave = 0
    radius_current_epave = 0

    dont_move = False
    for i in range(unit_count):
        unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, extra_2 = input().split()
        print(unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, extra_2, file=sys.stderr)
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
       
        if player == best_ennemi and unit_type == 0:
            best_ennemi_position = (x,y)
            best_ennemi_speed = (vx, vy)
       
        if player == 0 and unit_type == 0:
            my_position = (x,y)
            my_speed = (vx, vy)
           
        if player == 0 and unit_type == 1:
            my_destroyer_position = (x,y)

        if player == 0 and unit_type == 2:
            my_doof_position = (x,y)  
           
        if unit_type == 3:
            if (extra - int(dist(my_destroyer_position, (x,y))/dist_equal_to_one_water)) >= bigger_water_tanker:
                bigger_water_tanker = (extra - int(dist(my_destroyer_position, (x,y))/dist_equal_to_one_water))
                position_bigger_tanker = (x,y)
       
        if unit_type == 4:
            distance_to_epave = dist(my_position,(x,y))
            if radius * radius_factor_to_be_on_it > distance_to_epave:
                dont_move = True
                id_current_epave = unit_id
                position_current_epave = (x,y)
                radius_current_epave = radius
                dist_to_current_epave = distance_to_epave
               
            elif ((extra - int(distance_to_epave/dist_equal_to_one_water)) >= bigger_water_epave) and not dont_move:
                    bigger_water_epave = (extra - int(distance_to_epave/dist_equal_to_one_water))
                    id_current_epave = unit_id
                    position_current_epave = (x,y)
                    radius_current_epave = radius
                    dist_to_current_epave = distance_to_epave
               
        
    acc = min(300, int(dist_to_acc_factor*dist_to_current_epave))
    print("Distance = "+str(dist_to_current_epave), file=sys.stderr)
    print("Acc = "+str(acc), file=sys.stderr)
    dest_x = position_current_epave[0]
    dest_y = position_current_epave[1]
    print("dest_x = "+str(dest_x), file=sys.stderr)
    print("dest_y = "+str(dest_y), file=sys.stderr)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    play_reaper(position_current_epave, my_position, my_speed, radius_current_epave)

    play_destroyer(my_rage, my_score, best_ennemi_score, best_ennemi_position, best_ennemi_speed, my_destroyer_position, position_bigger_tanker)
    play_doof()
