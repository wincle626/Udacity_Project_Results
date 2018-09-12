# **Traffic Sign Recognition** 

---

**Build a Traffic Sign Recognition Project**

The goals / steps of this project are the following:
* Load the data set (see below for links to the project data set)
* Explore, summarize and visualize the data set
* Design, train and test a model architecture
* Use the model to make predictions on new images
* Analyze the softmax probabilities of the new images
* Summarize the results with a written report


[//]: # (Image References)

[image1]: ./results/input_data_statistic.png "Visualization"
[image2]: ./results/input_data_preprocessing.png "Grayscaling"
[image3]: ./results/training_valid_accuracy.png "Training Accuracy"
[image4]: ./results/load_data_preprocessing.png "Five Traffic Signs"
[image5]: ./results/load_data_softmax.png "Five Traffic Signs Classifier"
[image6]: ./results/load_data_featuremap1.png "Featuremap1"
[image7]: ./results/load_data_featuremap2.png "Featuremap2"
[image8]: ./newresults/uniforminputdata.png "uniforminput"
[image9]: ./newresults/accuracyimprove.png "accuracyimprove"
[image10]: ./newresults/newsoftmax.png "newsoftmax"

## Rubric Points
### Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/481/view) individually and describe how I addressed each point in my implementation.  

---
### Writeup / README

#### 1. Provide a Writeup / README that includes all the rubric points and how you addressed each one. You can submit your writeup as markdown or pdf. You can use this template as a guide for writing the report. The submission includes the project code.

You're reading it! and here is a link to my [project code](https://github.com/wincle626/Udacity_Project_Results/blob/master/project02/Traffic_Sign_Classifier.ipynb)

### Data Set Summary & Exploration

#### 1. Provide a basic summary of the data set. In the code, the analysis should be done using python, numpy and/or pandas methods rather than hardcoding results manually.

I used the matplotlib library to calculate summary statistics of the traffic
signs data set:

* The size of training set is 34799
* The size of the validation set is 4410
* The size of test set is 12630
* The shape of a traffic sign image is (32, 32)
* The number of unique classes/labels in the data set is 43

#### 2. Include an exploratory visualization of the dataset.

Here is an exploratory visualization of the data set. It is a bar chart showing how the data distributed among all the 43 classes. 

Old:
![alt text][image1]

New:
![alt text][image8]


From the bar chart, it worth notice that there is an bias of classes across 43 different labels. Not sure how much it will affect on the training process, which needs further exploration. 

### Design and Test a Model Architecture

#### 1. Describe how you preprocessed the image data. What techniques were chosen and why did you choose these techniques? Consider including images showing the output of each preprocessing technique. Pre-processing refers to techniques such as converting to grayscale, normalization, etc. (OPTIONAL: As described in the "Stand Out Suggestions" part of the rubric, if you generated additional data for training, describe why you decided to generate additional data, how you generated the data, and provide example images of the additional data. Then describe the characteristics of the augmented training set like number of images in the set, number of images for each class, etc.)

The first step is to do a grayscaling, which reduce the training data size from 3 dimention color space to single gray space. Because the traffic sign is most likely related to the shape not the color. 

Secondly, the data set is normalized and standarized to remove the bias in terms of the data value itself. 

Thirdly, the data set is enhanced by adding random noise and rotation of the original training set. This is trying to enrich the diversity of training samples.  

The difference between the original data set and the all pre-processed data set is the following: 

![alt text][image2]

#### 2. Describe what your final model architecture looks like including model type, layers, layer sizes, connectivity, etc.) Consider including a diagram and/or table describing the final model.

I am still using the lenet to do this project, the architecture is as following:

Old architecture
| Layer         		|     Description	        					| 
|:---------------------:|:---------------------------------------------:| 
| Input         		| 32x32x1 RGB image   							| 
| Convolution 5x5     	| 1x1 stride, valid padding, outputs 28x28x6 	|
| RELU					|												|
| Max pooling	      	| 2x2 stride,  outputs 14x14x6 				|
| Convolution 5x5	    | 1x1 stride, valid padding, outputs 10x10x16      									|
| RELU					|												|
| Max pooling	      	| 2x2 stride,  outputs 5x5x16 				|
| Fully connected		| input 400, output = 120        									|
| RELU					|												|
| Fully connected		| input 120, output = 84        									|
| RELU					|												|
| Fully connected		| input 84, output = 43        									|
| Softmax				| input 43, output = 43        									|
|						|												|
|						|												|
 

New architecture
| Layer         		|     Description	        					| 
|:---------------------:|:---------------------------------------------:| 
| Input         		| 32x32x3 RGB image   							| 
| Convolution 5x5     	| 1x1 stride, valid padding, outputs 28x28x6 	|
| RELU					|												|
| Max pooling	      	| 2x2 stride,  outputs 14x14x6 				|
| Convolution 5x5	    | 1x1 stride, valid padding, outputs 10x10x16      									|
| RELU					|												|
| Max pooling	      	| 2x2 stride,  outputs 5x5x16 				|
| Fully connected		| input 400, output = 120        									|
| RELU					|												|
| Fully connected		| input 120, output = 84        									|
| RELU					|												|
| Fully connected		| input 84, output = 43        									|
| Softmax				| input 43, output = 43        									|
|						|												|
|						|												|

#### 3. Describe how you trained your model. The discussion can include the type of optimizer, the batch size, number of epochs and any hyperparameters such as learning rate.

To train the model, I used learning rate of 0.001, upto 200 epochs and bach size of 256.

#### 4. Describe the approach taken for finding a solution and getting the validation set accuracy to be at least 0.93. Include in the discussion the results on the training, validation and test sets and where in the code these were calculated. Your approach may have been an iterative process, in which case, outline the steps you took to get to the final solution and why you chose those steps. Perhaps your solution involved an already well known implementation or architecture. In this case, discuss why you think the architecture is suitable for the current problem.

The final model results are show as following:

Old:
![alt text][image3]

* training set accuracy is over 95%
* validation set accuracy of 85.0% 
* test set accuracy of 84.5%
 
 New:
![alt text][image9]

* validation set accuracy of 98% 
* test set accuracy of 96%

### Test a Model on New Images

#### 1. Choose five German traffic signs found on the web and provide them in the report. For each image, discuss what quality or qualities might be difficult to classify.

Here are five German traffic signs that I found on the web:

![alt text][image4] 


#### 2. Discuss the model's predictions on these new traffic signs and compare the results to predicting on the test set. At a minimum, discuss what the predictions were, the accuracy on these new predictions, and compare the accuracy to the accuracy on the test set (OPTIONAL: Discuss the results in more detail as described in the "Stand Out Suggestions" part of the rubric).

Here are the results of the prediction:

| Image			        |     Prediction	        					|
|:---------------------:|:---------------------------------------------:| 
|  Priority road       		|  Priority road    									|
|  Right-of-way at the next intersection       		|  Right-of-way at the next intersection    									|
|  Stop       		|  Stop    									|
|  No entry       		|  No entry    									|
|  Road work       		|  Road work    									|

The model was able to correctly guess 5 of the 5 traffic signs, which gives an accuracy of 100%. 

#### 3. Describe how certain the model is when predicting on each of the five new images by looking at the softmax probabilities for each prediction. Provide the top 5 softmax probabilities for each image along with the sign type of each probability. (OPTIONAL: as described in the "Stand Out Suggestions" part of the rubric, visualizations can also be provided such as bar charts)

The code for making predictions on my final model is located in the 17th cell of the Ipython notebook.

The top five soft max probabilities of each image are as following:

Old:
![alt text][image5] 

New:
![alt text][image10] 

### (Optional) Visualizing the Neural Network (See Step 4 of the Ipython notebook for more details)
#### 1. Discuss the visual output of your trained network's feature maps. What characteristics did the neural network use to make classifications?

![alt text][image6] 
![alt text][image7] 


# By revisit the project and three major modification is done:

## 1. Improve the data pre-processing: a. correct the program typos in the image flipping function; b. add more data augment methods; c. balance the data set of different classes.

## 2. Change the LeNet input from single color image to RGB image. This migh be the major reason of low accuracy in previous version. 

## 3. Reduce the number of both the learning rate and the epoch. 
