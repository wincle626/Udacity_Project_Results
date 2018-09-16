# **Car Behavior Clone** 

[//]: # (Image References)

[image1]: ./data_dist.png "dataprep"
[image2]: ./data_prep.png "imageproc"
[image3]: ./show_data_improve.png "dataprepimprove"
[image4]: ./datahist_improve.png "imageprocimprove"
[image5]: ./errloss_improve.png "errorloss"

### Project Files

|  Filename   |   Description  | 
|:-------------:|:-------------:|
| data_prep.py |  data preprocessing and argumentation |
| model1.py | define and train the neual network |
| model1.h5 | saved model by keras |
| drive.py | communicate with simulator and use saved model to predict steering angle  |
| video.mp4 | track 1 video record |

### Updated files:
|  Filename   |   Description  | 
|:-------------:|:-------------:|
| dataprep_improve.py |  improved data preprocessing and argumentation |
| model_improve.py | improved define and train the neual network |
| model_improve.h5 | improved saved model by keras |
| video_improve.mp4 | improved track 1 video record |

### Usage

Download simulator from [udacity repository](https://github.com/udacity/self-driving-car-sim), run the simulator in 
autonomous mode and execute following command:
```
> python drive.py model1.h5 run1
```

### Data Preprocessing & Argumentation
I used the trained data from the simulator. Using the simulator, the car is driving mannually for several rounds. Data is recorded as image and the corresponding steering, left/right turn, throttle, brake and speed are all saved in a .scv file. The distribution of data class labels are shown as:

![alt text][image1] 

The data is preprocessed with noise and flipping due to the most left turn training data. 
![alt text][image2] 

#### Improvement Update

After several days experiments, the hardest part is to prepare the data. Several modification compared to previous approach are made as follow:

    1. It ends up to remove the bright adjust, equalization, blur and adding noise to the image but only keep the flipping. Althrough this does not sound practical but it works in the simulator. 
    
    2. As the drive trail has more left turning, besides the image flipping, I also record the drive with opposite direction on the trial.
    
    3.Instead of using a single speed, the car is driven in differenct speed, especially slow down at the turn.
    
    4. Adding some small steering even on strainght path. 

As shown, the augment part is only image flipping:
![alt text][image3] 

As shown, the data is more balance in turns of the histgram of steering compared to previous one:
![alt text][image4] 


### Model Architecture and Training
The model is based on [Nvidia's paper](http://images.nvidia.com/content/tegra/automotive/images/2016/solutions/pdf/end-to-end-dl-using-px.pdf) 
with following modification:
* use input shape of 75x320x3 instead of 66x200x3
* use rgb channel instead of yuv
* remove first fully connected layer with 1164 neurons
* add a dropout layer to avoid overfitting
* use elu instead of relu as activate function of covolution layer

The training uses mean squared error as cost function and Adam optimizer with 0.001 learning rate,
10% data as validation data, 50 epochs and batch size of 32.

#### Improvement Update

Overall, the architecture uses 5 feature extraction layers using 2D convolution. The first three feature extraction layers use 5x5 kernel and stride (2,2) while the last two feature extraction layers use 3x3 kernel and unit stride. Then the 3D data is flatten into 1x1164 array and input to another 5 layers fully connect classifier. 

The model is slightly adjust according to the Nvidia paper. The modifications are as follow:

    1. A image cropping layer is added in Keras to meeting the exactly papar set up, (66, 200, 3). (75, 320, 3) does not sound bad but for some reason it does not perform very well. 
    
    2. A normalization layer is added which normalized the image data with mean 0 and standard divation 1. The Lambda(lambda x: x / 255.0- 0.5) only is used previously but it seems not enough. 
    
    3. Dropout layer and activation are added to the fully connected layer which does reduced the overfitting.
    
    4. The learning rate for Adam optimizer is set to much smaller then before, 0.00001, which allows better optimization space using small steps. The batch size is increased to 128 to accelerate the epochs. The validation data set uses 20% instead of 10%. An error loss figure is added to show the iterating process shown as follow:
    
![alt text][image5] 
