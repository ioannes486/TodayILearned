import time
from random import choice


num_list = [x for x in range(1, 27)]
alpha_list = [chr(x) for x in range(65, 65+26)]

for i in range(26):
  num = choice([x for x in range(26)])
  print (num, alpha_list(num))
  time.sleep(3)
