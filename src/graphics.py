import framebuf
import machine

# Initialize Display (Modify this for your display type)
i2c = machine.I2C(0, scl=machine.Pin(22), sda=machine.Pin(21))
display = None  # Replace with actual display driver, e.g., SSD1306

WIDTH = 320
HEIGHT = 240

# Create a framebuffer (1-bit monochrome)
buffer = bytearray(WIDTH * HEIGHT // 8)
fb = framebuf.FrameBuffer(buffer, WIDTH, HEIGHT, framebuf.MONO_HLSB)

def init_screen():
    """Initialize the display."""
    if display:
        display.fill(0)
        display.show()

def draw_pixel(x, y, color):
    """Draw a pixel using framebuffer and refresh the display in bulk."""
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        fb.pixel(x, y, color)
    
def update_display():
    """Push framebuffer to display (faster than drawing pixels one by one)."""
    if display:
        display.blit(fb, 0, 0)
        display.show()

def clear_screen():
    """Clear the screen by setting all pixels to black."""
    for y in range(HEIGHT):
        for x in range(WIDTH):
            draw_pixel(x, y, 0)
    update_display()
