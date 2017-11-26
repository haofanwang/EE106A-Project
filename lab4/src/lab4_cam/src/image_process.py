#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from lab4_cam.srv import ImageSrv, ImageSrvResponse
import cv2, time, sys
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
from numpy.linalg import *
import math


# Nominal length of a tile side
TILE_LENGTH = 30.48 #cm

# Helper function to check computed homography
# This will draw dots in a grid by projecting x,y coordinates
# of tile corners to u,v image coordinates
def check_homography(image, H, nx, ny, length=TILE_LENGTH):
  # H should be a 3x3 numpy.array
  # nx is the number of tiles in the x direction
  # ny is the number of tiles in the y direction
  # length is the length of one side of a tile
  # image is an image array
  for i in range(nx+1):
    for j in range(ny+1):
      xbar = np.array([[i*length],[j*length],[1]])
      ubar = np.dot(H,xbar).T[0]
      u = np.int(ubar[0]/ubar[2])
      v = np.int(ubar[1]/ubar[2])
      print 'Dot location: ' + str((u,v))
      cv2.circle(image, (u,v), 5, 0, -1)
  cv2.imshow('Check Homography', image)

# Create a CvBridge to convert ROS messages to OpenCV images
bridge = CvBridge()

# Converts a ROS Image message to a NumPy array to be displayed by OpenCV
def ros_to_np_img(ros_img_msg):
  return np.array(bridge.imgmsg_to_cv2(ros_img_msg,'bgr8'))

# Define the total number of clicks we are expecting (4 corners)
TOT_CLICKS = 4

if __name__ == '__main__':
  
  # Waits for the image service to become available
  rospy.wait_for_service('last_image')
  
  # Initializes the image processing node
  rospy.init_node('image_processing_node')
  
  # Creates a function used to call the 
  # image capture service: ImageSrv is the service type
  last_image_service = rospy.ServiceProxy('last_image', ImageSrv)

  # Create an empty list to hold the coordinates of the clicked points
  points = []

  # Callback function for 'cv2.SetMouseCallback' adds a clicked point to the
  # list 'points'
  def on_mouse_click(event,x,y,flag,param):
    if(event == cv2.EVENT_LBUTTONUP):
      point = (x,y)
      print "Point Captured: " + str(point)
      points.append(point)

  while not rospy.is_shutdown():
    try:
      # Waits for a key input to continue
      raw_input('Press enter to capture an image:')
    except KeyboardInterrupt:
      print 'Break from raw_input'
      break
    
    try:
      # Request the last image from the image service
      # And extract the ROS Image from the ImageSrv service
      # Remember that ImageSrv.image_data was
      # defined to be of type sensor_msgs.msg.Image
      ros_img_msg = last_image_service().image_data

      # Convert the ROS message to a NumPy image
      np_image = ros_to_np_img(ros_img_msg)

      # Display the CV Image
      cv2.imshow("CV Image", np_image)

      # Tell OpenCV that it should call 'on_mouse_click' when the user
      # clicks the window. This will add clicked points to our list
      cv2.setMouseCallback("CV Image", on_mouse_click, param=1)

      # Zero out list each time we have a new image
      points = []

      # Loop until the user has clicked enough points
      while len(points) < TOT_CLICKS:
        if rospy.is_shutdown():
          raise KeyboardInterrupt
        cv2.waitKey(10)

      # Convert the Python list of points to a NumPy array of the form
      #   | u1 u2 u3 u4 |
      #   | v1 v2 v3 v4 |
      uv = np.array(points).T

# === YOUR CODE HERE ===========================================================
      
      # This is placeholder code that will draw a 4 by 3 grid in the corner of
      # the image
      nx = 3#3
      ny = 3#4
      H = np.eye(3)
      x1=0
      y1=0
      x2=0
      y2=TILE_LENGTH*ny
      x3=TILE_LENGTH*nx
      y3=TILE_LENGTH*ny
      x4=TILE_LENGTH*nx
      y4=0
      A=np.array([
                  [x1,y1,1,0,0,0,-uv[0][0]*x1,-uv[0][0]*y1],
                  [0,0,0,x1,y1,1,-uv[1][0]*x1,-uv[1][0]*y1],
                  [x2,y2,1,0,0,0,-uv[0][1]*x2,-uv[0][1]*y2],
                  [0,0,0,x2,y2,1,-uv[1][1]*x2,-uv[1][1]*y2],
                  [x3,y3,1,0,0,0,-uv[0][2]*x3,-uv[0][2]*y3],
                  [0,0,0,x3,y3,1,-uv[1][2]*x3,-uv[1][2]*y3],
                  [x4,y4,1,0,0,0,-uv[0][3]*x4,-uv[0][3]*y4],
                  [0,0,0,x4,y4,1,-uv[1][3]*x4,-uv[1][3]*y4]
                 ])
      b=np.array([
                  [uv[0][0]],
                  [uv[1][0]],
                  [uv[0][1]],
                  [uv[1][1]],
                  [uv[0][2]],
                  [uv[1][2]],
                  [uv[0][3]],
                  [uv[1][3]]
                 ])
      
      #x=np.dot(inv(A),b)
      x=inv(A).dot(b)
      
      H[0][0]=x[0]
      H[0][1]=x[1]
      H[0][2]=x[2]
      H[1][0]=x[3]
      H[1][1]=x[4]
      H[1][2]=x[5]
      H[2][0]=x[6]
      H[2][1]=x[7]

      Q=inv(H)
      

# ==============================================================================
      
      # Check the produced homography matrix
      check_homography(np_image, H, nx, ny)

      #####our code
      '''coord=uv
      newx1=(Q[0][0]*coord[0][4]+Q[0][1]*coord[1][4]+Q[0][2])/(Q[2][0]*coord[0][4]+Q[2][1]*coord[1][4]+Q[2][2])
      
      newy1=(Q[1][0]*coord[0][4]+Q[1][1]*coord[1][4]+Q[1][2])/(Q[2][0]*coord[0][4]+Q[2][1]*coord[1][4]+Q[2][2])
      
      newx2=(Q[0][0]*coord[0][5]+Q[0][1]*coord[1][5]+Q[0][2])/(Q[2][0]*coord[0][5]+Q[2][1]*coord[1][5]+Q[2][2])
      
      newy2=(Q[1][0]*coord[0][5]+Q[1][1]*coord[1][5]+Q[1][2])/(Q[2][0]*coord[0][5]+Q[2][1]*coord[1][5]+Q[2][2])
 
      val1=math.pow(newx1-newx2,2)
      val2=math.pow(newy1-newy2,2)
      val3=val1+val2
      dis=math.sqrt(val3)
      print dis'''
      for x0 in x:
      	print x0


      # Loop until the user presses a key
      key = -1
      while key == -1:
        if rospy.is_shutdown():
          raise KeyboardInterrupt
        key = cv2.waitKey(100)
      
      # When done, get rid of windows and start over
      # cv2.destroyAllWindows()

    except KeyboardInterrupt:
      print 'Keyboard Interrupt, exiting'
      break

    # Catch if anything went wrong with the Image Service
    except rospy.ServiceException, e:
      print "image_process: Service call failed: %s"%e
    
  cv2.destroyAllWindows()

