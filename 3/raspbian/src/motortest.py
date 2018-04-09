#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  motortest.py
#  Conducts a basic test of the two motors that drive the wheels
#
#  Copyright 2018  <pi@raspbari19>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import RPi.GPIO as GPIO					# the library that interfaces with GPIO registers
import time								# standard time library

def motortest(args):
	print("Starting Motor Test!")		# identify the start of the program
	GPIO.setmode(GPIO.BCM)				# using the Broadcom convention to identify the GPIO registers
	GPIO.setwarnings(False)				# ignore warnings - needed for repetitive execution of program
										# left motor uses pins 7 (reverse) and 8 (forward)
	Motor_left_reverse = 7
	GPIO.setup(Motor_left_reverse, GPIO.OUT)
	Motor_left_forward = 8
	GPIO.setup(Motor_left_forward, GPIO.OUT)
	print("{0}: reverse: {1}, forward: {2}".format("Left", Motor_left_reverse, Motor_left_forward))
										# right motor uses pins 9 and 10
	Motor_right_reverse = 9
	GPIO.setup(Motor_right_reverse, GPIO.OUT)
	Motor_right_forward = 10
	GPIO.setup(Motor_right_forward, GPIO.OUT)
	print("{0}: reverse: {1}, forward: {2}".format("Right", Motor_right_reverse, Motor_right_forward))
										# initialize the motor state
										# "off it"
	GPIO.output(Motor_left_reverse, GPIO.LOW)
	GPIO.output(Motor_left_forward, GPIO.LOW)
	GPIO.output(Motor_right_reverse, GPIO.LOW)
	GPIO.output(Motor_right_forward, GPIO.LOW)
	print("All pins now set to {0}".format(GPIO.LOW))
	time.sleep(1)
										# rotate left motor; "on it"
	print("Individual motor tests")
	print("{0} {1}".format("Left", "forward"))
	GPIO.output(Motor_left_reverse, GPIO.LOW)
	GPIO.output(Motor_left_forward, GPIO.HIGH)
	time.sleep(1)
	print("{0} {1}".format("Left", "reverse"))
	GPIO.output(Motor_left_reverse, GPIO.HIGH)
	GPIO.output(Motor_left_forward, GPIO.LOW)
	time.sleep(1)
										# turn off both motors; "off it"
	GPIO.output(Motor_left_reverse, GPIO.LOW)
	GPIO.output(Motor_left_forward, GPIO.LOW)
	GPIO.output(Motor_right_reverse, GPIO.LOW)
	GPIO.output(Motor_right_forward, GPIO.LOW)
	time.sleep(2)						# wait for two seconds
	GPIO.cleanup()						# reset the GPIO registers
	print("All done!")					# inform the operator
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(motortest(sys.argv))
