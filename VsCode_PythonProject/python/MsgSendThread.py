import threading
import time
import queue,random
import protoFuncMgr
class MsgSendThread (threading.Thread):
    def __init__(self, mainTask,name=''):
        threading.Thread.__init__(self)
        self.name=name # "生产者"
        self.mainTask=mainTask

    def run(self):
        while True:
            while not self.mainTask.msgSendQueue.empty():                
                z=self.mainTask.msgSendQueue.get()
                client,msg=z
                print(msg)
                try:
                    client.transport.write(msg.encode('utf8'))
                except Exception as ex:
                    print(repr(ex))