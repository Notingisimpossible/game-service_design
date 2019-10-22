import threading
import time
import queue,random

class producer (threading.Thread):
    def __init__(self, Q,name):
        threading.Thread.__init__(self)
        self.name=name # "生产者"
        self.Q=Q

    def run(self):
        while True:
            while not self.Q.full():
                x=random.randint(1,1000)
                self.Q.put(x)
                print("%s产生：%d" %(self.name,x))
                time.sleep(2)
            print(self.name,"结束了")

class consumer (threading.Thread):
    def __init__(self, Q, name):
        threading.Thread.__init__(self)
        self.name=name # "消费者"
        self.Q=Q

    def run(self):
        while True:
            while not self.Q.empty():            
                z=self.Q.get()
                print("%s消费了：%d" %(self.name,z))
                time.sleep(2)
        
Q=queue.Queue(10)
p1=producer(Q,"1#生产器")
p2=producer(Q,"2#生产器")
c1=consumer(Q,"1#消费者")
c2=consumer(Q,"2#消费者")
p1.start()
p2.start()
c1.start()
c2.start()