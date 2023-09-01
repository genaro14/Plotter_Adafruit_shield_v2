import serial
import time
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext

def send_command_with_confirmation(ser, command):
    ser.write(command.encode() + b'\n')
    response = ser.readline().decode().strip()
    return response

def start_script():
    try:
        port = port_entry.get()
        ser = serial.Serial(port, baudrate=9600, timeout=1)
        
        status_label.config(text="Serial port is open. Waiting...")
        root.update()
        time.sleep(2)

        expected_lines = 5
        received_lines = 0
        responses = []

        while received_lines < expected_lines:
            connection_response = ser.readline().decode().strip()
            status_label.config(text="Connection Response: " + connection_response)
            responses.append(connection_response)
            received_lines += 1

        time.sleep(2)

        gcode_filename = filedialog.askopenfilename(filetypes=[("G-code files", "*.gcode")])
        with open(gcode_filename, 'r') as gcode_file:
            commands = gcode_file.readlines()

        for i, command in enumerate(commands, start=1):
            command = command.strip()
            status_label.config(text=f"Sending command {i}/{len(commands)}: {command}")
            root.update()

            response = send_command_with_confirmation(ser, command)
            responses.append(response)
            responses_text.insert(tk.END, f"Sent: {command}\nReceived: {response}\n")

            while not response:
                response = send_command_with_confirmation(ser, command)
                time.sleep(1)
            if response != 'ok':
                status_label.config(text="Error: Did not receive 'ok' confirmation. Stopping.")
                break

        status_label.config(text="All commands processed.")

    except serial.SerialException as e:
        status_label.config(text="Serial communication error: " + str(e))

    finally:
        if ser.is_open:
            ser.close()

root = tk.Tk()
root.title("Serial Communication Script")

port_label = tk.Label(root, text="Enter Serial Port:")
port_label.pack()

default_port = "/dev/ttyACM0"
port_entry = tk.Entry(root)
port_entry.insert(0, default_port)
port_entry.pack()

start_button = tk.Button(root, text="Start Script", command=start_script)
start_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

responses_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
responses_text.pack()

root.mainloop()
