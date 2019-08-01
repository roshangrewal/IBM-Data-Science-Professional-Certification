from scipy.sparse import *
from scipy import *
from numpy import *
import csv
S = dok_matrix((10000,10000), dtype=bool)
f = open("sampledata.csv")
reader = csv.reader(f)
for line in reader:
    S[int(line[0]),int(line[1])] = True