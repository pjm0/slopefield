def avoid_border(point):
    border_dist = 100 # Go no closer than this to the outer borders    
    self_x = point[0]
    self_y = point[1]

    if (self_x < border_dist): # Too close to left side
        #printf("Too close to left side")
        if (self_y < border_dist): # Too close to top and left
           return pi/4 # Head down/right
        elif (self_y > 768 - border_dist): # Too close to bottom
           return -pi/4 # Head up/right
        return 0 # Head right
    elif (self_x > 1024 - border_dist): # Too close to right side
        #printf("Too close to right side")
        if (self_y < border_dist): # Too close to top and right
           return pi * 0.75 # Head down/left
        elif (self_y > 768 - border_dist): # Too close to bottom and right
           return -pi * 0.75 # Head up/left
        return pi # Head left
    else: # X value ok
       if (self_y < border_dist): # Too close to top
           #printf("Too close to top side")
           return pi/2 # Head down
       elif (self_y > 768 - border_dist): # Too close to bottom
           #printf("Too close to bottom side")
           return -pi/2 # Head up
