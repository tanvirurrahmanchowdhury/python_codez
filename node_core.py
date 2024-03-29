import numpy as np

import argparse

# creating an argparse instance
parser = argparse.ArgumentParser(description='Test of Argparse')

# we can also set required = True inside add_argument() to force parser
# to input an argumentfrom the user. (default = None)
# -var_name (shorthand variable) no space in between - and var_name
# --var_name (actual variable) no space in between - and var_name
parser.add_argument('-j','--jobs',type=int,metavar='',default = 1, help='Jobs')

parser.add_argument('-c','--cores',type=int,metavar='',default = 256, help='Cores')

args = parser.parse_args() # this line is somehow needed


# kind of line void main() in C/C++. All equal signs and underscores are double
if __name__ == '__main__':
    print(f'Choose core to be the square of 4 times an even number!')
    print(f'Suggested nodes: {(args.cores * args.jobs)/64}')
    print(f'Suggested -n: {args.cores * args.jobs}')
    print(f'NPAR = {np.sqrt(args.cores)}')
