import re

def transliterate(text,single_dic,double):

	for cyr,lat in double.items():
		text=text.replace(cyr.capitalize(),lat.capitalize())
		text=text.replace(cyr,lat)

	for cyr,lat in single_dic.items():
		text=text.replace(cyr.upper(),lat.upper())
		text=text.replace(cyr,lat)
		
	return text

def wordwise_transliterate(text,first_syl,last_syl,first_let,last_let,consonants,vowels1,vowels2):

	if consonants is None and (first_syl or last_syl):
		raise ValueError('No consonants defined for syllable rules')

	first_syl_mono=filterTheDict(first_syl,lambda elem: len(elem[0]) == 1)
	first_syl_double=filterTheDict(first_syl,lambda elem: len(elem[0]) >= 2)

	last_syl_mono=filterTheDict(last_syl,lambda elem: len(elem[0]) == 1)
	last_syl_double=filterTheDict(last_syl,lambda elem: len(elem[0]) >= 2)

	text=re.sub(r"(["+vowels1.upper()+r"])(["+vowels2+r"])",r"\1"+"j"+r"\2",text)
	text=re.sub(r"(["+vowels1+r"])(["+vowels2+r"])",r"\1"+"j"+r"\2",text)

	for (key,val) in first_let.items():
		text=re.sub(r"(\b)"+key.capitalize(),r"\1"+val.capitalize(),text)
		text=re.sub(r"(\b)"+key,r"\1"+val,text)

	for (key,val) in last_let.items():
		text=re.sub(key+r"(\b)",val+r"\1",text)

	for (key,val) in first_syl_double.items():
		text=re.sub(r"(\b["+consonants.upper()+"]*)"+key,r"\1"+val,text)
		text=re.sub(r"(\b["+consonants+"]*)"+key,r"\1"+val,text)

	for (key,val) in last_syl_double.items():
		text=re.sub(key+r"["+consonants+"]*\b",val+r"["+consonants+"]*\b",text)

	for (key,val) in first_syl_mono.items():
		text=re.sub(r"(\b["+consonants.upper()+"]*)"+key,r"\1"+val,text)
		text=re.sub(r"(\b["+consonants+"]*)"+key,r"\1"+val,text)

	for (key,val) in last_syl_mono.items():
		text=re.sub(key+r"["+consonants+"]*\b",val+r"["+consonants+"]*\b",text)

	return text


def latin_replacements(text,double_consonants):
	cons_with_accent="".join(double_consonants.values())

	for x,y in double_consonants.items():
		text=re.sub(x.capitalize()+r"(["+cons_with_accent+"])",y.capitalize()+r"\1",text)
		text=re.sub(x+r"(["+cons_with_accent+"])",y+r"\1",text)

	return text


def filterTheDict(dictObj, callback):
    newDict = dict()
    # Iterate over all the items in dictionary
    for (key, value) in dictObj.items():
        # Check if item satisfies the given condition then add to new dict
        if callback((key, value)):
            newDict[key] = value
    return newDict