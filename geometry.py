from math import pi, atan2

def distance_to_line(point_1, point_2, point_3):
    """https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line#Line_defined_by_two_points https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line\
    """
    x_1, y_1 = point_1;
    x_2, y_2 = point_2;
    x_3, y_3 = point_3;
    return (abs(x_1 * (y_3 - y_2)
                - y_1 * (x_3 - x_2)
                + x_3 * y_2 - y_3 * x_2)
            / distance_to(point_2, point_3));


##for line in text.splitlines():
##    if "{" not in line and "}" not in line:
##        print(line.replace(";", "").replace("//", "#"))
##while True: pass        

def angle_to(point_1, point_2):
    return atan2(point_1[1] - point_2[1],
                 point_1[0] - point_2[0])

def distance_to(point_1, point_2):
    return ((point_1[0] - point_2[0])**2
            + (point_1[1] - point_2[1])**2)**.5

def add_angles(angle1, angle2):
    theta = angle1 + angle2
    while theta < -pi:
        theta += 2 * pi
    while theta >= pi:
        theta -= 2 * pi
    return theta
#PI = pi
