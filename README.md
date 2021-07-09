## BBC Micro:bit data visualization
# Instalation of libraries

```
pip uninstall serial
pip install flask pyserial
```
It's bcs python have build-in library  
called serial that works differently


# Usage

### Setting up local server

```
C:\Users\Admin> python Main.py
[-]: Aviable serial ports:
[Com1, Com7, ...]
Enter ID:
```

You will enter witch port is your micro:bit,  
for example, if your m:b is Com7, you enter number 2 bcs it is displayed on second place

Then, local server will start on IP `127.0.0.1:5000`  
or you can click link in your terminal

### Setting up BBC Micro:bit
In `BBC_Codes` Folder, is .hex code for Micro:bit and source code in python  
This script is adjustable for as many lines of data as you need  
You must loop them like this:

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

This `"END"` Line is most important to be last one of all of them  
This must be in LOOP

### Timing and configuration
In Micro:bit script, there must be a timeout after sending `"END"` line  
This timeout is in MS  
1 000 MS = 1S

#### in Main.py, line 8 and 9
`HowManyVariablesIncoming = 7` How many lines is incoming in one loop before `"END"`  
`refreshTime = 0.1` How long is timeout setted in Micro:bit

If you got any Issue, open an Issue, i'll fix it
