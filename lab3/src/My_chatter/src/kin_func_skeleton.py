#!/usr/bin/env python
"""Kinematic function skeleton code for Prelab 3.
Course: EE 106A, Fall 2015
Written by: Aaron Bestick, 9/10/14
Used by: EE106A, 9/11/15

This Python file is a code skeleton for Pre lab 3. You should fill in 
the body of the eight empty methods below so that they implement the kinematic 
functions described in the homework assignment.

When you think you have the methods implemented correctly, you can test your 
code by running "python kin_func_skeleton.py at the command line.

This code requires the NumPy and SciPy libraries. If you don't already have 
these installed on your personal computer, you can use the lab machines or 
the Ubuntu+ROS VM on the course page to complete this portion of the homework.
"""

import numpy as np
import math
import scipy as sp
from scipy import linalg

np.set_printoptions(precision=4,suppress=True)

def skew_3d(omega):
    """
    Converts a rotation vector in 3D to its corresponding skew-symmetric matrix.
    
    Args:
    omega - (3,) ndarray: the rotation vector
    
    Returns:
    omega_hat - (3,3) ndarray: the corresponding skew symmetric matrix
    """
    if not omega.shape == (3,):
        raise TypeError('omega must be a 3-vector')
    
    #YOUR CODE HERE
    omega_hat = np.array([[0,-omega[2],omega[1]],
                         [omega[2],0,-omega[0]],
                         [-omega[1],omega[0],0]])

    return omega_hat

def rotation_2d(theta):
    """
    Computes a 2D rotation matrix given the angle of rotation.
    
    Args:
    theta: the angle of rotation
    
    Returns:
    rot - (2,2) ndarray: the resulting rotation matrix
    """
    
    #YOUR CODE HERE
    rot = np.array([[math.cos(theta),-math.sin(theta)],[math.sin(theta),math.cos(theta)]])

    return rot

def rotation_3d(omega, theta):
    """
    Computes a 3D rotation matrix given a rotation axis and angle of rotation.
    
    Args:
    omega - (3,) ndarray: the axis of rotation
    theta: the angle of rotation
    
    Returns:
    rot - (3,3) ndarray: the resulting rotation matrix
    """
    if not omega.shape == (3,):
        raise TypeError('omega must be a 3-vector')
    
    #YOUR CODE HERE
    I = np.array([[1,0,0],
                  [0,1,0],
                  [0,0,1]])

    w_norm = np.linalg.norm(omega)
    w_hat = skew_3d(omega)
    sin = math.sin(w_norm*theta)
    w_norm2 = w_norm * w_norm
    cos = math.cos(w_norm*theta)
    w_hat2 = np.dot(w_hat,w_hat)      ### Be careful! Not np.dot(w_hat,np.transpose(W_hat))

    rot = I + w_hat * sin / w_norm + w_hat2 * (1-cos) / w_norm2

    return rot

def hat_2d(xi):
    """
    Converts a 2D twist to its corresponding 3x3 matrix representation
    
    Args:
    xi - (3,) ndarray: the 2D twist
    
    Returns:
    xi_hat - (3,3) ndarray: the resulting 3x3 matrix
    """
    if not xi.shape == (3,):
        raise TypeError('omega must be a 3-vector')

    #YOUR CODE HERE

    xi_hat = np.zeros([3,3])
    xi_hat[0][1] = -xi[2]
    xi_hat[0][2] =  xi[0]
    xi_hat[1][0] =  xi[2]
    xi_hat[1][2] =  xi[1]

    return xi_hat

def hat_3d(xi):
    """
    Converts a 3D twist to its corresponding 4x4 matrix representation
    
    Args:
    xi - (6,) ndarray: the 3D twist
    
    Returns:
    xi_hat - (4,4) ndarray: the corresponding 4x4 matrix
    """
    if not xi.shape == (6,):
        raise TypeError('xi must be a 6-vector')

    #YOUR CODE HERE
    xi_hat = np.zeros([4,4])
    xi_hat[0][1] = -xi[5]
    xi_hat[0][2] =  xi[4]
    xi_hat[0][3] =  xi[0]
    xi_hat[1][0] =  xi[5]
    xi_hat[1][2] = -xi[3]
    xi_hat[1][3] =  xi[1]
    xi_hat[2][0] = -xi[4]
    xi_hat[2][1] =  xi[3]
    xi_hat[2][3] =  xi[2]

    return xi_hat

def homog_2d(xi, theta):
    """
    Computes a 3x3 homogeneous transformation matrix given a 2D twist and a
    joint displacement

    Args:
    xi - (3,) ndarray: the 2D twist
    theta: the joint displacement

    Returns:
    g - (3,3) ndarray: the resulting homogeneous transformation matrix
    """
    if not xi.shape == (3,):
        raise TypeError('xi must be a 3-vector')

    #YOUR CODE HERE

    R = np.array([[math.cos(xi[2]*theta),-math.sin(xi[2]*theta)],[math.sin(xi[2]*theta),math.cos(xi[2]*theta)]])

    p1 = np.array([[1-math.cos(xi[2]*theta),math.sin(xi[2]*theta)],[-math.sin(xi[2]*theta),1-math.cos(xi[2]*theta)]])

    p2 = np.array([[0,-1],[1,0]])

    p3 = np.array([[xi[0]/xi[2],xi[1]/xi[2]]])

    p = np.dot(np.dot(p1,p2),p3.T)

    g1 = np.hstack((R,p))
    g2 = np.array([0,0,1])

    g = np.vstack((g1,g2))

    return g

def homog_3d(xi, theta):
    """
    Computes a 4x4 homogeneous transformation matrix given a 3D twist and a 
    joint displacement.
    
    Args:
    xi - (6,) ndarray: the 3D twist
    theta: the joint displacement

    Returns:
    g - (4,4) ndarary: the resulting homogeneous transformation matrix
    """
    if not xi.shape == (6,):
        raise TypeError('xi must be a 6-vector')

    #YOUR CODE HERE
    I = np.array([[1,0,0],
                  [0,1,0],
                  [0,0,1]])

    w = np.array([xi[3],xi[4],xi[5]])
    v = np.array([xi[0],xi[1],xi[2]])

    e_hat = rotation_3d(w,theta)

    w_norm2 = np.linalg.norm(w)*np.linalg.norm(w)

    residue = np.dot((I-e_hat),(np.dot(skew_3d(w),np.array([v]).T)))\
              +np.dot(np.multiply(np.array([w]),np.array([w]).T),np.array([v]).T)*theta ####Be careful,the difference between dot/multiply

    bottom = np.array([0,0,0,1])

    g1 = np.hstack((e_hat,residue/w_norm2))
    g = np.vstack((g1,bottom))

    return g

def prod_exp(xi, theta):
    """
    Computes the product of exponentials for a kinematic chain, given 
    the twists and displacements for each joint.

    Args:
    xi - (6,N) ndarray: the twists for each joint
    theta - (N,) ndarray: the displacement of each joint
    
    Returns:
    g - (4,4) ndarray: the resulting homogeneous transformation matrix
    """
    if not xi.shape[0] == 6:
        raise TypeError('xi must be a 6xN')

    #YOUR CODE HERE
    N = xi.shape[1]
    g = np.array([[1,0,0,0],
                 [0,1,0,0],
                 [0,0,1,0],
                 [0,0,0,1]])

    for i in range(N):
        g = np.dot(g,homog_3d((xi.T)[i],theta[i]))

    return g

#-----------------------------Testing code--------------------------------------
#-------------(you shouldn't need to modify anything below here)----------------

def array_func_test(func_name, args, ret_desired):
    ret_value = func_name(*args)
    if not isinstance(ret_value, np.ndarray):
        print('[FAIL] ' + func_name.__name__ + '() returned something other than a NumPy ndarray')
    elif ret_value.shape != ret_desired.shape:
        print('[FAIL] ' + func_name.__name__ + '() returned an ndarray with incorrect dimensions')
    elif not np.allclose(ret_value, ret_desired, rtol=1e-3):
        print('[FAIL] ' + func_name.__name__ + '() returned an incorrect value')
    else:
        print('[PASS] ' + func_name.__name__ + '() returned the correct value!')

if __name__ == "__main__":
    print('Testing...')

    #Test skew_3d()
    arg1 = np.array([1.0, 2, 3])
    func_args = (arg1,)
    ret_desired = np.array([[ 0., -3.,  2.],
                            [ 3., -0., -1.],
                            [-2.,  1.,  0.]])
    array_func_test(skew_3d, func_args, ret_desired)

    #Test rotation_2d()
    arg1 = 2.658
    func_args = (arg1,)
    ret_desired = np.array([[-0.8853, -0.465 ],
                            [ 0.465 , -0.8853]])
    array_func_test(rotation_2d, func_args, ret_desired)

    #Test rotation_3d()
    arg1 = np.array([2.0, 1, 3])
    arg2 = 0.587
    func_args = (arg1,arg2)
    ret_desired = np.array([[-0.1325, -0.4234,  0.8962],
                            [ 0.8765, -0.4723, -0.0935],
                            [ 0.4629,  0.7731,  0.4337]])
    array_func_test(rotation_3d, func_args, ret_desired)

    #Test hat_2d()
    arg1 = np.array([2.0, 1, 3])
    func_args = (arg1,)
    ret_desired = np.array([[ 0., -3.,  2.],
                            [ 3.,  0.,  1.],
                            [ 0.,  0.,  0.]])
    array_func_test(hat_2d, func_args, ret_desired)

    #Test hat_3d()
    arg1 = np.array([2.0, 1, 3, 5, 4, 2])
    func_args = (arg1,)
    ret_desired = np.array([[ 0., -2.,  4.,  2.],
                            [ 2., -0., -5.,  1.],
                            [-4.,  5.,  0.,  3.],
                            [ 0.,  0.,  0.,  0.]])
    array_func_test(hat_3d, func_args, ret_desired)

    #Test homog_2d()
    arg1 = np.array([2.0, 1, 3])
    arg2 = 0.658
    func_args = (arg1,arg2)
    ret_desired = np.array([[-0.3924, -0.9198,  0.1491],
                            [ 0.9198, -0.3924,  1.2348],
                            [ 0.    ,  0.    ,  1.    ]])
    array_func_test(homog_2d, func_args, ret_desired)

    #Test homog_3d()
    arg1 = np.array([2.0, 1, 3, 5, 4, 2])
    arg2 = 0.658
    func_args = (arg1,arg2)
    ret_desired = np.array([[ 0.4249,  0.8601, -0.2824,  1.7814],
                            [ 0.2901,  0.1661,  0.9425,  0.9643],
                            [ 0.8575, -0.4824, -0.179 ,  0.1978],
                            [ 0.    ,  0.    ,  0.    ,  1.    ]])
    array_func_test(homog_3d, func_args, ret_desired)

    #Test prod_exp()
    arg1 = np.array([[2.0, 1, 3, 5, 4, 6], [5, 3, 1, 1, 3, 2], [1, 3, 4, 5, 2, 4]]).T
    arg2 = np.array([0.658, 0.234, 1.345])
    func_args = (arg1,arg2)
    ret_desired = np.array([[ 0.4392,  0.4998,  0.7466,  7.6936],
                            [ 0.6599, -0.7434,  0.1095,  2.8849],
                            [ 0.6097,  0.4446, -0.6562,  3.3598],
                            [ 0.    ,  0.    ,  0.    ,  1.    ]])
    array_func_test(prod_exp, func_args, ret_desired)

    print('Done!')
