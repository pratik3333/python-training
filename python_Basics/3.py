

import datetime
my_date=datetime.datetime(2021,5,31)

#may 05, 2021
sentence='{:%B %d, %y}'.format(my_date)
print(sentence)