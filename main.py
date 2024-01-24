# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Servo standard servo example"""

import time
import board
import pwmio
from adafruit_motor import servo
from analogio import AnalogIn
import digitalio

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.GP0, duty_cycle=2 ** 15, frequency=50)

# potentiometer setup.
pot = AnalogIn(board.GP27)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

def angle_converter(value):
    scaled_value = (value/65535)*180
    return scaled_value

def RCServo_pos_Pot(flag):
    while flag:
        my_servo.angle = angle_converter(pot.value)
        time.sleep(0.1)

def RCServo_pos_REPL():
    while True:
        try:
            pos = float(input("Please enter the position(in angles[0-180]):"))

            my_servo.angle = pos

        except:
            print("Invalid value, please enter a floating number btw [0-180] range.")
            print("exiting...")
            break


def main():
    options = {"option 1" : "REPL", "option 2": "potentiometer"}
    print("----Servo Angle Control----")
    print("Option 1 - REPL\nOption 2 - Potentiometer")
    print("########---------########")
    option_input = input("Please make a mode selection:")

    if option_input == "REPL":
        RCServo_pos_REPL()
    elif option_input == "pot":
        RCServo_pos_Pot(True)

main()
