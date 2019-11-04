import threading
import time
import queue,random
import os,json
import sys

sys.path.append('.')

import protoFuncMgr


class MsgRecvThread (threading.Thread):
    def __init__(self, mainTask,name=''):
        threading.Thread.__init__(self)
        self.name=name # "生产者"
        self.mainTask=mainTask
        self.protoMgr=protoFuncMgr.protoFcunMgr()

    def run(self):
        while True:
            while not self.mainTask.msgRecvQueue.empty():
                try:                
                    client,data=self.mainTask.msgRecvQueue.get()
                    dx=json.loads(data)
                    self.protoMgr.doRecvData((self.mainTask,client,dx))
                except Exception as ex:
                    print(repr(ex))