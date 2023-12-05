#!/usr/bin/env python3

# NAME: stop_motors.py
# PURPOSE: force stops the rotation motor
# AUTHOR: Emma Bethel


from gpiozero import PhaseEnableMotor

motor = PhaseEnableMotor(17, 18)
motor.stop()
