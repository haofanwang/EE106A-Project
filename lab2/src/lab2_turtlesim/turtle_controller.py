#!/usr/bin/env python
#The line above tells Linux that this file is a Python script,
#and that the OS should use the Python interpreter in /usr/bin/env
#to run it. Don't forget to use "chmod +x [filename]" to make
#this script executable.

#Import the rospy package. For an import to work, it must be specified
#in both the package manifest AND the Python file in which it is used.
import rospy

#Import the String message type  from the /msg directory of
#the std_msgs package.
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import sys

#Define the method which contains the main functionality of the node.
def talker():

  #Run this program as a new node in the ROS computation graph 
  #called /talker.
  rospy.init_node('talker', anonymous=True)

  #Create an instance of the rospy.Publisher object which we can 
  #use to publish messages to a topic. This publisher publishes 
  
  name = sys.argv[1]
  path = '/'+name+'/cmd_vel'
  pub = rospy.Publisher(path, Twist, queue_size=10)
  #messages of type std_msgs/String to the topic /chatter_talk
  #if sys.argv[1] == 'turtle1' :
  #  pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
  #if sys.argv[1] == 'newturtle' :
  #  pub = rospy.Publisher('/newturtle/cmd_vel', Twist, queue_size=10)
  # Create a timer object that will sleep long enough to result in
  # a 10Hz publishing rate
  r = rospy.Rate(10) # 10hz

  speed = 1
  # Loop until the node is killed with Ctrl-C
  while not rospy.is_shutdown():
    # Construct a string that we want to publish
    # (In Python, the "%" operator functions similarly
    #  to sprintf in C or MATLAB)
    ##pub_string = "hello world %s" % (rospy.get_time())
    
    key = raw_input()
    pub_vel = Twist()
    
    if key == 'w':
       pub_vel.linear.x = speed
    elif key == 's':
       pub_vel.linear.x = -speed
    elif key == 'a':
       pub_vel.angular.z = 3
    elif key == 'd':
       pub_vel.angular.z = -3

    if key == 'f':
       speed = speed + 1
    if key == 'p':
        if speed>0:
           speed = speed - 1
        elif speed<0:
           speed = speed + 1
        else:
           speed = 0


    # Publish our string to the 'chatter_talk' topic
    pub.publish(pub_vel)
    
    # Use our rate object to sleep until it is time to publish again
    r.sleep()
      
# This is Python's sytax for a main() method, which is run by default
# when exectued in the shell
if __name__ == '__main__':
  # Check if the node has received a signal to shut down
  # If not, run the talker method
  try:
    talker()
  except rospy.ROSInterruptException: pass
