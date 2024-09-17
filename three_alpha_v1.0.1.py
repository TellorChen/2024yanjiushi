# import RPi.GPIO as GPIO
import time
import cv2


class StepperMotorController:
    def __init__(self, step_pin, dir_pin, enable_pin):
        # 在实际应用中，这些引脚会被用来控制步进电机
        # 但在这里，我们只是模拟它们
        self.step_pin = step_pin
        self.dir_pin = dir_pin
        self.enable_pin = enable_pin

    def move(self, steps):
        # GPIO.output(step_pin, GPIO.HIGH)
        time.sleep(steps)
        # GPIO.output(step_pin,GPIO.LOW)


'''
xzhengfu = +
yxhengfu = +`

xmotol = StepperMotorController(4,5,6)
ymotol = StepperMotorController(1,2,3)

xmotol.move(0) #转为初始值
ymotol.move(0) #转为初始值

while True:
    GPIO.setmode(GPIO.BCM)
    GPIO.output(step_pin, GPIO.HIGH)#稍弱

    wenzi = cv2.chaxun(xxx)#假设它为list


    GPIO.output(step_pin, GPIO.LOW)

    if wenzi == None:
        cotinue
    else:
        dian = cv2.chaxun(xxx)#假设它为list

        if int(wenzi[0]) == int(dian[0]) and int(wenzi[1]) == int(dian[1]):
            GPIO.output(step_pin, GPIO.HIGH)
            time.sleep(2)
            GPIO.output(step_pin, GPIO.LOW)
        elif int(wenzi[0]) > int(dian[0]): #x轴
            xmotol.move(-step_pin)
        elif int(wenzi[0]) < int(dian[0]):
            xmotol.move(step_pin)
        elif int(wenzi[1]) > int(dian[1]):
            ymotol.move(-step_pin)
        elif int(wenzi[1]) < int(dian[1]):
            ymotol.move(step_pin)
    if xxxxxxx: #若x值未达顶峰（低谷）
        xmotol.move(int(str(xzhengfu)) + str(step_pin))
    else:
        xzhengfu = abs(xzhengfu) #切换为“正”或“负”

    if yyyyyyy: #若y值未达顶峰（低谷）：
        ymotol.move(int(str(yzhengfu)) + str(step_pin))
    else:
        yzhengfu = abs(yzhengfu) #切换为“正”或“负”

    xmotol.move(step_pin)
    ymotol.move(step_pin)
'''