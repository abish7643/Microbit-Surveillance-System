import serial.tools.list_ports
import serial

def getPort():
    ports = serial.tools.list_ports.comports()
    required_port = ''
    for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))
        if ("BBC" in desc or "micro:bit" in desc):
            print("Microbit Found On", port)
            required_port = port
    return required_port

microbit_port = getPort()
baud_rate = 115200

if microbit_port != '':
    try:
        serialPort = serial.Serial(port = microbit_port, baudrate=baud_rate,
                                   bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
        serialPort.flush()
    except:
        print("Couldn't Get Port")

    while(True):

        # Wait until there is data waiting in the serial buffer
        try:
            if(serialPort.in_waiting > 0):

                # Read data out of the buffer until a carraige return / new line is found
                serialString = serialPort.readline()
                if ((serialString.decode('Ascii')).strip() == "Pressed"):
                    print("Pressed")
                elif ((serialString.decode('Ascii')).strip() == "Released"):
                    print("Released")
                elif ((serialString.decode('Ascii')).strip() == "Lighton"):
                    print("Lighton")
                elif ((serialString.decode('Ascii')).strip() == "Lightoff"):
                    print("Lightoff")
                elif ((serialString.decode('Ascii')).strip() == "Shaked"):
                    print("Shaked")
        except Exception as e:
            print(e)
            break