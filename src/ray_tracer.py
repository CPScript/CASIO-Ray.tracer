import math
import fast

WIDTH = 320
HEIGHT = 240
SPHERE_POS = (160, 120, 50)  
LIGHT_POS = (100, 50)  

def ray_trace(draw_pixel, update_display):
    """Core ray tracing loop, optimized with integer math and fast shading."""
    for y in range(HEIGHT):
        for x in range(WIDTH):
            dx = x - SPHERE_POS[0]
            dy = y - SPHERE_POS[1]
            
            if dx**2 + dy**2 <= SPHERE_POS[2]**2:
                normal_x = dx / SPHERE_POS[2]
                normal_y = dy / SPHERE_POS[2]

                light_x = LIGHT_POS[0] - x
                light_y = LIGHT_POS[1] - y
                light_len = math.sqrt(light_x**2 + light_y**2)
                
                if light_len > 0:
                    light_x /= light_len
                    light_y /= light_len

                color = fast.fast_shade(normal_x, normal_y, light_x, light_y)  # Call optimized C function
                draw_pixel(x, y, color)
    
    update_display()
