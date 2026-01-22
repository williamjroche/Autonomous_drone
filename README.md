# Autonomous Drone

This is a GPS-Denied **Autonomous Drone** project that uses **computer vision** for flight with a **radio-transmission override**.  
The repository contains two main subsystems:

- **Flight Controller**
- **Flight Computer**

This is an **ongoing project**, and the flight controller is still in development. A prototype flight controller can be seen in the photo on the bottom. A more refined PCB implementation of this flight controller is in the works, named **'Atlas Flight Controller'**. This board uses the rp2350A microcontroller from Raspberry Pi, micro-usb power and data, ICM-20948 IMU chip (9-axis), 16MB flash memory (W25Q128JVS), an automatic power switching circuit for use with both external power and micro-usb power. This board will be powered by 5v input (from PDB) during flight which has voltage regulators for smooth and stable power delivery. 

## Flight Controller
- Software:
  - Connects to the IMU and adjusts motor speed for flight stability using PID control  
  - Implements PID control (a feedback control system that continuously adjusts an output to reach a target value)  
  - Runs the main motor-control software  
  - Includes a custom transmitter/receiver interface program
- ATLAS Flight Controller v0.4:

<p align='center'>
  <img width="898" height="811" alt="atlas_flight_controller_pcb_3dview_v0 4" src="https://github.com/user-attachments/assets/9087c51c-edc1-4f96-96cb-7165504e71e9" />
</p>

This board uses the **RP2350A** microcontroller from Raspberry Pi, micro-usb power and data, **ICM-20948 IMU** chip (9-axis), 16MB flash memory (W25Q128JVS), an automatic power switching circuit for use with both external power and micro-usb power. This board will be powered by 5v input (from PDB) during flight which has voltage regulators for smooth and stable power delivery. This board is still in development and has not been tested yet. The current design sports a **4-layer** design, with the top and bottom for routing, second layer for GND copper pour, and the third layer for a 3.3v copper pour.

## Flight Computer

- Uses **ROS2** to send commands to the flight controller based on computer-vision input  
- Contains main computer-vision software  
- Interfaces directly with the onboard camera  

## Dual Power Supply PCB

- Provides regulated power for sensors and radio receiver
- Uses **PDB 12V pins** as input
- Includes both **5V and 3.3V outputs** for versatility  
- **KiCad files included** for open access  
- **Gerber, BOM, and Pick-and-Place files** included for quick ordering  
  - *Update: I was was using JLCPCB, but my PCB order never arrived so I am now using PCBway, ETA: Feburary 14th*

## Drone Frame

- Modified STL files sourced online and optimized for **3D printing in PLA**  
- All screw holes intended for **M3 screws** (not pre-threaded — use nuts)  
- Due to 3D-printer tolerances, some holes may require **M2 screws with nut and lock washer**  
- Ensure all screws are tightened **as much as possible** to avoid structural weakness  

## How to Use

*This repo is best used as a guide for building your own custom autonomous drone, as the implementation is specific to the materials used.*

-Materials: 3D printer, PLA filament, 4 BLDC motors (I'm using 920kv DJI), 3S lipo, 4 ESC's, 1 PDB (power distribution board), radio ELRS controller, radio ELRS to PWM receiver, Raspberry Pi 5, Raspberry Pi Pico, IMU board
- Upload all files in the **Flight Controller** folder to a **Raspberry Pi Pico** running the latest Micropython  
- Follow the GPIO mappings in `esc_control.py` and `controller_input.py`, or adjust as needed  
- Ensure BLDC motors adjacent to each other rotate in **opposite directions**
- Optional: order dual channel power distribution board for smooth and effecient power
- *Flight Computer instructions are still in progress*

My progress so far:


![drone](https://github.com/user-attachments/assets/f177758e-e5d2-44e2-8123-dc4d9e2fefe5)


*This is a work in progress*


MIT License
