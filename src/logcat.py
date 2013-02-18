import Queue
import subprocess
import threading


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
    data = line.split(" ")
    if data[1] != "gps\r\n":
        if "16215" in data[0]:
            #print data[0]
            #print data[1]
            return True
        
def update_fps(line):
    print line

# Check the queues if we received some output (until there is nothing more to get).
while not stdout_reader.eof():
    while not stdout_queue.empty():
        line = stdout_queue.get()
        #print line.split(" ")
        #is_fps_line(line)
        if is_fps_line(line):
            update_fps(line)




