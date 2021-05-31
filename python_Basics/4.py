

import datetime

my_date=datetime.datetime(2021,5,31)


#march 31, 2018 fell on a Tuesday and was the 120 day of the year

sentence='{0:%B %d, %y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)