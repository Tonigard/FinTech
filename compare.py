from functools import lru_cache
from timeit import timeit

import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
print(input_file, output_file)
def my_dist_cached(a, b):
    def recursive(i, j):
        if i == 0 or j == 0:
            return max(i, j)
        elif a[i - 1] == b[j - 1]:
            return recursive(i - 1, j - 1)
        else:
            return 1 + min(
                recursive(i, j - 1), 
                recursive(i - 1, j), 
                recursive(i - 1, j - 1)
            )
    r = recursive(len(a), len(b))
    return r
#print(my_dist_cached("hello world", "hell world!"))

mistakes_count = []
lenght = [] 
with open(input_file, 'r') as f:
    for line in f.readlines():
        try:
            directorys = line.strip().split()
            file1, file2 = directorys[0], directorys[1]
            text1, text2 = '', ''
            with open(file1, 'r') as f:
                text1 = f.read()
            with open(file2, 'r') as f:
                text2 = f.read()

            mistakes_count.append(my_dist_cached(text1, text2))
            lenght.append(len(text1))
        except:
            continue

with open(output_file, 'a') as f:
    for i in range(len(mistakes_count)):
        f.write(str(mistakes_count[i]/lenght[i])+'\n')
