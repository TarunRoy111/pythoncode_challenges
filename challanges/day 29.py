## write a program to check ipv4 configuration

import re

p = r'\b(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\b'

inp = 'my ip is 192.168.250.24'  
is_matched = re.findall(p, inp)

if is_matched:
    valid_ip = '.'.join(is_matched[0])
    print(valid_ip)  
else:
    print('not found or invalid')


#write an example program for abstraction example

from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def display(self):
        print("Hello")
class B(A):
    def display(self):
        print("Hiii")
        
b=B()
b.display()
