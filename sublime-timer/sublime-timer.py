import sublime, sublime_plugin
import threading  
import time

i=0

class timer(threading.Thread): #The timer class is derived from the class threading.Thread  
    def __init__(self, num, interval):
        threading.Thread.__init__(self)
        self.thread_num = num
        self.interval = interval
        self.thread_stop = False 
    def run(self): #Overwrite run() method, put what you want the thread do here
        global i
        while not self.thread_stop:
            sublime.set_timeout(write_time,1)
            i+=1  
            time.sleep(self.interval)          
    def pause(self):        
        self.thread_stop = True
    
    def zero(self):
        global i
        i=0    



thread1 = timer(1, 1)
class gtimerCommand(sublime_plugin.TextCommand):    
    def run(self, edit):
        global thread1
        thread=timer(1,1) 
        if thread1.isAlive():
            live=True
        else:                               
            thread.start()
            thread1=thread

class gtimerpauseCommand(sublime_plugin.TextCommand):    
    def run(self, edit):         
        global thread1
        thread1.pause()

class gtimerzeroCommand(sublime_plugin.TextCommand):    
    def run(self, edit):
        global thread1         
        thread1.zero()
        
   
def write_time():
    sublime.status_message(time_manage(i))

def time_manage(time_number):
    time_str='time:'+str(time_number/60)+'min '+str(time_number%60)+'s'
    return time_str
          
