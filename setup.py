import os
import sys

def install_module(module_name):
    try:
        import upip
        print(f"Installing {module_name}...")
        upip.install(module_name)
    except Exception as e:
        print(f"Error installing {module_name}: {e}")

required_modules = [
    'ssd1306',  # For OLED display (adjust if you use a different display)
    'machine',  # For hardware control (GPIO, I2C, etc.)
    'math',  # For mathematical functions used in ray tracing
    'time',  # For time-related functions (sleep)
]

def setup():
    print("Setting up...")
    for module in required_modules:
        install_module(module)

if __name__ == '__main__':
    setup()
