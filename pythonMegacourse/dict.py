import json
from difflib import get_close_matches
a=input()
b=json.load(open("dictdata.json"))
def dict(a):
    if a.lower() in b:
       return(b[a.lower()])
    elif a.title() in b:
       return(b[a.title()])
    elif a.upper() in b:
        return(b[a.upper()])
    elif len(get_close_matches(a,b.keys()))>0:
       return ("Please check whether you are referring to some of the following text"+str(get_close_matches(a,b.keys()))+"\nIf yes then,try it with the above mentioned text ")

    else:
           return("Enter correct word")
print(dict(a))
