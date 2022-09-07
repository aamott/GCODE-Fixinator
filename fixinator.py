import re

cut_by = None
while cut_by != 'l' and cut_by != 'h' and cut_by != 'L' and cut_by != "H":
    cut_by = input("Cut by (L)ayer number or Z (H)eight? ([L]/h): ")
    if cut_by == '': # default
        cut_by = "L"

z_height = None
# Cut by z height
if cut_by.lower() == 'h':
    z_height = None
    while type(z_height) is not float:
        try:
            z_height = input("What is the Z height in mm? Height: ").strip()
            z_height = z_height.rstrip("mm") # in case they put 'mm'
            z_height = float(z_height)
        except:
            print("Please enter a number. Ex. '30'")
            
# Cut by layer
elif cut_by.lower() == "l":
    num_layers = None
    while type(num_layers) is not int:
        try:
            num_layers = input("Enter the last printed layer: ")
            num_layers = int(num_layers)
        except:
            print("Please enter a number. Ex. '50'")

    layer_height = None
    while type(layer_height) is not float:
        try:
            layer_height = input("Enter layer height (0.2mm default): ")
            if layer_height == '': #default
                layer_height = 0.2
                continue
            layer_height = layer_height.rstrip("mm") # in case they put 'mm'
            layer_height = float(layer_height) or 0.2
        except:
            print("Please enter a number. Ex. '0.2'")

    z_height = layer_height * num_layers 

# Test if the file can be opened.
file_success = None
while not file_success:
    filename = input("Enter the gcode filename or file path: ")
    try:
        with open(filename):
            file_success = True
            print("File", filename, "opened successfully.")
    except:
        print("File failed to open. Re-enter filename.")

# Test if the new file can be opened/created
file_success = None
new_filename = "cut_" + filename
while not file_success:
    try:
        with open(new_filename, "w"):
            file_success = True
            print("New file", new_filename, "created")
    except:
        print(f"Failed to create a new file '{new_filename}'")
        print("Try entering a new filename/filepath.")
        new_filename = input("Please enter the name or path for the new gcode file: ")

try:
    with open(filename) as file, open(new_filename, "w") as new_file:
        still_searching = True
        for line in file:
            # skip comments
            if still_searching:
                if line.startswith(';'): # keep comments
                    new_file.write(line)
                
                elif line.startswith("G28"): # DON'T let it home Z!
                    new_file.write("G28 X Y\n")

                elif line.startswith("G204"): # remove acceleration change commands. They clutter the code. 
                    continue
                
                elif line.startswith("G1") or line.startswith("G0") or line.startswith("G3")  or line.startswith("G2"): # Move command!
                    height = re.search("Z\\d+\\.?\\d*", line) # each line should only have 1 match at most
                    if height:
                        height = height[0]
                        height = height.strip("Z")
                        height = float(height)
                        if height >= z_height:
                            print("Found height to stop cutting at! That line was:")
                            print(line)
                            set_height = "G92 Z" + str(height) + "\n"
                            print("Adding a line to tell the extruder that it's at height", set_height)
                            new_file.write(set_height)

                            new_file.write(line)
                            # from here on out, we want to save everything.
                            still_searching = False
                        else:
                            continue
                    else:
                        continue # was a move, but no Z...

                else: # default to writing the line. Heating up, status, ...
                    new_file.write(line)

            else: # just plain copy everything once the z height has been matched
                new_file.write(line)

except Exception as error:
    print("Error writing to file.")
    print(error)