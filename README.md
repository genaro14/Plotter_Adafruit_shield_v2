# Plotter_Adafruit_shield_v2

## Code Example for Plotting with an Adafruit Motor Shield V2

This is more a toy than a working machine. You are adviced

[Structure:](https://www.thingiverse.com/thing:3521286)     
[Pen holder:](https://www.thingiverse.com/thing:1372864)        
[Carriages: ](https://www.thingiverse.com/thing:3561319)        

 


The code has been tested using and arduino uno and the Adafruit Motor shield V2

### Parts
+ Arduino Uno
+ Adafruit Motor shield V2
+Cd rom recicled stepper motors (and fixing bolts) x2
+ 3mm rods x5 (at least)
+ Psu 5v (cellphone)
## Gcode Sender 
A Gcode basic sender is included in cli and GUI.    
It will send the commans in the test.gcode file to the plotter.
``` bash
$ python3 sender_gui.py
```
### Quick Cheatsheet

    // G1 for moving
    // G4 P300 (wait 150ms)
    // M300 S30 (pen down)
    // M300 S50 (pen up)
    // Discard anything with a (
    // Discard any other command!

TODO: add pictures and upload modified pen holder.

