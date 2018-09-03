# Vehicle Detection
[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)


In this project, your goal is to write a software pipeline to detect vehicles in a video (start with the test_video.mp4 and later implement on full project_video.mp4), but the main output or product we want you to create is a detailed writeup of the project.  Check out the [writeup template](https://github.com/udacity/CarND-Vehicle-Detection/blob/master/writeup_template.md) for this project and use it as a starting point for creating your own writeup.  

Creating a great writeup:
---
A great writeup should include the rubric points as well as your description of how you addressed each point.  You should include a detailed description of the code used in each step (with line-number references and code snippets where necessary), and links to other supporting documents or external references.  You should include images in your writeup to demonstrate how your code works with examples.  

All that said, please be concise!  We're not looking for you to write a book here, just a brief description of how you passed each rubric point, and references to the relevant code :). 

You can submit your writeup in markdown or use another method and submit a pdf instead.

The Project
---

The goals / steps of this project are the following:

* Perform a Histogram of Oriented Gradients (HOG) feature extraction on a labeled training set of images and train a classifier Linear SVM classifier
* Optionally, you can also apply a color transform and append binned color features, as well as histograms of color, to your HOG feature vector. 
* Note: for those first two steps don't forget to normalize your features and randomize a selection for training and testing.
* Implement a sliding-window technique and use your trained classifier to search for vehicles in images.
* Run your pipeline on a video stream (start with the test_video.mp4 and later implement on full project_video.mp4) and create a heat map of recurring detections frame by frame to reject outliers and follow detected vehicles.
* Estimate a bounding box for vehicles detected.

Here are links to the labeled data for [vehicle](https://s3.amazonaws.com/udacity-sdc/Vehicle_Tracking/vehicles.zip) and [non-vehicle](https://s3.amazonaws.com/udacity-sdc/Vehicle_Tracking/non-vehicles.zip) examples to train your classifier.  These example images come from a combination of the [GTI vehicle image database](http://www.gti.ssr.upm.es/data/Vehicle_database.html), the [KITTI vision benchmark suite](http://www.cvlibs.net/datasets/kitti/), and examples extracted from the project video itself.   You are welcome and encouraged to take advantage of the recently released [Udacity labeled dataset](https://github.com/udacity/self-driving-car/tree/master/annotations) to augment your training data.  

Some example images for testing your pipeline on single frames are located in the `test_images` folder.  To help the reviewer examine your work, please save examples of the output from each stage of your pipeline in the folder called `ouput_images`, and include them in your writeup for the project by describing what each image shows.    The video called `project_video.mp4` is the video your pipeline should work well on.  

**As an optional challenge** Once you have a working pipeline for vehicle detection, add in your lane-finding algorithm from the last project to do simultaneous lane-finding and vehicle detection!

**If you're feeling ambitious** (also totally optional though), don't stop there!  We encourage you to go out and take video of your own, and show us how you would implement this project on a new video!

## How to write a README
A well written README file can enhance your project and portfolio.  Develop your abilities to create professional README files by completing [this free course](https://www.udacity.com/course/writing-readmes--ud777).

[//]: # (Image References)

[image1]: ./output_images/data_visualization.png "DataVisual"
[image2]: ./output_images/hog_visualization.png "HOGVisual"
[image3]: ./output_images/color_hist_vis.png "ColorHist"
[image4]: ./output_images/bin_spatial1.png "carphoto"
[image5]: ./output_images/bin_spatial2.png "SpatialHist1"
[image6]: ./output_images/bin_spatial3.png "SpatialHist2"
[image7]: ./output_images/sliding_windows.png "Slidingwindows"
[image8]: ./output_images/windows.png "Imagetests"
[image9]: ./output_images/heat_map1.png "Heatmapslidingwindows"
[video1]: ./output_videos/test_video_out.mp4 "Video"
[video2]: ./output_videos/project_video_out.mp4 "Video"

# Project Steps: 

## 1. Lane finding using functions from last project. 

## 2. Car detection

### a. The training data is loaded from give zip files "vehicle.zip" and "non-vehicle.zip". The samples of training data are shown as follow:

![alt text][image1]

### b. In order to detect the car, the feature of the image is extracted. Here the HOG based feature extraction with hog function in skimage library. The HOG based extracted features of different color channels are shown as follow:

![alt text][image2]
![alt text][image3]

### c. Instead of HOG based feature extraction, it is also potential to use the histgram of the color space information for different color space transformation. The color space extraced features are shown as follow:

![alt text][image4]
![alt text][image5]
![alt text][image6]

### d. By using the extracted features from both vehicle image and non-vehicle image, the Linear Support Vector Machine based Classifier (SVC) can be trained using pre-labeled tags. With sklearn library, this could be easily achieved through tuning different parameters of Support Vector Machine. The accuracy around 97% is achieved in this project by using part of the training data as test data. 

### e. After training the classifier, the sliding windows based object matching through the image is implemented. By adopting different ROI and scaling of the sliding window, the vehicles can be identified using the pre-trained SVC. The results on the test images are shown as follow:

![alt text][image7]
![alt text][image8]

### f. By using a threshold based heat map transformation, multiple overlapped sliding windows can be combined into a single one that represents a vehicle only. The process is shown as follow:

![alt text][image9]

### g. So far the frame processing pipeline of video is very clear. With pre-trained SVC, firstly using sliding windows to identify possible windows as a vehicle; secondly, using the threshold based heat map techinque to combine multiple overlapped windows; thirdly, apply the combined windows on to original video frame as the bound of a vehicle. If applying the windows on a frame with pre-detected lane, both lane and vehicle detection can be illustrated in a same video. 

Here's a [link to the project video result](./output_videos/project_video_out.mp4 "project")

## 3. Discussion

### a. The training data space could be improved using large training benchmark database. 
### b. The SVC based method could be replaced with other ML or DL algorithms, such as the method for traffic sign classifier. 
### c. The result sometimes cannot detect the vehicle very well due to: only partial vehicle appear; similar color space to the enviroment; ROI restriction; and overlapped multiple vehicle in frame. 
