# GCODE Fixinator
## *Try it out: [GCODE Fixinator](fixinator.htm)*


Ever finish a print and realize it didn't really finish? You come to see your lovely model only half finished? And for one reason or another, you can't use Power Loss Recovery - be it OctoPrint, a printer without Marlin, or a clog that luckily didn't mangle your model. I guess we restart that week long print...

But wait! Is that a glimmer of hope and a flat top surface? Try the GCODE Fixinator! It removes the entire already-printed part of your model so you can resume printing where it stopped! 

When a print is interrupted, it often leaves behind a perfectly good model base, just missing a top. GCODE Fixinator removes the already-printed GCODE, homes the X and Y axes, reheats the nozzle and bed, and then resumes the print.

## How do I use GCODE Fixinator?
Well, first you're going to have to make sure the model's top surface is flat. If the nozzle left strands all over, you may be able to save it by removing them, but the top surface should be one smooth layer before you resume printing. 

Once you know the surface is flat, you need to find out the height. If you know the layer it's on and the layer height was consistent (i.e. not using adaptive layers) use those. Otherwise, measure the height of the last printed layer as accurately as you can.

### JavaScript Version
Open fixinator.htm and enter the layer height and lanumbers of layers or the height in mm.

### Python Version
Run the program in Python and a window should come up with a prompt. 
Enter 'h' for height, 'l' (that's 'L') for layer.
You'll be asked to enter either the layer number or the height. Don't enter 'mm' following anything: just enter the number.  
Finally, enter the file name or path. Enter something like 
`example.gcode`,  
or `c:/users/me/Downloads/example.gcode`

To recap, you need: 
- A flat top surface
- The last printed layer number or height of the model
- Python or a Browser

## Requirements
- Python 3  
or 
- A Browser