def transliterate(text,single_dic,double):
	
	for cyr,lat in double.items():
		text=text.replace(cyr.capitalize(),lat.capitalize())
		text=text.replace(cyr,lat)

	for cyr,lat in single_dic.items():
		text=text.replace(cyr.upper(),lat.upper())
		text=text.replace(cyr,lat)

	return text