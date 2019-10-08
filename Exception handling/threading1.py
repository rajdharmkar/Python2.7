import sys
import threading
import time
import Queue


def thread(args1, stop_event, queue_obj):
    print "starting thread"
    stop_event.wait(10)
    if not stop_event.is_set():
        try:
            raise Exception("signal!")
        except Exception:
            queue_obj.put(sys.exc_info())
    pass


try:
    queue_obj = Queue.Queue()
    t_stop = threading.Event()
    t = threading.Thread(target=thread, args=(1, t_stop, queue_obj))
    t.start()

    time.sleep(11)

    # normally this should not be executed
    print "stopping thread!"
    t_stop.set()

    try:
        exc = queue_obj.get(block=False)
    except Queue.Empty:
        pass
    else:
        exc_type, exc_obj, exc_trace = exc
        print exc_obj

except Exception as e:
    print "action took to long, bye!"