import threading
import time

def thread(args1, stop_event):
    print "starting thread"
    stop_event.wait(10)
    if not stop_event.is_set():
        raise Exception("signal!")
    pass

try:
    t_stop = threading.Event()
    t = threading.Thread(target=thread, args=(1, t_stop))
    t.start()

    time.sleep(11)

    #normally this should not be executed
    print "stopping thread!"
    t_stop.set()

except Exception as e:
    print "action took to long, bye!"