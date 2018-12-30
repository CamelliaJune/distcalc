 #!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
import numpy as np
vector1 = []
vector2 = []
with open(sys.argv[1]) as f1:
    for line in f1:
        line_list = line.split(',')
        vector1.append(np.array(line_list,dtype = float))

with open(sys.argv[2]) as f2:
    for line in f2:
        line_list = line.split(',')
        vector2.append(np.array(line_list,dtype = float))

line_num = len(vector1)

for i in range(line_num):
    distance=np.sum(np.square(vector1[i]-vector2[i]))
    print(distance)