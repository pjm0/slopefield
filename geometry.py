from math import pi, atan2, sin, cos

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
    if angle1 == None:
        return angle2
    elif angle2 == None:
        return angle1
    else:
        theta = angle1 + angle2
        while theta < -pi:
            theta += 2 * pi
        while theta >= pi:
            theta -= 2 * pi
        return theta

def add_angles_2(angle1, mag1, angle2, mag2):
    return vector_to_angle(add_vectors(scale_vector(angle_to_vector(angle1), mag1),
                                       scale_vector(angle_to_vector(angle2), mag2)))

def add_vectors(vector1, vector2):
    x1, y1 = vector1
    x2, y2 = vector2
    return (x1 + x2, y1 + y2)

def angle_to_vector(angle):
    return (cos(angle), sin(angle))

def vector_to_angle(vector):
    return atan2(vector[1], vector[0])

def scale_vector(vector, scale):
    return tuple(scale * n for n in vector)
#PI = pi
