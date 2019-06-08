
# random password generator program

import random as rd

print(f'Your Password is :' ,(lambda x=rd.randint(5 ,10) :''.join([chr(rd.randint(33 ,122)) for _ in range(x)]))())

