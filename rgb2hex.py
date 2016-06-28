"""
RGB to Hex Controller
Author - Chatura Samarasinghe

"""

def rgb_hex():
  invalid_msg = "Invalid RGB message"

  red = int (raw_input("Enter the Red(R) value : "));

  if red < 0 or red > 255:
    print invalid_msg;
    return;

  green = int(raw_input("Enter the Green(G) value : "));

  if(green < 0 or green > 255):
    print invalid_msg;
    return;

  blue = int(raw_input("Enter the Blue(B) value : "));

  if(blue < 0 or blue > 255):
    print invalid_msg;
    return;

  val = (red << 16) + (green << 8) +  blue;

  val = hex(val);

  """Check this line"""
  print "%s" %(val[2:]).upper();


def hex_rgb():
    hex_val = raw_input("Enter the Hexadecimal value: ");

    if (len(hex_val) != 6 ):
      print "invalid hex value"
    else:
      hex_val = int(hex_val, 16);

    #This will return the first RGB value (from right to left) of blue
    two_hex_digits = 2**8

    blue = hex_val % two_hex_digits;

    hex_val = hex_val >> 8
    green = hex_val % two_hex_digits;

    hex_val = hex_val >> 8
    red = hex_val % two_hex_digits;


    print "RGB values - Red:%d Green:%d Blue:%d" % (red,green,blue)

def convert():

  while(True):

    option = raw_input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter 'X' to Exit ")

    if (option == '1'):
        rgb_hex();
    elif (option == '2'):
        hex_rgb();
    elif(option == 'X' or option == 'x'):
      break;
    else:
      print "Error";

convert();
















