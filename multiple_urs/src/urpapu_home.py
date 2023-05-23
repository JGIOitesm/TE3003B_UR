#!/usr/bin/env python

import rospy
import actionlib
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
import numpy as np

def move_robot():
    # Initialize the ROS node
    rospy.init_node("home_robot_papu")

    # Create an action client
    client = actionlib.SimpleActionClient('/urpapu/scaled_pos_joint_traj_controller/follow_joint_trajectory', FollowJointTrajectoryAction)

    # Wait for the action server to become available
    client.wait_for_server()

    # Create a trajectory point
    point = JointTrajectoryPoint()
    point.positions = [0, -np.pi/2, 0, -np.pi/2, 0, 0]  # Fill in the joint positions
    point.time_from_start = rospy.Duration(1.0)  # Set the time from start

    # Create a trajectory
    trajectory = JointTrajectory()
    trajectory.joint_names = ['elbow_joint','shoulder_lift_joint','shoulder_pan_joint','wrist_1_joint','wrist_2_joint','wrist_3_joint']  # Fill in the joint names
    trajectory.points.append(point)

    # Create a goal
    goal = FollowJointTrajectoryGoal()
    goal.trajectory = trajectory

    # Send the goal
    client.send_goal(goal)

    # Wait for the action to complete
    client.wait_for_result()



if __name__ == '__main__':
    try:
        move_robot()
    except rospy.ROSInterruptException:
        pass