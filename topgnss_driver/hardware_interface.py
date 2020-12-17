import serial

good_data = '$GNGGA'

def position():
    with serial.Serial('/dev/ttyS0', baudrate=9600, timeout=1) as ser:
        while True:
            line = ser.readline().decode('ascii', errors='replace')
            if good_data in line:
                print(line.strip())
                return line.strip()

position()

