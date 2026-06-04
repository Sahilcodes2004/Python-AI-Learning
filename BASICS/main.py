#aceepting arguments
#import sys
#name=sys.argv[1]

#print("hello"+name)
import argparse
parser=argparse.ArgumentParser(
    description="This program prints the name of my dog"
)
parser.add_argument('-c','--color',metavar='color',required=True,
                   choices={'red','yellow'},help='the color search for')
args=parser.parse_args()

print(args.color)