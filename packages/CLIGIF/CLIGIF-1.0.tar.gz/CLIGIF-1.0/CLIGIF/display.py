import sys, os
def colored_sequence(char, rgb, brightness):
    try:
        r = rgb[0]+int((brightness-50)*1.5)
        g = rgb[1]+int((brightness-50)*1.5)
        b = rgb[2]+int((brightness-50)*1.5)
        if r < 0:
            r = 0
        elif r > 255:
            r = 255
        if g < 0:
            g = 0
        elif g > 255:
            g = 255
        if b < 0:
            b = 0
        elif b > 255:
            b = 255
        
        return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, char)
    except:
        pass
    
def display(arr, char='X', brightness=100, text="", auto_adjust=False):
    if text != "":
        if auto_adjust:
            for i in range(int(os.get_terminal_size().columns/2-len(text))):
                sys.stdout.write(" ")
        sys.stdout.write(text+'\n')
    if auto_adjust == True:
        for i in range(int(os.get_terminal_size().columns/2-arr.index("n"))):
            sys.stdout.write(" ")
    for i in arr:
        if i != 'n':
            if colored_sequence(char, i, brightness) != None:
                sys.stdout.write(colored_sequence(char, i, brightness))
              
        else:
            sys.stdout.write('\n');
            if auto_adjust == True:
                for i in range(int(os.get_terminal_size().columns/2-arr.index("n"))):
                    sys.stdout.write(" ")
                  
            