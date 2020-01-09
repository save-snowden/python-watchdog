#IT18211160 SOS_2_Assignment
#This Program will capture the events hapenning in a selected location and log the details in to a selected file

'''
In this code the log file is created inside te users documents. You can save the log file in secured location and you just have to change the file location 

/home/chamod_wijetunga/Documents/log.txt  --> Code Location

'''
import getpass #To display the username
import sys
import time 
from datetime import datetime #To display time and date
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler  #WatchDog Library Event

username = getpass.getuser() #This will take the username out
now = datetime.now()
dt_string = now.strftime("%d-%m-%Y %H:%M:%S") #Those commands will take date and time and arrange that to a order


class EventHandler(FileSystemEventHandler):
    
    def on_created(self,event):
        if event.is_directory:
           print("{} - {} - Created Directory {}".format(username,dt_string,event.src_path))#On Directory create event
	   f = open("/home/chamod_wijetunga/Documents/log.txt", "a") #File parth for store details. Open the end of the file and write 
	   f.write("{} - {} - Created Directory {}\n".format(username,dt_string,event.src_path)) 
	   f.close()
	
	else:
	   print("{} - {} - Created File {}".format(username,dt_string,event.src_path)) #On File create event
	   f = open("/home/chamod_wijetunga/Documents/log.txt", "a")#File parth for store details. Open the end of the file and write
	   f.write("{} - {} - Created File {}\n".format(username,dt_string,event.src_path)) 
	   f.close()
	   

    def on_deleted(self,event):
        if event.is_directory:
           print("{} - {} - Deleted Directory {}".format(username,dt_string,event.src_path))  #On Directory delete event
	   f = open("/home/chamod_wijetunga/Documents/log.txt", "a")#File parth for store details. Open the end of the file and write
           f.write("{} - {} - Deleted Directory {}\n".format(username,dt_string,event.src_path))
	   f.close()
	
	else:
	   print("{} - {} - Deleted File {}".format(username,dt_string,event.src_path)) #On File delete event
	   f = open("/home/chamod_wijetunga/Documents/log.txt", "a")#File parth for store details. Open the end of the file and write
	   f.write("{} - {} - Deleted File {}\n".format(username,dt_string,event.src_path))
	   f.close()

    def on_modified(self,event):
        if event.is_directory:
           print("{} - {} - Modified Directory {}".format(username,dt_string,event.src_path))  #On Directory modify event
	   f = open("/home/chamod_wijetunga/Documents/log.txt", "a")#File parth for store details. Open the end of the file and write
	   f.write("{} - {} - Modified Directory {}\n".format(username,dt_string,event.src_path))
           f.close()
	   
	else:
	   print("{} - {} - Modified File {}".format(username,dt_string,event.src_path)) #On File modify event
	   f = open("/home/chamod_wijetunga/Documents/log.txt", "a")#File parth for store details. Open the end of the file and write
	   f.write("{} - {} - Modified File {}\n".format(username,dt_string,event.src_path))
	   f.close()

    def on_moved(self,event):
        if event.is_directory:
           print("{} - {} - Moved Directory from {} to {}".format(username,dt_string,event.src_path,event.dest_path))  #On Directory move event
	   f = open("/home/chamod_wijetunga/Documents/log.txt", "a")#File parth for store details. Open the end of the file and write
           f.write("{} - {} - Moved Directory from {} to {}\n".format(username,dt_string,event.src_path,event.dest_path))
	   f.close()

	else:
	   print("{} - {} - Moved File from {} to {}".format(username,dt_string,event.src_path,event.dest_path)) #On File move event
	   f = open("/home/chamod_wijetunga/Documents/log.txt", "a")#File parth for store details. Open the end of the file and write
	   f.write("{} - {} - Moved File from {} to {}\n".format(username,dt_string,event.src_path,event.dest_path))
	   f.close()

if __name__ == "__main__":  #Start of the Main Function
    path = sys.argv[1] if len(sys.argv) > 1 else '.'

    event_handler = EventHandler() #Setting Up event handler
    observer = Observer() #setting up observer
    observer.schedule(event_handler, path, recursive=True)
    observer.start() #Starting observing and keeping it running till an interrupt occure
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
	
        observer.stop() #Stopping Observing Events
    observer.join()
    




