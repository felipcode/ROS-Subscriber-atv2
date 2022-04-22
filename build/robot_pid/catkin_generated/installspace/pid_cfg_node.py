# 2) Um robô tem suas variáveis de controle PID estáticas no código. 
# Crie um programa que faça a alteração do PID de forma dinâmica 
# pelos tópicos robot/control/p, robot/control/i e robot/control/d. 
# Use o tipo de mensagem std_msgs/Float32.


#!/usr/bin/en python3

import rospy
from std_msgs.msg import Float32


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def pid_cfg_node():
    rospy.init_node('pid_cfg_node', anonymous = False) # node handle


    while not rospy.is_shutdown():
        pass




if __name__ == '__main__':
    try:
        pid_cfg_node()
        pass
    except:
        pass


