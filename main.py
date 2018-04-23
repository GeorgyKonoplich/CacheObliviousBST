import random
import numpy as np
import datetime
import time

from bst_default import BST
from bst_veb import BSTVEB

length = 100000
array = random.sample(range(length), length)

bst = BST(array)
bst_veb = BSTVEB(bst, len(array))

number = 1000
k = 10
for step in range(0, 3):
    k = k * 10
    test_array = random.sample(range(number), 100) * k
    #random.shuffle(test_array)

    start_time = time.time()
    for x in test_array:
        bst.find(x)
    exec_time = time.time() - start_time
    print(exec_time)

    start_time = time.time()
    for x in test_array:
        bst_veb.find(x)
    exec_time = time.time() - start_time
    print(exec_time)
    print('----------------------')

