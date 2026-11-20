# ESP32 Serial Data Logger

## Project Overview

This project demonstrates a serial telemetry ingestion
pipeline using an ESP32 microcontroller and Python 3.

The ESP32 generates simulated temperature readings every
two seconds using MicroPython. A Python script running on
a Windows PC receives these readings over USB serial,
validates the data, adds a timestamp and device ID, and
saves the results to a CSV file.

## System Architecture

ESP32 (MicroPython)
    |
    | USB Serial (115200 baud)
    v
Windows PC (Python 3 + PySerial)
    |
    v
logger.py
    |
    v
sensor_data.csv

## Requirements

- ESP32 running MicroPython
- Python 3.x
- PySerial library
- USB data cable
- Windows PC

## Installation

Install PySerial:

    python -m pip install pyserial

## Configuration

Open logger.py and configure the serial port:

    COM_PORT = "COM9"

Change this value if the ESP32 is assigned a different
COM port.

## Running the Logger

1. Connect the ESP32 to the PC via USB.
2. Ensure the ESP32 is running its MicroPython emitter.
3. Close Thonny or any other serial monitor.
4. Open a terminal in the project directory.
5. Run:

    python logger.py

6. Observe the incoming temperature readings.
7. Press Ctrl+C to stop data collection safely.

## CSV Output

The program automatically creates sensor_data.csv.

Each row contains:

- Timestamp: Local PC date and time
- Device_ID: Identifier of the ESP32
- Temperature_F: Simulated temperature in Fahrenheit

The CSV file is excluded from Git version control.

## Error Handling

The logger handles:

- Serial connection errors
- Invalid incoming data
- File I/O errors
- Keyboard interrupts (Ctrl+C)

The serial connection is automatically closed when
the application terminates.

## Version Control

This repository contains the PC-side Python logger
and its documentation.

The ESP32 MicroPython firmware and collected CSV
data are intentionally excluded.