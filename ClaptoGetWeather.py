import Adafruit_BBIO.PWM as PWM
import subprocess, shlex #for shell command
subprocess.call(shlex.split('echo BB-PWM1 > /sys/devices/platform/bone_capemgr/slots')) #for shell command2
subprocess.call(shlex.split('echo cape-universaln > /sys/devices/platform/bone_capemgr/slots')) #for shell command3

myPWM="P8_13"
PWM.start(myPWM, 0, 1000)
for i in range(0,5):
    DC=input("What Duty Cycle Would You Like")
    PWM.set_duty_cycle(myPWM, DC)
PWM.stop(myPWM)
PWM.cleanup()