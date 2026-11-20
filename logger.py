import serial
import csv
import os
from datetime import datetime

# ==========================================
# CONFIGURATION
# ==========================================

COM_PORT = "COM9"
BAUD_RATE = 115200
CSV_FILENAME = "sensor_data.csv"
DEVICE_ID = "ESP32_Node_1"

# ==========================================
# SERIAL CONNECTION
# ==========================================

print(f"Connecting to ESP32 on {COM_PORT}...")

try:
    with serial.Serial(
        port=COM_PORT,
        baudrate=BAUD_RATE,
        timeout=1
    ) as ser:

        print("Serial connection established!")
        print("Waiting for temperature data...")
        print("Press Ctrl+C to stop.\n")

        # Check if CSV needs a header
        write_header = (
            not os.path.exists(CSV_FILENAME)
            or os.path.getsize(CSV_FILENAME) == 0
        )

        # Open CSV in append mode
        with open(
            CSV_FILENAME,
            mode="a",
            newline="",
            encoding="utf-8"
        ) as file:

            csv_writer = csv.writer(file)

            if write_header:
                csv_writer.writerow([
                    "Timestamp",
                    "Device_ID",
                    "Temperature_F"
                ])
                file.flush()

            # Continuously listen for incoming data
            while True:

                raw_data = ser.readline().decode(
                    "utf-8",
                    errors="ignore"
                ).strip()

                # Ignore empty lines
                if not raw_data:
                    continue

                # Validate incoming temperature
                try:
                    temperature = float(raw_data)
                except ValueError:
                    print(f"Ignored: {raw_data}")
                    continue

                # Generate PC timestamp
                current_time = datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )

                # Display reading
                print(
                    f"[{current_time}] "
                    f"{DEVICE_ID}: "
                    f"{temperature:.2f} F"
                )

                # Write reading to CSV
                csv_writer.writerow([
                    current_time,
                    DEVICE_ID,
                    temperature
                ])

                # Immediately save data
                file.flush()

# ==========================================
# ERROR HANDLING
# ==========================================

except serial.SerialException as e:
    print(f"\nSERIAL ERROR: {e}")
    print("Check the COM port and USB connection.")
    print("Make sure Thonny is disconnected.")

except KeyboardInterrupt:
    print("\nData collection stopped by user.")

except OSError as e:
    print(f"\nFILE ERROR: {e}")

finally:
    print("Serial logger shutdown complete.")
