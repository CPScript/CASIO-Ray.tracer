> A lightweight ray tracer optimized for MicroPython-based Micro Controllers, featuring **fast pixel rendering**, **framebuffer optimizations**, and **C-accelerated shading calculations**.

## 🚀 Features

- **Framebuffer Rendering**: Faster pixel updates using `framebuf`
- **Optimized Shading**: Uses a **C module** for fast lighting calculations
- **Integer Math**: Reduces slow floating-point operations
- **ESP32/RP2040 Parallel Processing**: Can utilize multi-core rendering (optional)
- **Modular Structure**: Easily customizable for different displays and resolutions

---

## 🛠 Installation

### 1️⃣ Flash MicroPython
Ensure your board has **MicroPython** installed. If not, download it from:
[MicroPython Downloads](https://micropython.org/download/)

### 2️⃣ Install Required Modules
Upload the **setup script** and install dependencies:

```bash
mpremote fs cp setup.py :/setup.py
mpremote run setup.py
```

### 3️⃣ Upload Project Files
Transfer all required source files to your MicroPython device:
```bash
mpremote fs cp -r src :/src
mpremote fs cp -r modules :/modules
```

### 4️⃣ Compile C Module (Optional for Performance)
If using ESP32/RP2040, compile the C module for optimized shading:

```bash
mpy-cross modules/fast_raytrace.c
```
> Refer to MicroPython's `C module guide` for detailed instructions.

---

#### 📌 Usage

Run the ray tracer with:
```
import src.main
```

> Output: Will render a simple sphere with shading

--- 

#### 📂 Tree
```
/ray_tracer_project
│── /src
│   ├── graphics.py      # Handles pixel drawing & framebuffer
│   ├── ray_tracer.py    # Main ray tracing logic
│   ├── main.py          # Entry point of the program
│── /modules
│   ├── fast_raytrace.c  # C module for faster shading
│── setup.py             # Installs required modules
```

---

#### 🖥️ How It Works
### 📍 1. Graphics Engine

**graphics.py**:

-    Uses framebuf for efficient screen updates
-    Draws pixels via the display driver
-    Implements clear screen & refresh functions

### 🎮 2. Ray Tracing Algorithm

**ray_tracer.py**:

-    Traces rays to detect sphere intersections
-    Calculates shading intensity based on a light source
-    Uses the fast C module for improved performance

### ⚡ 3. Optimized Performance

-    Batch pixel updates reduce display lag
-    Precomputed math avoids redundant calculations
-    C acceleration speeds up shading operations

---

#### ⚡ Optimizations & Performance

Optimization | Benefit
---|---
Framebuffer (`framebuf`) | Fast pixel updates
C Module (`fast_raytrace.`c) | Accelerates shading calculations
Integer Math | Avoids slow floating-point operations
ESP32/RP2040 Parallelism | Uses multiple cores for rendering

---

#### 🔧 Customization

Modify the following parameters in `ray_tracer.py`:

-    Resolution (WIDTH, HEIGHT)
-    Sphere Position (SPHERE_POS)
-    Light Source (LIGHT_POS)
-    Color Intensity (`shade()` function in `fast_raytrace.c`)

---

> Built off of "https://github.com/CPScript/fx-CG50_RayTracer"
