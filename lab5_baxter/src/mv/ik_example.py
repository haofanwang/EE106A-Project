#!/usr/bin/env python
import rospy
from moveit_msgs.srv import GetPositionIK, GetPositionIKRequest, GetPositionIKResponse
from geometry_msgs.msg import PoseStamped
from moveit_commander import MoveGroupCommander
import numpy as np
from numpy import linalg
from baxter_interface import gripper as robot_gripper
# from listener import dic

def main():
    #Wait for the IK service to become available
    rospy.wait_for_service('compute_ik')
    rospy.init_node('service_query')
    
    #Create the function used to call the service
    compute_ik = rospy.ServiceProxy('compute_ik', GetPositionIK)
    right_gripper = robot_gripper.Gripper('right')
    
    global step 
    step = 0
    mov1 = [-0.046, 0.078, 0.259,-0.162, 0.201, -0.704, 0.662]
    mov2 = [-0.046, 0.078, 0.359,-0.162, 0.201, -0.704, 0.662]
    # mov3 = [0.758, -0.235, -0.258,0.061, 0.998, -0.012, 0.013]
    # mov4 = [0.758, -0.235, -0.158,-0.025, -0.003, -0.740, 0.012]
    # mov5 = [0.747, -0.241, -0.172,0.061, 0.998, -0.012, 0.013]
    # mov6 = [0.827, -0.261, -0.040,0.998, -0.042, -0.048, -0.010]
    pose = [mov1,mov2]
    while not rospy.is_shutdown():
        #raw_input('Press [ Enter ]: ')
        s = pose[step]
        #Construct the request
        request = GetPositionIKRequest()
        request.ik_request.group_name = "right_arm"
        request.ik_request.ik_link_name = "right_wrist"
        request.ik_request.attempts = 20
        request.ik_request.pose_stamped.header.frame_id = "left_hand_camera"#update'base'
        
        #Set the desired orientation for the end effector HERE
        request.ik_request.pose_stamped.pose.position.x = s[0]
        request.ik_request.pose_stamped.pose.position.y = s[1]
        request.ik_request.pose_stamped.pose.position.z = s[2]        
        request.ik_request.pose_stamped.pose.orientation.x = s[3]
        request.ik_request.pose_stamped.pose.orientation.y = s[4]
        request.ik_request.pose_stamped.pose.orientation.z = s[5]
        request.ik_request.pose_stamped.pose.orientation.w = s[6]
        
        try:
            #Send the request to the service
            response = compute_ik(request)
            
            #Print the response HERE
            print(response)
            group = MoveGroupCommander("right_arm")

            # Setting position and orientation target
            group.set_pose_target(request.ik_request.pose_stamped)

            # TRY THIS
            # Setting just the position without specifying the orientation
            ###group.set_position_target([0.5, 0.5, 0.0])

            # Plan IK and execute
            group.go()
            if step==1:
               #right_gripper.calibrate()
               right_gripper.close()
            if step==4:
               right_gripper.open()
            
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e

        step += 1

#Python's syntax for a main() method
if __name__ == '__main__':
      main()

