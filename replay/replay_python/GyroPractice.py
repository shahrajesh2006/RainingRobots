#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

#gy = GyroSensor() 
# Put the gyro sensor into GYRO-ANG mode
# to measure the turn angle in degrees
#gy.mode='GYRO-ANG'

# Attach large motors to ports B and C
mB = LargeMotor('outB')
mC = LargeMotor('outC')

# Start the left motor with speed 40% to initiate a medium turn right.
mB.run_forever(speed_sp=360)

# Wait until the gyro sensor detects that the robot has turned
# (at least) 45 deg in the positive direction (to the right)
#while gy.value() <= 45: # loop until turn angle exceeds 45 degrees
    #sleep(0.01)
    
# Robot moves straight ahead with speed 50% until the wheels
# have turned through one rotation (360 degrees)
mB.run_to_rel_pos(position_sp=360, speed_sp=450, stop_action="brake")
mC.run_to_rel_pos(position_sp=360, speed_sp=450, stop_action="brake")

# Wait for the motion to finish
mB.wait_while('running')
mC.wait_while('running')
