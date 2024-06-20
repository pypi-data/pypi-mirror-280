# This libary is created and intended to be used with a Raspberry Pi 5

import serial
import os
import time
import subprocess
import RPi.GPIO as GPIO
from threading import Thread



class LIN:

    def __init__(self):
        self.ser = serial.Serial()
        self.mclr = 26
        self.send_status = 0
        self.stop_cont_thread  = False
        self.status_var = ''
        self.data = {}
        self.start_time = 0
         


#-------CONNECT TO BOARD---------------
# This function is the initialization function of connecting to the hat
    def connect(self, serial_baudrate = 115200, serial_port = '/dev/ttyAMA0'):
        try:
            # acm = '/dev/ttyAMA0' #Change this if not on Raspberry Pi 5. 'ttyS0' for RPi4 and 'ttyAMA0' for RPi3. Needs verification. Use command ls -l /dev and find serial0
            print('port selected = ', serial_port)
            self.ser.baudrate = serial_baudrate
            self.ser.port = serial_port
            if self.ser.isOpen() == False:
                print('open port')
                self.ser.open()
                self.t = Thread(target = self.rx_task) #Begin reading serial data
                self.t.start()
                time.sleep(0.5)
                self.open_coms() #Open LIN Coms
        
        except:
            print('can not open port')
            
            
        try:
            telegram_bin = bytearray()
            msg = b'V\r' 
            
            print('telegram_tx = ', msg)
            self.ser.write(msg)

        except:
            print('Can not start thread')



#--------------LIN BAUD RATE------------------
    def change_LIN_baudrate(self, baudrate = 19200):
        try:
            match baudrate:
                case 19200:
                    self.send("S3")
                case 10400:
                    self.send("S2")
                case 9600:
                    self.send("S1")
                case _:
                    print("Please enter a standard baudrate as an integer: 9600, 10400, 19200")
        except:
            "Cannot send baudrate request message on LIN"



#----------------READING SERIAL THREAD TASK--------------------

    def rx_task(self):
        print('rx task started')
        self.start_time = time.time()
        while True:

            rc_ch = 0
            telegram_string = b''
            bytecount = 0

            while (not rc_ch == b'\r') and bytecount < 120:
                rc_ch = self.ser.read()
                if(not rc_ch == b'\r'):
                    telegram_string = telegram_string + rc_ch
                    bytecount+=1

            if bytecount > 110:
                bytecount = 0

            if telegram_string[0] == 0x4d and telegram_string != b'M00': # M
                #Data format
                #Key: ID, [data, Time stamp, delta t, crc_status]
                pid_str = chr(telegram_string[3])+chr(telegram_string[4])     # Extract PID
                pid_int = int(pid_str,base=16)

                len_str = chr(telegram_string[1]) + chr(telegram_string[2])   # Extract length from 2bytes
                len_int=int(len_str,base=16)

                crc_str = chr(telegram_string[(len_int*2)+1])+chr(telegram_string[(len_int*2)+2]) # Extract checksum
                crc_int = int(crc_str,base=16)

                data_str = ''
                dataraw_str = b''
                for i in range(len_int -2):
                    data_str = data_str+chr(telegram_string[5+(i*2)])+chr(telegram_string[6+(i*2)])+' '
                    dataraw_str = dataraw_str +bytearray(chr(telegram_string[5+(i*2)])+chr(telegram_string[6+(i*2)]),encoding='utf-8')

                temp=[]
                temp.append(data_str)
                temp.append(time.time()-self.start_time)
                try:
                    if self.data[pid_str][1]:
                        temp.append(time.time()-self.start_time - self.data[pid_str][1])
                    else:
                        self.data[pid_str][1] = 0
                except:
                    temp.append(0)

                crc_status = self.crc_check(dataraw_str,len_int,pid_int,crc_int)
                temp.append(crc_status)  

                self.data[chr(telegram_string[3]) + chr(telegram_string[4])] = temp




#---------REQUEST READ CONSTANT------------
#    
    def cont_read(self, nodes, interval = 0):
        try:
                interval_int=int(interval)
                print("interval {:d}".format(interval_int))
                interval_int = interval_int/1000
        except:
                print("Interval must be a number")
                
        self.tcont = Thread(target = self.cont_read_task,args=[nodes, interval_int])
        
        if self.send_status == 0:
            self.stop_cont_thread = False
            self.tcont.start()
            self.send_status = 1

        else:
            
            self.send_status = 0
            self.stop_cont_thread = True
            self.tcont.join()


#---------REQUEST READ CONSTANT------------
# This is the thread for the function below
    def cont_read_task(self, nodes, interval):
        if isinstance(nodes, list):
            while 42:
                for node in nodes:
                    t=bytearray()
                    t=str.encode("r" + node)   
            
                    t= t+ b'\r'
                    self.ser.write(t)
                    time.sleep(interval)
                    if self.stop_cont_thread:
                        break
        else:
            while 42:
                t=bytearray()
                t=str.encode("r" + nodes)   
        
                t=t + b'\r'
                self.ser.write(t)
                time.sleep(interval)
                if self.stop_cont_thread:
                    break
                
   

#----------LIN HAT HARDWARE VERSION-----------
#
    def get_hardware(self):
        msg = b'V\r' 
            
        print('telegram_tx = ', msg)
        self.ser.write(msg)



#----------LIN HAT SOFTWARE VERSION-----------
#
    def get_software(self):
        msg = b'v\r' 
            
        print('telegram_tx = ', msg)
        self.ser.write(msg)




#----------OPEN COMS FOR THE HAT-----------
#
    def open_coms(self):
        msg = b'O\r' 
            
        print('telegram_tx = ', msg)
        self.ser.write(msg)



#----------CLOSE COMS FOR THE HAT-----------
#
    def close_coms(self):
        msg = b'C\r' 
            
        print('Closing LIN Communications')
        self.ser.write(msg)



#---------------SEND MESSAGE--------------
#This is a generic 
    def send(self, msg):

        t=bytearray()
        t=str.encode(msg)   
        t=t+ b'\r'
        
        print('telegram_tx = ', t)
        self.ser.write(t)




#---------------TRANSMIT MESSAGE--------------
#Transmit a LIN fram ewith classic checksum
    def transmit(self, address, data_length, data):
        msg = 't' + address + data_length + data
        t=bytearray()
        t=str.encode(msg)   
        t=t+ b'\r'
        
        print('telegram_tx = ', t)
        self.ser.write(t)



#---------------TRANSMIT ENHANCED MESSAGE--------------
#Transmit a LIN fram ewith classic checksum
    def transmit(self, address, data_length, data):
        msg = 'T' + address + data_length + data
        t=bytearray()
        t=str.encode(msg)   
        t=t+ b'\r'
        
        print('telegram_tx = ', t)
        self.ser.write(t)




#---------------WAKE-----------------------
#This wake a single or multiple devices using a standard code
    def wake_device(self, nodes):
        if isinstance(nodes, list):
            for id in nodes:
                msg = 't' + id + "4C000007F"
                self.send(msg)
                time.sleep(0.01)
        else:
            msg = 't' + nodes + "4C000007F"
            self.send(msg)
        


#-------------CRC CHECK-------------

    def crc_check(self, crc_str, length, pid,crc_int):
        
        if self.calculate_crc(crc_str,length-2,0) == crc_int:
    #         print('classic')
            res = 'Classic'
        elif self.calculate_crc(crc_str,length-2,pid) == crc_int:
            #print('enhance')
            res = 'Enhanced'
        else:
            #print('error')
            res = 'Error'
            
        return res



#-------------CRC CALCULATE-------------

    def calculate_crc(self, data, size, sum):
        
            self.array_bin = bytearray()
            self.len_str = ""
        
            for i in range(size):
                self.len_str = chr(data[i*2]) + chr(data[(i*2)+1])
            
                self.len_int=int(self.len_str,base=16)
            
                self.array_bin.append(self.len_int)
                
            for i in range(size):
                sum = sum + self.array_bin[i]
                
                if sum >= 256:
                    sum = sum-255
            sum = (-sum-1) & 0xff
            return sum
    

#------------GET DATA------------
    def get_messages(self, id = None):
        if id == None:
            return self.data
        else:
            if id in self.data:
                return self.data[id]
            else:
                print("No matching key")



#------------GET DATA------------
    def get_data(self, id):
        if id in self.data:
            return self.data[id][0]
        else:
            print("No matching key")
    


#------------GET TIMESTAMP------------
    def get_timestamp(self, id):
        if id in self.data:
            return self.data[id][1]
        else:
            print("No matching key")


#------------GET TIME DELTA------------
    def get_time_delta(self, id):
        if id in self.data:
            return self.data[id][2]
        else:
            print("No matching key")



#------------GET CHECKSUM------------
    def get_crc(self, id):
        if id in self.data:
            return self.data[id][3]
        else:
            print("No matching key")
    


#------------CLEAR DATA-------------
    def set_clear(self):
        self.data = []




#-------------RESET--------------
    def set_reset(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.mclr,GPIO.OUT)
        GPIO.output(self.mclr,False)
        time.sleep(0.1)
        GPIO.output(self.mclr,True)



#-------------DESTRUCTOR-------------
    def __del__(self):
        self.t.join()
        self.tcont.join()
        self.set_clear
        self.close_coms()


