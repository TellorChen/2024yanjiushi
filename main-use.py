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
        #GPIO.output(step_pin, GPIO.HIGH)
        time.sleep(steps)
        #GPIO.output(step_pin,GPIO.LOW)


capture = cv2.VideoCapture(0)
capture.set(6, cv2.VideoWriter_fourcc('M','J','P','G'))
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
frame_count = 0
start_time = time.time()
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

    
    ####################################################################################################################
    111
    
    ret, frame = capture.read()
    
    # 若读取帧失败，则跳出循环
    # If reading the frame fails, break out of the loop
    if not ret:
        break
    
    # 帧计数器递增
    # Increment frame counter
    frame_count += 1
    
    # 每隔10帧计算一次FPS
    # Calculate FPS every 10 frames
    if frame_count % 10 == 0:
        # 计算当前FPS
        # Calculate current FPS
        end_time = time.time()
        fps = frame_count / (end_time - start_time)
        # 将FPS保留两位小数
        # Round FPS to two decimal places
        fps = "{:.2f}".format(fps)
        # 在帧上添加显示FPS的文字
        # Add text showing FPS on the frame
        cv2.putText(frame, "FPS:" + str(fps), (0, 50), cv2.FONT_ITALIC, 1, (0, 255, 0), 2)
        # 显示当前帧
        # Display the current frame
        cv2.imshow('CameraPreview', frame)
        # 重置帧计数器和起始时间
        # Reset frame counter and start time
        frame_count = 0
        start_time = time.time()
'''