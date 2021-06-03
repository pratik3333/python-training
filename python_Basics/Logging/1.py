

import logging
import Employee

logging.basicConfig(filename='sample.log',level=logging.DEBUG)



def add(x,y):
    return x + y


num_1=1000
num_2=100

add_result=add(num_1,num_2)

#print(f'add {num_1},{num_2} = {add_result}')
#logging.warning(f'add {num_1},{num_2} = {add_result}')
#logging.error(f'add {num_1},{num_2} = {add_result}')
#logging.critical(f'add {num_1},{num_2} = {add_result}')
logging.debug (f'add {num_1},{num_2} = {add_result}'
               )
#