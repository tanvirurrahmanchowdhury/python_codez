import math, argparse

# creating an argparse instance
parser = argparse.ArgumentParser(description='Test of Argparse')

# we can also set required = True inside add_argument() to force parser
# to input an argumentfrom the user. (default = None)
# -var_name (shorthand variable) no space in between - and var_name
# --var_name (actual variable) no space in between - and var_name
parser.add_argument('-r','--radius',type=int,metavar='',default = 3, help='Radius')

parser.add_argument('-H','--height',type=int,metavar='',default = 2, help='Height')

args = parser.parse_args() # this line is somehow needed

# function definition
def cylinder(r,h):
    return (math.pi) * (r**2) * h
    
# kind of line void main() in C/C++. All equal signs and underscores are double
if __name__ == '__main__':
    # args.(same name as --variable name in add_argument
    print(cylinder(args.radius,args.height))
