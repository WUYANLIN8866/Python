import time
import threading
import queue
import logging
logging.basicConfig(level=logging.NOTSET, format='%(message)s')
logger = logging.getLogger()
class Worker(threading.Thread):
  def __init__(self, queue, num):
    threading.Thread.__init__(self)
    self.queue = queue
    self.num = num
  def run(self):
    while self.queue.qsize() > 0:
      msg = self.queue.get()
      logger.warning("Worker %d: %s", self.num, msg)
      time.sleep(1)
my_queue = queue.Queue()
for i in range(10):my_queue.put("Data %d" % i)
# Build two Worker
my_worker1 = Worker(my_queue, 1)
my_worker2 = Worker(my_queue, 2)
# Let Worker start processing data
my_worker1.start()
my_worker2.start()
# Waiting for all workers to end
my_worker1.join()
my_worker2.join()