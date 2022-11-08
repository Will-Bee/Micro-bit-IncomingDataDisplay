## BBC Micro:bit data visualization
# Instalation of libraries

```
pip uninstall serial
pip install flask pyserial
```
*Pre-installed library "serial" works differently


# Usage

### Setting up local server

```
$ python Main.py
[-]: Aviable serial ports:
[Com1, Com7, ...]
Enter ID:
```

You have to enter witch Com. you want to use, starting from 1

Then, local server will start, usually at `127.0.0.1:5000`

### Setting up BBC Micro:bit
In `BBC_Codes` Folder is a .hex file for Micro:bit and source code in python  
This script is adjustable for as many lines of data as you need  
You have to loop them like this:

```
def on_forever():
    serial.write_line("xAXIS: " + ("" + str(input.acceleration(Dimension.X))))
    serial.write_line("yAXIS: " + ("" + str(input.acceleration(Dimension.Y))))
    serial.write_line("zAXIS: " + ("" + str(input.acceleration(Dimension.Z))))
    serial.write_line("TEMP: " + ("" + str(input.temperature())))
    serial.write_line("LightLevel: " + ("" + str(input.light_level())))
    serial.write_line("SoundLevel: " + ("" + str(input.sound_level())))
    serial.write_line("Test: " + ("" + str(input.sound_level())))
    serial.write_line("END")
    basic.pause(100)
basic.forever(on_forever)
```

This `"END"` line is most important to be last one
This have to be in LOOP

### Timing and configuration
In Micro:bit script, there has be a timeout after sending `"END"` line  

*1 000 MS = 1S

#### in Main.py, line 8 and 9
`HowManyVariablesIncoming = 7` How many lines is incoming in one loop before `"END"`  
`refreshTime = 0.1` Your timeout
