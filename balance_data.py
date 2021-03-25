import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2

train_data = np.load('training_data.npy')

df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))

lefts = []
rights = []
jumps = []

shuffle(train_data)

for data in train_data:
    img = data[0]
    choice = data[1]

    if choice == [1,0,0]:
        lefts.append([img,choice])
    elif choice == [0,1,0]:
        jumps.append([img,choice])
    elif choice == [0,0,1]:
        rights.append([img,choice])
        

lefts = lefts[:len(jumps)][:len(rights)]
jumps = jumps[:len(lefts)]
rights = rights[:len(lefts)]

final_data = jumps + lefts + rights
shuffle(final_data)
print(len(final_data))
np.save('balanced_training_data.npy', final_data)
