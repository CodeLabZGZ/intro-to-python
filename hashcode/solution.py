import csv
import numpy as np
import os
import random

def read_input(dir, filename):
  with open(dir+"/"+filename+".in", 'r') as file:
    csv_reader = csv.reader(file, delimiter=' ')
    rows, columns, min, max = next(csv_reader)
    pizza = [list(line[0]) for line in csv_reader]
  return int(rows), int(columns), int(min), int(max), np.array(pizza)

def write_output(correct_slices, dir, filename):
    if not os.path.exists(dir):
        os.makedirs(DIRECTORY)
    
    with open(dir+"/s_"+filename+".in", 'w+') as out: 
        total = len(correct_slices)
        out.write(str(total)+"\n")
        for sli in correct_slices:
            out.write(' '.join(map(str, sli))+"\n")   
        print(total)

def random_cuts(ROWS, COLUMNS, H):
    """ Creates random cuts to try that have less or equal the maximum number of slices"""
    r1 = random.randint(0, ROWS-1)
    c1 = random.randint(0, COLUMNS-1)
    
    r2 = r1+random.randint(0,min(H,ROWS-r1)-1)
    c2 = c1+random.randint(0,min((H//(r2-r1+1)),COLUMNS-c1)-1)
    return r1, c1, r2, c2

def correct_slice(pizza, r1, c1, r2, c2, R, C, L, H):
  try_slice = pizza[r1:r2+1, c1:c2+1]
  
  if 'x' in try_slice:
    return False
  else:
    tomato = np.count_nonzero(try_slice == 'T')
    mush = np.count_nonzero(try_slice == 'M')
    
    if tomato >= L and mush >= L and try_slice.size <= H:
      return True
    else:
      return False

def cut_slice(pizza, r1, c1, r2, c2):
    """Cut the slice passed by changing to 'x' those pieces"""
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            pizza[i][j] = 'x'
            
DIRECTORY = "hashcode"
FILENAME = "c_medium"
NUM_RAND_COORD = 10000

ROWS, COLUMNS, L, H, PIZZA = read_input(DIRECTORY, FILENAME)

correct_slices = []

for _ in range(NUM_RAND_COORD):
  r1, c1, r2, c2 = random_cuts(ROWS, COLUMNS, H)

  if correct_slice(PIZZA, r1, c1, r2, c2, ROWS, COLUMNS, L, H):
    cut_slice(PIZZA, r1, c1, r2, c2)
    sli = [r1, c1, r2, c2]
    correct_slices.append(sli)
    
write_output(correct_slices, DIRECTORY, FILENAME)
