import Queue
import zmq
import subprocess
import threading
import re


class AsynchronousFileReader(threading.Thread):
    '''
    Helper class to implement asynchronous reading of a file
    in a separate thread. Pushes read lines on a queue to
    be consumed in another thread.
    '''

    def __init__(self, fd, queue):
        assert isinstance(queue, Queue.Queue)
        assert callable(fd.readline)
        threading.Thread.__init__(self)
        self._fd = fd
        self._queue = queue

    def run(self):
        '''The body of the tread: read lines and put them on the queue.'''
        for line in iter(self._fd.readline, ''):
            self._queue.put(line)

    def eof(self):
        '''Check whether there is no more content to expect.'''
        return not self.is_alive() and self._queue.empty()


# You'll need to add any command line arguments here.
process = subprocess.Popen(["/Users/quake0day/Documents/android-sdk-macosx/platform-tools/adb","logcat","|","grep","AuxilaryLog"], stdout=subprocess.PIPE)

# Launch the asynchronous readers of the process' stdout.
stdout_queue = Queue.Queue()
stdout_reader = AsynchronousFileReader(process.stdout, stdout_queue)
stdout_reader.start()

def is_fps_line(line):
    return 0


def update_fps(line,line_temp):
    return 0

# Check the queues if we received some output (until there is nothing more to get).

block = []
context = zmq.Context()
socket = context.socket(zmq.PUB)
#socket.connect("tcp://127.0.0.1:5000")

while not stdout_reader.eof():
    while not stdout_queue.empty():
        line = stdout_queue.get()
        if "Within" not in line and len(line) > 0:
            pre_line = line
            block.append(line)
            #print "PRELINE:",pre_line
        if "Within" in line:
            block.append(line)
            try:
                name = block[-2].split(":")[1]
                distance = block[-1].split(":")[1]
                print name,distance
                f = open("./tmp")
                f.write("1")
                f.close()
            except Exception,E:
                pass 

            block = []
           # print "DIS",line
        

