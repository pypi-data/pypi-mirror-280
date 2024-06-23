#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 02 28 00:58:20 2024

@project: damip
@author : kaiwei.li
@company: Digitopia Robotics Ltd.,Co.
"""

import sys
import os
import time
import json
import serial
import logging

# Set logging level
logging.basicConfig(level=logging.DEBUG, format=':) %(asctime)s %(levelname)s: %(message)s')

class Robot:

    __uart_dev= "/dev/ttyUSB0"
    __baudrate = 115200 #(9600,19200,38400,57600,115200,921600)
    serial_delay = 0.2 #delay seconds for serial

    name = "RayRanger"

    __HEAD_INIT_POSTION = 500
    __HEAD_SWING_RANGE = 200

    __RIGHT_ARM_INIT_POSTION = 500
    __RIGHT_ARM_SWING_RANGE = 200
    
    __LEFT_ARM_INIT_POSTION = 500
    __LEFT_ARM_SWING_RANGE = 200

    __LEFT_WHEEL_INIT_SPEED = 100
    __LEFT_WHEEL_STEP_SPEED = 50

    __BUS_FULL_VOL = 12.324

    # json messages

    # singleton
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            Robot._instance = object.__new__(cls)
        return Robot._instance
    
    # serial open
    try:
        __ser = serial.Serial(__uart_dev, int(__baudrate), dsrdtr=None, timeout=2) # timeout
    except Exception as e:
        logging.debug(":) Open serial failed!")

    # Initial
    def __init__(self):
        self.name = "RayRanger"
    
    # Hello Robot
    def hello(self):
        return(':) Hello, I am a RayRanger robot, My name is ' + self.name + ".")

    # Initial by serial
    def init(self):
        self.__serial_buffer_clear()
        self.head_postion(self.__HEAD_INIT_POSTION)
        self.right_arm_postion(self.__RIGHT_ARM_INIT_POSTION)
        self.left_arm_postion(self.__LEFT_ARM_INIT_POSTION)
    
    # Open serial
    def serial_open(self):
        try:
            self.__ser.open()
            return True
        except Exception as e:
            logging.debug(":) Open serial failed!")
            return False
    
    # Close serial
    def serial_close(self):
        try:
            self.__ser.close()
            return True
        except Exception as e:
            logging.debug(":) Close serial failed!")
            return False
    
    # Check serial
    def serial_check(self):
        try:
            ser_status = self.__ser.is_open
            logging.debug(":) Check serial opened!")
            return ser_status
        except Exception as e:
            logging.debug(":) Check serial failed!")
        return False

    # serial query
    def serial_query(self, message, flag):
        try:
            # add \n
            cmd_msg = message + "\n"
            # send data
            cmd_len = self.__ser.write(cmd_msg.encode('UTF-8'))
            logging.debug(":) Send: " + str(cmd_msg.replace("\n", "")))
            # delay
            time.sleep(self.serial_delay)
            # receive data
            rcv_msg = self.__ser.readline().decode('UTF-8')
            logging.debug(":) Recv: "+ str(rcv_msg.replace("\n", "")))
            # check mismatch
            if str(cmd_msg) not in str(rcv_msg):
                logging.error("serial receive datas mismatch error!")
                self.__serial_buffer_clear()
                return False
            # read the return data
            if flag:
                # time.sleep(self.serial_delay)
                rcv_msg = self.__ser.readline().decode('UTF-8')
                logging.debug(":) Recv: " + str(rcv_msg.replace("\n", "")))
                return str(rcv_msg)
        except serial.SerialException as e:
            logging.error(f"SerialException: {e}")
            return False
        except serial.SerialTimeoutException as e:
            logging.error(f"SerialTimeoutException: {e}")
            return False
        finally:
            logging.debug(":) Serial query success.")
        return True
    
    # Set head postion by serial
    def head_postion(self, value):
        cmd_head_pos = "{\"T\":505,\"id\":6,\"pos\":" + str(value) + ",\"spd\":500,\"acc\":30}"
        self.serial_query(cmd_head_pos, False)
        return True

    # Shake head by serial
    def head_shake(self, value):
        if value < 0 or value > 1:
            logging.error(":) Head shake value not support, value should be in [0:1].")
            return False
        postion_m = self.__HEAD_INIT_POSTION
        postion_a = postion_m - self.__HEAD_SWING_RANGE * value
        postion_b = postion_m + self.__HEAD_SWING_RANGE * value
        self.head_postion(postion_a)
        self.head_postion(postion_b)
        self.head_postion(postion_m)
        return True

    # Set right arm postion by serial
    def right_arm_postion(self, value):
        cmd_arm_pos = "{\"T\":505,\"id\":2,\"pos\":" + str(value) + ",\"spd\":500,\"acc\":30}"
        self.serial_query(cmd_arm_pos, False)
        return True

    # Shake right arm by serial
    def right_arm_shake(self, value):
        if value < 0 or value > 1:
            logging.error(":) Arm shake value not support, value should be in [0:1].")
            return False
        postion_m = self.__RIGHT_ARM_INIT_POSTION
        postion_a = postion_m - self.__RIGHT_ARM_SWING_RANGE * value
        postion_b = postion_m + self.__RIGHT_ARM_SWING_RANGE * value
        self.right_arm_postion(postion_a)
        self.right_arm_postion(postion_b)
        self.right_arm_postion(postion_m)
        return True

    # Set left arm postion by serial
    def left_arm_postion(self, value):
        cmd_arm_pos = "{\"T\":505,\"id\":8,\"pos\":" + str(value) + ",\"spd\":500,\"acc\":30}"
        self.serial_query(cmd_arm_pos, False)
        return True

    # Shake left arm by serial
    def left_arm_shake(self, value):
        if value < 0 or value > 1:
            logging.error(":) Left arm shake value not support, value should be in [0:1].")
            return False
        postion_m = self.__LEFT_ARM_INIT_POSTION
        postion_a = postion_m + self.__LEFT_ARM_SWING_RANGE * value
        postion_b = postion_m - self.__LEFT_ARM_SWING_RANGE * value
        self.left_arm_postion(postion_a)
        self.left_arm_postion(postion_b)
        self.left_arm_postion(postion_m)
        return True

    # Set speed by serial
    def move_speed(self, left_value, right_value):
        cmd_mov_speed = "{\"T\":11,\"L\":" + str(left_value) + ",\"R\":" + str(right_value) + "}"
        self.serial_query(cmd_mov_speed, False)
        return True
    
    # Manage move by serial
    def move_manage(self, value):
        if value < 0 or value > 1:
            logging.error(":) Move value not support, value should be in [0:1].")
            return False
        left_speed = self.__LEFT_WHEEL_INIT_SPEED + self.__LEFT_WHEEL_STEP_SPEED * value
        right_speed =self.__LEFT_WHEEL_INIT_SPEED + self.__LEFT_WHEEL_STEP_SPEED * value
        
        i = 0

        # lowly start
        for i in range(0,10,1): # 9~0 
            self.move_speed(int(left_speed * i/10), int(right_speed * i/10))
            time.sleep(self.serial_delay)
        
        # lowly stop
        for i in range(9,-1,-1): # 9~0 
            self.move_speed(int(left_speed * i/10), int(right_speed * i/10))
            time.sleep(self.serial_delay)
        
        # self.move_speed(0, 0)
        return True
    
    # Clear serial read buffer
    def __serial_buffer_clear(self):
        try:
            received_data = self.__ser.read_all().decode('UTF-8')
            received_data = self.__ser.read_all().decode('UTF-8')
            received_data = self.__ser.read_all().decode('UTF-8')
        except serial.SerialException as e:
            logging.error(f"SerialException: {e}")
            return False
        except serial.SerialTimeoutException as e:
            logging.error(f"SerialTimeoutException: {e}")
            return False
        finally:
            logging.debug(":) Cleared serial read buffer.")
        return True

    # Get base status
    def base_status(self):
        get_base_status = "{\"T\":130}"
        received_data = self.serial_query(get_base_status, True)        
        
        json_data = json.loads(received_data)
        bus_r = json_data['r']
        bus_p = json_data['p']
        bus_y = json_data['y']
        bus_v = json_data['v']

        logging.debug(":) base status:" + str(bus_r) + str(bus_p) + str(bus_y))

        bat_p = str(round((bus_v / self.__BUS_FULL_VOL) * 100, 2))
        logging.debug(":) base battery:" + str(bat_p) + "%")

        return str(bus_r), str(bus_p), str(bus_y), str(bat_p)

    # Get servo info
    def servo_status(self, number):
        cmd_get_servo = "{\"T\":506,\"id\":" + str(number) + "}"
        received_data = self.serial_query(cmd_get_servo, True)
        
        if len(received_data) != 0:
            json_data = json.loads(received_data)
            pos = str(json_data['pos'])
            volt = str(json_data['volt'])
            temp = str(json_data['temp'])
        else:
            pos = ""
            volt = ""
            temp = ""
            logging.error(":) Recv length is zero, bypass.")
        return pos, volt, temp

    # Get stance status
    def stance_status(self):
        cmd_get_stance = "{\"T\":126}"
        received_data = self.serial_query(cmd_get_stance, True)
        
        if len(received_data) != 0:
            json_data = json.loads(received_data)
            temp = str(json_data['temp'])
            roll = str(json_data['r'])
            pitch = str(json_data['p'])
            yaw = str(json_data['y'])
            acce_X = str(json_data['ax'])
            acce_Y = str(json_data['ay'])
            acce_Z = str(json_data['az'])
            gyro_X = str(json_data['gx'])
            gyro_Y = str(json_data['gy'])
            gyro_Z = str(json_data['gz'])
            magn_X = str(json_data['mx'])
            magn_Y = str(json_data['my'])
            magn_Z = str(json_data['mz'])
        else:
            temp = ""
            roll = ""
            pitch = ""
            yaw = ""
            acce_X = ""
            acce_Y = ""
            acce_Z = ""
            gyro_X = ""
            gyro_Y = ""
            gyro_Z = ""
            magn_X = ""
            magn_Y = ""
            magn_Z = ""
            logging.error(":) Recv length is zero, bypass.")
        logging.debug(":) acceleration info:" + str(acce_X) + "/" + str(acce_Y) + "/" + str(acce_Z))
        logging.debug(":) gyroscope info:" + str(gyro_X) + "/" + str(gyro_Y) + "/" + str(gyro_Z))
        logging.debug(":) magnetic field info:" + str(magn_X) + "/" + str(magn_Y) + "/" + str(magn_Z))
        return temp, roll, pitch, yaw, acce_X, acce_Y, acce_Z, gyro_X, gyro_Y, gyro_Z, magn_X, magn_Y, magn_Z

    # Get website url
    def website_url(self):
        url = 'https://digitopia.com.cn/rayranger/'
        return url

    # Speak english by espeak
    def speak_en(self, voice):
        cmd_data = 'espeak "' + str(voice) + '"'
        logging.debug(":) " + cmd_data)
        os.system(cmd_data)
        return True
