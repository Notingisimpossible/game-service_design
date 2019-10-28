from twisted.internet import reactor, defer,utils,task,protocol
from twisted.protocols.policies import TimeoutMixin
import queue,random
import re
import pymssql

from echoserv import YibinProto,YibinFactory
from MsgRecvThread import MsgRecvThread
from MsgSendThread import MsgSendThread
from CMgrPlayer import CMgrPlayer


class MainTask():
    def __init__(self):
        self.clients={}
        self.players=CMgrPlayer()#playerid,class_player
        self.groups={} #聊天组

        self.msgRecvQueue=queue.Queue(1000) #创建长度1000的消息对列

        self.msgSendQueue=queue.Queue(1000) #创建长度1000的消息对列
        # self.msgSendThread=MsgSendThread(self,"msgsend Thread")
        self.threadArr=[]
        for idx in range(4):
            self.threadArr.append(MsgRecvThread(self,"msg recv Thread %d" %(idx)))
        for idx in range(2):
            self.threadArr.append(MsgSendThread(self,"msg send Thread %d" %(idx)))
        

        pass

    def register(self,client,data):
        self.clients[client]=(client,data) #player

        pass

    def unregister(self,client):
        xx=self.clients.pop(client)
        if not xx:
            xx.transport.loseConnection()
        pass

    def findPlayerByName(self,data):
        for key in self.clients:
            if self.clients[key][1]==data:
                return key
        return None
    def getPlayersInGroup(self,groupName):
        clt_list=[] #组内玩家的连接列表
        for pName in self.groups[groupName]:
            x=self.findPlayerByName(pName)
            if not x: #如果玩家已经登录。（没登录的玩家不需要发信息）
                clt_list.append(x)
        return clt_list

    def tcpServer(self,port):
        reactor.listenTCP(port,YibinFactory(self,700))
    
    def start(self,port=8000):
        self.tcpServer(port)
        for th in self.threadArr:
            th.start()

if __name__ == "__main__":
    m=MainTask()
    m.start()
    reactor.run()
    
    pass
