# Import
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from skimage import io, color, exposure, filters, img_as_ubyte
from skimage.transform import resize
from skimage.util import random_noise
import warnings
import sys
import cv2

# Data 
data_folder = './data1/'
drive_log = pd.read_csv(data_folder + 'driving_log.csv')
drive_log.head()

# Analysis of data
fig=plt.figure(figsize=(16, 16))
ax = fig.add_subplot(2, 2, 1)
ax.set_title("Steering", fontsize=24)
plt.hist(drive_log['steering'], bins=100)
ax = fig.add_subplot(2, 2, 2)
ax.set_title("Throttle", fontsize=24)
plt.hist(drive_log['throttle'], bins=100)
ax = fig.add_subplot(2, 2, 3)
ax.set_title("Brake", fontsize=24)
plt.hist(drive_log['brake'], bins=100)
ax = fig.add_subplot(2, 2, 4)
ax.set_title("Speed", fontsize=24)
plt.hist(drive_log['speed'], bins=100)
plt.savefig("datahist.png")
plt.show()

def generate_data(line):
    type2data = {}
    
    # center image
    center_img = io.imread(line['center'].strip())
    center_ang = line['steering']
    type2data['center'] = (center_img, center_ang)
    
    # flip image if steering is not 0
    if line['steering']:
        flip_img = center_img[:, ::-1]
        #flip_img = cv2.flip(center_img, 1)
        flip_ang = center_ang * -1
        type2data['flip'] = (flip_img, flip_ang)
    
    # left image 
    left_img = io.imread(line['left'].strip())
    left_ang = center_ang + .2+ .05 * np.random.random()
    left_ang = min(left_ang, 1)
    type2data['left_camera'] = (left_img, left_ang)
    
    # right image
    right_img = io.imread(line['right'].strip())
    right_ang = center_ang - .2 - .05 * np.random.random()
    right_ang = max(right_ang, -1)
    type2data['right_camera'] = (right_img, right_ang)
    
    # crop all images
    for name, (img, ang) in type2data.items():
        #plt.imshow(img)
        #plt.show()
        img = img[55: -30, ...]
        type2data[name] = (img, ang)
        #plt.imshow(img)
        #plt.show()
    
    return type2data

def show_data(type2data):
    col = 4
    #row = 1 + len(type2data) // 4
    row = 1 + len(type2data) // 4
    
    #f, axarr = plt.subplots(2, col, figsize=(16, 4))
    f, axarr = plt.subplots(row, col, figsize=(16, 4))

    for idx, (name, (img, ang)) in enumerate(type2data.items()):
        axarr[idx//col, idx%col].set_title('{}:{:f}'.format(name, ang))
        axarr[idx//col, idx%col].imshow(img)
    plt.savefig("show_data.png")
    plt.show()

type2data = generate_data(drive_log.iloc[0])

# Generate all rows of data
line = type2data
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    
    X_train, y_train = [], []
    for idx, row in drive_log.iterrows():
        type2data = generate_data(row)
        for img, ang in type2data.values():
            X_train.append(img)
            y_train.append(ang)
        if(row['steering']):
            line = row

X_train = np.array(X_train)
y_train = np.array(y_train)

# plot the distribution, tried distribution more uniform but doesn't work well
plt.hist(y_train, bins=100)
plt.savefig("trainclasshist.png")
plt.title("Hist of Angle")
plt.show()
type2data = generate_data(line)
show_data(type2data)



# won't use keras fit generator since it's only 2.39 gb 
gb = (sys.getsizeof(X_train) + sys.getsizeof(y_train)) / 2**30
print('size: {:f} GB'.format(gb))

# save training data
np.save('X_train', X_train)
np.save('y_train', y_train)
