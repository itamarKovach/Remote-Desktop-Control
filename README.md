# Remote Desktop Control

This project is a simple remote desktop control system, similar to the RDP (Remote Desktop Protocol). It consists of two Python applications:

1. **Technician Program**: The technician uses this application to remotely control and assist the grandma by sending keyboard and mouse inputs to her computer.
2. **Grandma Program**: The grandma uses this application on her computer, which receives the technician's inputs and sends back a live stream of her screen at 30 frames per second (FPS).

Both programs utilize **Tkinter** for displaying the screen and handling real-time inputs in a graphical interface.

## Features

- **Keyboard Control**: The technician's keyboard presses (e.g., typing 'w') are mirrored on the grandma's computer.
- **Mouse Control**: The technician's mouse movement is transmitted to the grandma's computer, allowing them to move her mouse pointer.
- **Screen Sharing**: The grandma's screen is sent to the technician at 30 FPS so they can view what’s happening on her computer and assist with troubleshooting.
- **GUI Display**: Both the technician and grandma programs use `Tkinter` for creating a window that shows the grandma’s screen and the technician's live inputs (mouse and keyboard) in real-time.

## Requirements

- Python 3.x
- Required Python packages:
  - `pynput` (for controlling mouse and keyboard)
  - `Pillow` (for capturing screenshots, imported via `PIL` namespace)
  - `socket` (for communication)
  - `threading` (for multi-threaded handling)
  - `tkinter` (for creating the graphical user interface)

You can install the required dependencies by running:

```bash
pip install pynput Pillow
