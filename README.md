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
You must loop them like this

```
def on_forever():
    serial.write_line("xAXIS: " + ("" + str(input.acceleration(Dimension.X))))
    serial.write_line("yAXIS: " + ("" + str(input.acceleration(Dimension.Y))))
    serial.write_line("zAXIS: " + ("" + str(input.acceleration(Dimension.Z))))
    serial.write_line("TEMP: " + ("" + str(input.temperature())))
    serial.write_line("LightLevel: " + ("" + str(input.light_level())))
    serial.write_line("SoundLevel: " + ("" + str(input.sound_level())))
    serial.write_line("Test: " + ("" + str(input.sound_level())))
+ (input.sound_level() + input.sound_level()))))))
    serial.write_line("END")
    basic.pause(100)
basic.forever(on_forever)```
