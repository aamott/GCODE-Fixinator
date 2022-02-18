# GCODE Fixinator
Every finish a print and realize it didn't really finish? You come to see your lovely model only half finished? And for one reason or another, you can't use Power Loss Recovery - be it OctoPrint, a printer without Marlin, or a clog that luckily didn't mangle your model. I guess we restart that week long print...

But wait! Is that a glimmer of hope and a flat top surface? Try the GCODE Fixinator! Will it fix a clump of plastic on the nozzle? No. Unfortunately not. However, it *will* remove the entire already-printed part of your model so you can resume printing where it stopped! 

## How do I use GCODE Fixinator?
Well, first you're going to have to make sure the model's top surface is flat. If the nozzle left strands all over, you may be able to save it by removing them, but the top surface should be one smooth layer before you resume printing. 

Once you know the surface is flat, you need to find out the height. If you know the layer it's on and the layer height was consistent (i.e. not using adaptive layers) use those. Otherwise, measure the height of the last printed layer as accurately as you can.

You'll need Python to run the program for now. Run the program in Python and a window should come up with a prompt. 
Enter 'h' for height, 'l' (that's 'L') for layer.
You'll be asked to enter either the layer number or the height. Don't enter 'mm' following anything: just enter the number.  
Finally, enter the file name or path. Enter something like 
`example.gcode`,  
or `c:/users/me/Downloads/example.gcode`

To recap, you need: 
- A flat surface
- The last printed layer number or height of the model
- Python

## Requirements
- Python 3