# **Car Behavior Clone** 

[//]: # (Image References)

[image1]: ./data_dist.png "dataprep"
[image2]: ./data_prep.png "imageproc"

### Project Files

|  Filename   |   Description  | 
|:-------------:|:-------------:|
| data_prep.py |  data preprocessing and argumentation |
| model1.py | define and train the neual network |
| model1.h5 | saved model by keras |
| drive.py | communicate with simulator and use saved model to predict steering angle  |
| video.mp4 | track 1 video record |

### Usage

Download simulator from [udacity repository](https://github.com/udacity/self-driving-car-sim), run the simulator in 
autonomous mode and execute following command:
```
> python drive.py model.h5 run1
```

### Data Preprocessing & Argumentation
I used the trained data from the simulator. Using the simulator, the car is driving mannually for several rounds. Data is recorded as image and the corresponding steering, left/right turn, throttle, brake and speed are all saved in a .scv file. The distribution of data class labels are shown as:

![alt text][image1] 

The data is preprocessed with noise and flipping due to the most left turn training data. 
![alt text][image2] 

### Model Architecture and Training
The model is based on [Nvidia's paper](http://images.nvidia.com/content/tegra/automotive/images/2016/solutions/pdf/end-to-end-dl-using-px.pdf) 
with following modification:
* use input shape of 75x320x3 instead of 66x200x3
* use rgb channel instead of yuv
* remove first fully connected layer with 1164 neurons
* add a dropout layer to avoid overfitting
* use elu instead of relu as activate function of covolution layer
