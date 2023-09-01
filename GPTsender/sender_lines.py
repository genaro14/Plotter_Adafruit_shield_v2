import serial
import time

def send_command_with_confirmation(ser, command):
    ser.write(command.encode() + b'\n')
    response = ser.readline().decode().strip()
    return response

# Serial port configuration
ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)

try:
    if ser.is_open:
        print("Serial port is open. Waiting...")
        time.sleep(2)  # Wait for 2 seconds

        expected_lines = 5  # Number of lines to wait for
        received_lines = 0
        responses = []  # List to store responses

        # Wait for the expected number of lines
        while received_lines < expected_lines:
            connection_response = ser.readline().decode().strip()
            print("Connection Response:", connection_response)
            responses.append(connection_response)
            received_lines += 1

        time.sleep(2)  # Wait for 2 seconds before sending commands

        # Open the G-code file
        with open('test.gcode', 'r') as gcode_file:
            commands = gcode_file.readlines()

        for command in commands:
            command = command.strip()
            response = send_command_with_confirmation(ser, command)
            print(f"Sent: {command}\nReceived: {response}\n")
            responses.append(response)
            while not response:  # Wait if the response is empty
                response = send_command_with_confirmation(ser, command)
                time.sleep(1)  # Wait for 1 second
            if response != 'ok':
                print("Error: Did not receive 'ok' confirmation. Stopping.")
                break

        # Print all responses
        print("\nAll Responses:")
        for i, response in enumerate(responses, start=1):
            print(f"{i}. {response}")

    else:
        print("Serial port is not open.")

except serial.SerialException as e:
    print("Serial communication error:", e)

finally:
    ser.close()
