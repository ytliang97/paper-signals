import Adafruit_BBIO.PWM as PWM




myPWM="P8_13"
PWM.start(myPWM, 0, 1000)
for i in range(0,5):
    DC=input("What Duty Cycle Would You Like")
    PWM.set_duty_cycle(myPWM, DC)
PWM.stop(myPWM)
PWM.cleanup()