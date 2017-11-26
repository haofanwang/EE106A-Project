from kin_func_skeleton import *
import numpy as np

g_st_0=np.array([[.0076, -.7040, .7102, 0.7957],
				[.0001, .7102, .7040,0.9965],
				[-1.000, -.0053, .0055, 0.3058],
				[0,0,0,1]])

#print g_st_0
'''
[[ 1.      0.      0.      0.7957]
 [ 0.      1.      0.      0.9965]
 [ 0.      0.      1.      0.3058]
 [ 0.      0.      0.      1.    ]]
'''
w1=np.array([-.0059,.0113,.9999])
w2=np.array([-.7077,.7065,-.0122])
w3 =np.array([.7065,.7077,-.0038])
w4 =np.array([-.7077,.7065,-.0122])
w5 =np.array([.7065,.7077,-.0038])
w6 =np.array([-.7077,.7065,-.0122])
w7 =np.array([.7065,.7077,-.0038])

q1=np.array([.0635,.2598,.1188])
q2 =np.array([.1106,.3116,.3885])
q3 =np.array([.1827,.3838,.3881])
q4 =np.array([.3682,.5684,.3181])
q5 =np.array([.4417,.6420,.3177])
q6 =np.array([.6332,.8337,.3067])
q7 =np.array([.7152,.9158,.3063])

epsilon1=np.hstack((-np.dot(skew_3d(w1),q1),w1))
epsilon2=np.hstack((-np.dot(skew_3d(w2),q2),w2))
epsilon3=np.hstack((-np.dot(skew_3d(w3),q3),w3))
epsilon4=np.hstack((-np.dot(skew_3d(w4),q4),w4))
epsilon5=np.hstack((-np.dot(skew_3d(w5),q5),w5))
epsilon6=np.hstack((-np.dot(skew_3d(w6),q6),w6))
epsilon7=np.hstack((-np.dot(skew_3d(w7),q7),w7))

xi=np.vstack((epsilon1,epsilon2))
xi=np.vstack((xi,epsilon3))
xi=np.vstack((xi,epsilon4))
xi=np.vstack((xi,epsilon5))
xi=np.vstack((xi,epsilon6))
xi=np.vstack((xi,epsilon7))

xi=np.transpose(xi)

'''
print xi.shape
(6, 7)
'''


def g_st_theta(theta):
    g_st_theta=np.dot(prod_exp(xi, theta),g_st_0)
    return g_st_theta

matrix = g_st_theta([ .29218333042203637, -1.5761832109443277, -0.6546936536965593, 1.5754983788770098, -0.003280152190219542, 1.5703673543491026, 0.4228980909423929])
print(str(matrix))

'''
print g_st_theta(np.array([1,2,3,4,5,6,7])).shape
(4, 4)
'''
