import string

s = "A man, a plan, a canal: Panama"
s=s.replace(' ','')
s=s.translate(str.maketrans('', '', string.punctuation))
return s.lower()[::-1]==s.lower()