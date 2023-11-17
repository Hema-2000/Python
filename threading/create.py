import threading

import warnings #to avoid deprecation to get beacuse og getname()
warnings.filterwarnings("ignore",category=DeprecationWarning)

print("Current ExecutingThread:",threading.current_thread().getName()) #it is main thread to get the name we r using getName()
threading.current_thread().setName("MohanThread")#here setting name to a thread
print("Current ExecutingThread:",threading.current_thread().getName()) #to check whether tthe name of the thread