from flask import Flask, render_template
import serial, sys

print("\033c")
app = Flask(__name__)

### EDIT ###
HowManyVariablesIncoming = 7
refreshTime = 0.1
### EDIT ###



@app.route("/")
def home():
    global x
    print("\nHomeLoading")
    variables = ""

    while 1:
        if "END" in str(Device.readline()):
            print("Escaped WhileLoop\n")
            break

    for i in range(x):
        content = Device.readline()
        print("For Loop,", i, end="")
        content = content[:-5]
        variables = variables + str(content) + "\n"
        print(content)

    variables = variables.replace("b'", "")
    variables = variables.replace("'", "")

    print("Variables:")
    print(variables)
    return render_template("index.html", content=variables, refrate=refrate)

def serial_ports(): 
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]

    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
        
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')

    else:
        raise EnvironmentError('Unsupported platform')

    result = []

    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)

        except (OSError, serial.SerialException):
            pass

    return result

def portSelector():
    global comport_list
    if len(comport_list) == 0:
        print("No Comport, exiting...")
        exit()
    
    print("[-]: Aviable serial ports:")
    print(comport_list)
    port_id = int(input("Enter ID: "))
    port_id -= 1
    port = comport_list[port_id]
    print("You selected", port)
    return port

if __name__ == "__main__":

    x = HowManyVariablesIncoming
    refrate = refreshTime

    comport_list = serial_ports()
    ComPortName = portSelector()
    Device = serial.Serial(ComPortName, 115200, timeout=1)

    app.run()