# **Finding Lane Lines on the Road** 

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report

[//]: # (Image References)

[image1]: ./examples/grayscale.jpg "Grayscale"

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of 5 steps:

Firstly, the specific color is masked on video frame, in this cases it's about white and yellow lane mark. This helps highlight the specific color on image allowing easier line identification with interferences such as shadow. 

[//]: # (Image References)

[image1]: ./result/HLS.jpg "HLS"
[image2]: ./result/HSV.jpg "HSV"

Secondly, the image is transformed into gray scale. This is a standard procedure to reduce the processing pixel dimension from 3D BRG to 2D gray. Instead of repesenting the pixel of 24 bits where 8 bits for each basical color from 0 to 255, 8 bits is used to represent the gray scale from 0 to 255. 

Thirdly, the Gaussion blur is appied to the image to smooth the value between pixels. For gray scale image, it is a 2D filter that commonly used for reducing the level of noise in image before edge detection.

Fourthly, the Canny edge deteciton is applied to the image and returns the edge only image. The principle is to calculate the gradient along all pixel. If there is a large change in term of gradient, it means there is a significant color change that indicates a edge. 

Fifthly, the image is masked with interesting region only. It artificially regulate a area only  used for further processing. This is to remove unnecessary computational effort since the lane mark is normally appear infornt of the vehicle as a trapezoidal shape to the driver. 

Sixthly, the edge only image with lines is transfomed into Hough space that representing those straight lines with gradient and intercept instead of axis point. Furthermore, the gradient and intercept can be transformed into a distance and an angle. The distance is the length from the origin to the closest point on the straight line while the angle represents the slope between the x axis and the line connecting the origin with that closest point (according to wikipedia). This is very useful as it removes all the curves edges and replaces them with straight line, even very short straight lines. At this point we shall be able to identify the lane but the notations are not continous due to the nature of lane mark. 

Seventhly, the average slope and intercept of all the straight lines are calculated. Notice that since there is normally two lane mark, left and right, the positive value usually indicates the left lane slope while the negative value indicatates the right lane slope. This is to prepare the parameter to draw either left or right lane in two straight lines. 

Eightly, the left and right lanes are drawed and notated on to the original image frame. At this point the goal of the project is achieved. In terms of the modification of draw_line function, I didn't do any modification but I use the weighted_img() functio after the lane detection. At that stage, I combine the orignial video frame with anotated image so that the anotated lane line is merged into the orignal image semi-transparently. 

Ninethly, show the video frame or save to file. 

### 2. Identify potential shortcomings with your current pipeline

There might be two shortcomings in current pipeline:

A. The region of interest pipeline later than edge detection which is increase the computational effort. If we resize the image with region of interest, it might save some computational cost. 

B. The current pipeline is highly dependent on the parameters of color mask low/high range, region of interest and hough transformation. These are handcraft parameters might not adapt to other scenarios. 

### 3. Suggest possible improvements to your pipeline

A. Take masking region of interest in advance.

B. Find a way to make parameters adaptive. I don't have a clue yet. 
