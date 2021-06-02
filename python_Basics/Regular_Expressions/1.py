
import re

my_str='''+917249672727 February 2000 – Tetley Tea Company, $407 million[7]
March 2004 – Daewoo Commercial Vehicle Company, $102 million
August 2004 – NatSteel's Steel business, $292 million
November 2004 – Tyco Global Network, $130 million
July 2005 – Teleglobe International Holdings, $239 million
October 2005 – Good Earth Corporation
December 2005 – Millennium Steel, Thailand, $165 million
December 2005 – Brunner Mond Chemicals, $10 million
June 2006 – Eight O'Clock Coffee, $220 million
November 2006 – Ritz Carlton Boston, $170 million
January 2007 – Corus Group, $12 billion[8]
March 2007 – PT Kaltim Prima Coal (KPC) (Bumi Resources), $1.1 billion
April 2007 – Campton Place Hotel, San Francisco, $60 million
January 2008 – Imacid Chemical Company, Morocco[9]
February 2008 – General Chemical Industrial Products, $1 billion 5746-78243-7842
Pratikkagale@gmail.com'''

#findout,search,split,sub,finditer

#Mete characters
#patt=re.compile(r'Morocco')
#patt=re.compile(r'.')  # . Any character (except newline character)
#patt=re.compile(r'.ary')  # ends with
#patt=re.compile(r'^Chemical')  # ^ starts with
#patt=re.compile(r'ion$')  # $ Ends with
#patt=re.compile(r'al*')  # * Zero or more accurrences
#patt=re.compile(r'ber{2}')  # {} Exactly number of accurrences
#patt=re.compile(r'(ber){1}')  # () Capture and group
#patt=re.compile(r'ber{1}|n')  # | Either or


#Special sequences
#patt=re.compile(r'\AMarch')   #\A returns a match if the specified characters are at the beginning of the string
#patt=re.compile(r'\bMarch')   #\A returns a match where the specified characters are at the beginning or at the end of a word
#patt=re.compile(r'06\b')   #\A returns a match where the specified characters are at the beginning or at the end of a word
#patt=re.compile(r'\d{5}-\d{4}')
#patt=re.compile(r'\d{10}')
patt=re.compile(r'[a-zA-z]+[a-zA-Z]+\.com')
matches=patt.finditer(my_str)
for match in matches:
    print(match)