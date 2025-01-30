import time
from graphics import draw_pixel, update_display, clear_screen
from ray_tracer import ray_trace

clear_screen()

while True:
    ray_trace(draw_pixel, update_display)
    time.sleep(0.1)  # delay
