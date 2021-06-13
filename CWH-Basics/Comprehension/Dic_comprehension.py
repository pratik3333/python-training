dict1={'a':45,'b':65,'A':5}
print({k.lower():dict1.get (k.lower(), 0)+dict1.get(k.upper(), 0) for k in dict1.keys()})