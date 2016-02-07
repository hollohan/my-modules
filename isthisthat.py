'''
	this function will test 'phrase' to see if it is of type 'type'
	right now, type can be 'char' or 'int'
'''

mydict = {
    'char'  : lambda phrase: True if phrase.isalpha() and len(phrase) == 1 else False,
    'int'   : lambda phrase: True if phrase.isdigit() else False
}

def isthisthat(phrase, type):
    if type in mydict:
        return mydict[type](phrase)
    else:
        print('invalid type')