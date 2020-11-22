# author: Tiffany Timbers (still, I just modify)
# date: 2020-11-22


"""This script prints out docopt args.
Usage: docopt.py <arg> --arg2=<arg2> [--arg3=<arg3>] [--arg4=<arg4>]

Options:
<arg>             Takes any value (this is a required positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
[--arg4=<arg4>]   Takes any value (this is an optional option)
"""

from docopt import docopt
opt = docopt(__doc__)

def main(arg, arg2, arg3=NULL, arg4=NULL):
  arg_list = [arg, arg2, arg3, arg4]
  print(arg4)
  for i in arg_list:
    print(i)
    print(type(i))
  
if __name__ == "__main__":
  main(opt["arg"], opt["--arg2"], opt["--arg3"], opt["--arg4"])
