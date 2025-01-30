import time
from src.graphics import draw_pixel
from src.ray_tracer import ray_trace

while True:
    ray_trace(draw_pixel)
    time.sleep(0.1)
