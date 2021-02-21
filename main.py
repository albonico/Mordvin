#!/usr/bin/python
# transliterate.py
# Import the argparse library
import argparse
import yaml

import os
import sys
from transliterate import transliterate

#Don't execute if importing file elsewhere
if __name__ == '__main__':
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

	my_parser.add_argument('--ofile', '-o',
	                    metavar='output_path',
	                    type=str,
						help='define name of output file to save result i.e. "output.txt"')

	# Execute the parse_args() method
	args = my_parser.parse_args()

	language = args.Language
	filepath = args.Path
	out_filepath = args.ofile


	# Read dictionary according to chosen language
	with open(f"Dictionaries/{language}.yml") as file:
	    rules = yaml.full_load(file)

	single_list,double=rules["single"],rules["double"]

	single={ a : b for a,b in zip(single_list[0],single_list[1])}

	# Load txt to be transliterated
	with open(filepath,"rb") as text_file:
		to_translit=text_file.read().decode("utf-8")



	out_text=transliterate(to_translit,single,double)

	if out_filepath is not None:
		with open(out_filepath,"w") as text_file:
			text_file.write(out_text)
	else:
		print(out_text)



