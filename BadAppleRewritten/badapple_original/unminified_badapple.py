import time, gzip

def render(frame):
    col=0                       # we start at the zeroth column ofc
    rendered=''                 # initialize the current frame as an empty string
    for byte in frame:          # for each byte (pixel) in the frame bytecode
        if col == 40:           # if we're at the last column
            col = 0             # set the column back to zero
            rendered += '\n'    # and add a newline to the current frame (to move to the next row)
        col += 1                # add one to the column
        if byte == 0:           # if the current byte we're reading is a zero (black)
            rendered += '  '    # add a black pixel to the frame
        else:                   # else (the pixel is white)
            rendered += '%%'    # add a white pixel to the frame
    print(rendered+'\x1b[30A')  # print the rendered frame and jump 30 lines back up

start = time.time()
frame = 0

try:
    bpf = 1200                                        # bytes per frame (why hard programmed?????????)
    file = gzip.open('baddestapple.dat.gz')           # read the data file using the gzip module
    while frame<6573:                                 # while under the number of frames (juliet why is this hard programmed?!?)
        frame = int((time.time() - start) * 30) + 1   # get current frame to display
        file.seek(frame * bpf)                        # set the cursor in the file to the current frame
        render(file.read(bpf))                        # read the current frame and send it off to be rendered
        time.sleep(.02)                               # wait!
except KeyboardInterrupt:                             # catch a ctrl+c
    print('\x1b[30B')                                 # move 30 lines down (we draw from the top)

    #this is the original version of my bad apple demo
    #the way i had audio working was really broken so nearly 3 years later i just said "fuck it" and completely removed it
    #we do not talk about it trust me!
    #created by AverageJuliet

#  __________________________________________________________
# / hi guys!! i'm carter (@carteeeee on discord)             \
# | juliet made the horrible desicion of minifying this code |
# | and then she made me unminify it :sob:                   |
# | i mean tbh it was fine because i was bored so like...    |
# | yeah. anyways thanks for reading this and my other       |
# | code comments!                                           |
# \__________________________________________________________/
#
