# 2) Um robô tem suas variáveis de controle PID estáticas no código. 
# Crie um programa que faça a alteração do PID de forma dinâmica 
# pelos tópicos robot/control/p, robot/control/i e robot/control/d. 
# Use o tipo de mensagem std_msgs/Float32.


#!/usr/bin/en python3

import rospy
from std_msgs.msg import Float32




class PIDConfig:
    p = 12
    i = 2
    d = 9
    def __init__(self):
        self.p_ = 1
        self.i_ = 1
        self.d_ = 1
        self.subsc_p_ = rospy.Subscriber("robot/control/p", Float32, self.setP_callback, queue_size=10)
        self.subsc_i_ = rospy.Subscriber("robot/control/i", Float32, self.setI_callback, queue_size=10)
        self.subsc_d_ = rospy.Subscriber("robot/control/d", Float32, self.setD_callback, queue_size=10)
        # self.sub_ = rospy.Subscriber("robot/control/p", Float32, self.setX_callback, queue_size=10)
    def setI_callback(self, msg):
        self.i_ = msg.data
        pass
    def setD_callback(self, msg):
        self.d_ = msg.data
        pass
    def setP_callback(self, msg):
        self.p_ = msg.data
        pass




def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def pid_cfg_node():
    rospy.init_node('pid_cfg_node', anonymous = False) # node handle


    while not rospy.is_shutdown():
        pass




if __name__ == '__main__':

    # p = 10
    # i = 1 
    # d = 10

    try:
        #wpid_cfg_node()

        while not rospy.is_shutdown():
            rospy.spin()
            pass

        pass
    except:
        pass


