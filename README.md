<div align="center">
  <h1>CSE423: COMPUTER GRAPHICS</h1>
  <p><strong>Semester:</strong> Summer 2024</p>
  <p>OpenGL-based lab assignments implemented in Python, covering foundational graphics primitives and interactive 2D games.</p>
  <p>
    <img alt="Python" src="https://img.shields.io/badge/Python-3.x-1f425f?style=flat-square">
    <img alt="OpenGL" src="https://img.shields.io/badge/OpenGL-PyOpenGL-5586A4?style=flat-square">
    <img alt="GLUT" src="https://img.shields.io/badge/GLUT-Interactive-2E7D32?style=flat-square">
  </p>
</div>

---

## Overview
- This repository contains three lab assignments focused on rasterization, input handling, and simple game loops.
- The work uses classic OpenGL concepts (points, lines, midpoint algorithms) with GLUT for real-time interaction.
- Lab reports and raw code PDFs are archived in `LabReports`.

---

## Lab Highlights
### LAB-1
- Task 1: House in the Rain
  - Draws a house scene with dynamic rain.
  - Controls: `a` (night to day), `f` (day to night), arrow keys (rain direction), `r` (reset).
- Task 2: Random Shooter Balls
  - Spawns points with randomized motion and colors.
  - Controls: Right click (spawn), left click (blink toggle), arrow up/down (speed), space (pause/resume), `r` (reset).

### LAB-2
- Catch the Diamonds
  - Move the plate to catch falling diamonds with a running score and speed scaling.
  - Controls: Arrow keys (move plate), on-screen buttons for pause, restart, and exit.

### LAB-3
- Bubble Shooter
  - Shoot bubbles while avoiding missed shots and collisions.
  - Controls: `a`/`d` (move), space (shoot), on-screen buttons for pause, restart, and exit.

---

## Project Structure
```
LAB/
├─ LAB-1/
│  ├─ My_task1.py
│  ├─ My_task2.py
│  └─ OpenGL.zip
├─ LAB-2/
│  ├─ LAB-2.py
│  ├─ 421-Lab-2.pdf
│  └─ catch_the_diamonds_gameplay.mp4
├─ LAB-3/
│  ├─ LAB-3.py
│  └─ Assignment 3.docx
└─ LabReports/
   ├─ Lab-1/
   ├─ Lab-2/
   └─ Lab-3/
```

---

## Requirements
- Python 3.x
- PyOpenGL and GLUT bindings (platform-specific setup may be needed)

---

## Run Locally
From the repository root:
```bash
python LAB-1/My_task1.py
python LAB-1/My_task2.py
python LAB-2/LAB-2.py
python LAB-3/LAB-3.py
```

---

## Notes
- This repository focuses on lab exercises; reports and raw PDFs are included for reference.
- There was no project in our semester.
