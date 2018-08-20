## Writeup Template

### You can use this file as a template for your writeup if you want to submit it as a markdown file, but feel free to use some other method and submit a pdf if you prefer.

---

**Advanced Lane Finding Project**

The goals / steps of this project are the following:

* Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
* Apply a distortion correction to raw images.
* Use color transforms, gradients, etc., to create a thresholded binary image.
* Apply a perspective transform to rectify binary image ("birds-eye view").
* Detect lane pixels and fit to find the lane boundary.
* Determine the curvature of the lane and vehicle position with respect to center.
* Warp the detected lane boundaries back onto the original image.
* Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.

[//]: # (Image References)

[image1]: ./output_images/chessboards.png "Chessboard"
[image2]: ./output_images/chessboardcalibration.png "ChessboardCalibaration"
[image3]: ./output_images/test_image_calib.png "TestImageCalibration"
[image4]: ./output_images/test_image_unwarp.png "TestImageUnwarp"
[image5]: ./output_images/test_image_colospace.png "TestImageColorSpace"
[image6]: ./output_images/test_image_sobelxy.png "TestImageSobelXY"
[image7]: ./output_images/test_image_sobelmag.png "TestImageSobelMagnitude"
[image8]: ./output_images/test_image_sobeldir.png "TestImageSobelDirection"
[image9]: ./output_images/test_image_combine_sobelmagdir.png "TestImageSobelMagnitudeDirection"
[image10]: ./output_images/test_image_hlssch.png "TestImageHLSSChannel"
[image11]: ./output_images/test_image_hlslch.png "TestImageHLSLChannel"
[image12]: ./output_images/test_image_labch.png "TestImageLABChannel"
[image13]: ./output_images/test_image_lanefind.png "TestImageFindLane"
[image14]: ./output_images/test_image_hist.png "TestImageHistgram"
[image15]: ./output_images/test_image_winslide.png "TestImageSlideWindow"
[image16]: ./output_images/test_image_polyfit.png "TestImagePolyFit"
[image17]: ./output_images/test_image_drawlane.png "TestImageDrawLane"
[image18]: ./output_images/test_image_drawpos.png "TestImageDrawPosition"
[video1]: ./output_videos/project_video_out.mp4 "Video"
[video2]: ./output_videos/challenge_video_out.mp4 "Video"
[video3]: ./output_videos/harder_challenge_video_out.mp4 "Video"


## [Rubric](https://review.udacity.com/#!/rubrics/571/view) Points

### Here I will consider the rubric points individually and describe how I addressed each point in my implementation.  

---

### Writeup / README

#### 1. Provide a Writeup / README that includes all the rubric points and how you addressed each one.  You can submit your writeup as markdown or pdf.  [Here](https://github.com/udacity/CarND-Advanced-Lane-Lines/blob/master/writeup_template.md) is a template writeup for this project you can use as a guide and a starting point.  

You're reading it!

### Camera Calibration

#### 1. Briefly state how you computed the camera matrix and distortion coefficients. Provide an example of a distortion corrected calibration image.

The code for this step is contained in the first code cell of the IPython notebook located in "./Advance_Car_Lane_Finding.ipynb".

I start by preparing "object points", which will be the (x, y, z) coordinates of the chessboard corners in the world. Here I am assuming the chessboard is fixed on the (x, y) plane at z=0, such that the object points are the same for each calibration image.  Thus, `objp` is just a replicated array of coordinates, and `objpoints` will be appended with a copy of it every time I successfully detect all chessboard corners in a test image.  `imgpoints` will be appended with the (x, y) pixel position of each of the corners in the image plane with each successful chessboard detection.  

I then used the output `objpoints` and `imgpoints` to compute the camera calibration and distortion coefficients using the `cv2.calibrateCamera()` function.  I applied this distortion correction to the test image using the `cv2.undistort()` function and obtained this result: 

![alt text][image1]

### Pipeline (single images)

#### 1. Provide an example of a distortion-corrected image.

To demonstrate this step, I will describe how I apply the distortion correction to the chess board image like this one:

![alt text][image2]

and one of the test images like this one:

![alt text][image3]

#### 2. Describe how (and identify where in your code) you performed a perspective transform and provide an example of a transformed image.

The code for my perspective transform includes a function called `unwarp()`.  The `unwarp()` function takes as inputs an image (`img`), as well as source (`src`) and destination (`dst`) points.  I chose the hardcode the source and destination points in the following manner:

```python
src = np.float32([(580,470),
                  (730,470), 
                  (290,690), 
                  (1150,690)])
offset = 400
dst = np.float32([(offset, 0),
                  (w-offset, 0), 
                  (offset, h), 
                  (w-offset, h)])
```

This resulted in the following source and destination points:

| Source        | Destination   | 
|:-------------:|:-------------:| 
| 585, 470      | 400, 0        | 
| 730, 470      | 880, 0        |
| 290, 690      | 400, 720      |
| 1150, 690     | 880, 720      |

I verified that my perspective transform was working as expected by drawing the `src` and `dst` points onto a test image and its warped counterpart to verify that the lines appear parallel in the warped image.

![alt text][image4]

#### 3. Describe how (and identify where in your code) you used color transforms, gradients or other methods to create a thresholded binary image.  Provide an example of a binary image result.

I used a combination of color and gradient thresholds to generate a binary image for the unwarped image from last step. 

Firstly, I explore the color space of different color transform such as RGB, HSV and LAB channels:

![alt text][image5]

By adding minimum and maximum threshold (0~255) to the value of the binary image, I explore the thresholded binary image for different filters:

    1. Sobel X and Y:

![alt text][image6]

    2. Sobel Magnitude:

![alt text][image7]

    3. Sobel Direction:

![alt text][image8]

    4. Combined Sobel Magnitude and Direction:

![alt text][image9]

By adding minimum and maximum threshold (0~255) to the value of the binary image, I also explore the shresholded binary image for different color space:

    1. HLS S-Channel:
    
![alt text][image10]

    2. HLS L-Channel:
    
![alt text][image11]

    3. LAB Channels:    

![alt text][image12]

By combine specific thresholded binary image, e.g. merge two binary image with those with 1 value from both, the lane marks are extracted from the test images displaying as follow:

![alt text][image13]

The Histgram of thresholded binary image across the X,Y-Axis is shown

![alt text][image14]

#### 4. Describe how (and identify where in your code) you identified lane-line pixels and fit their positions with a polynomial?

Then, based on the Histgram result, the lane-line pixels are found through a sliding window across the image. After that the lane lines are fitted with a 2nd order linear polynomial as shown:

![alt text][image15]

By fitting the lane-line, the lanes are shown as follow:

![alt text][image16]

#### 5. Describe how (and identify where in your code) you calculated the radius of curvature of the lane and the position of the vehicle with respect to center.

I did this in lines through function `measure_curvature_center_dist()`. The idea is to find the center of both left and right lane line and calculate which is used to derive the center of the road. The car position is supposed to be the center of the image. By subtracting the car position with the road center. The bias of the trojectory is calculated.

#### 6. Provide an example image of your result plotted back down onto the road such that the lane area is identified clearly.

The lane area is draw through function `draw_lane()`. Here is an example of the result on a test image:

![alt text][image17]

The curvature and bias of care are displayed through function `draw_data()`.  Here is an example of the result on a test image:

![alt text][image18]

---

### Pipeline (video)

#### 1. Provide a link to your final video output.  Your pipeline should perform reasonably well on the entire project video (wobbly lines are ok but no catastrophic failures that would cause the car to drive off the road!).

Here's a [link to the project video result](./output_videos/project_video_out.mp4 "project")

Here's a [link to challenge video result](./output_videos/challenge_video_out.mp4 "challenge")

Here's a [link to harder challenge video result](./output_videos/harder_challenge_video_out.mp4 "harder")

---

### Discussion

#### 1. Briefly discuss any problems / issues you faced in your implementation of this project.  Where will your pipeline likely fail?  What could you do to make it more robust?

The pipeline works OK for the project video as the enviroment is relative simpler than the other two. The pipeline does not work very well on the challenge and harder challenge for the reasons I thought as bellow:

    1. The sun light is not consistent. There are light changes and shadows which does torlerant the loose threshold as it works in the project video.
    
    2. The road apperance is not consistent. There are different colors, patch line, turns. The different color and patch line effect on the line finding in the image. The turn of the road introduce the dead angle of camera where the lane mark is not visible. 
    
    3. The ROI zone is not consistent. In some video frames, the ROI does not cover the real intereting area.
    
Firstly, I tried to fine tune the threshold according to those frames that hard to identify the lane. Second, I tried to tuning the ROI and warp source & destination. These two steps works for the project video. However, it still does not work for the challenge and harder challenge video. I even try to do Histgram equalization of the image first but it needs more tuing of the threshold of bianry images. The ways I think might improve this, would be filtering the lane identification across several frames and doing a adaptive parameterized thresholding. As the road turn, it might worth to try to use higher order fitting parameters. 
