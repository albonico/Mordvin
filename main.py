#!/usr/bin/python
# transliterate.py
# Import the argparse library
import argparse

import os
import sys
from transliterate import transliterate

from dict_M import single_dic as single_M
from dict_M import double as double_M
from dict_E import single_dic as single_E
from dict_E import double as double_E


# Create the parser
my_parser = argparse.ArgumentParser(description='Transliterate text from cyrillic')

# Add the arguments
my_parser.add_argument('Language',
                       metavar='lang',
                       type=str,
                       help='selects Erzya or Moksha')

my_parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='contains text file path')

# Execute the parse_args() method
args = my_parser.parse_args()

language = args.Language
filepath = args.Path

if language=="Moksha":
	single,double=single_M,double_M
elif language=="Erzya":
	single,double=single_E,double_E


with open(filepath,"rb") as text_file:
	to_translit=text_file.read().decode("utf-8")

# import pdb

# pdb.set_trace()

print(transliterate(to_translit,single,double))
