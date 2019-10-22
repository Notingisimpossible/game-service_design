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
        # c=connect.Connect()
        while True:
            while not self.mainTask.msgRecvQueue.empty():
                try:                
                    client,data=self.mainTask.msgRecvQueue.get()
                    dx=json.loads(data)
                    self.protoMgr.doRecvData((self.mainTask,client,dx))
                    # self.mainTask.msgSendQueue.put((client,"you register ok."))
                    # print(msg)

                    # arr=msg.split(',')

                    # if len(arr)<3:
                    #     continue
                    # myname=''

                    # if arr[0]!='1':
                    #     myname=self.mainTask.clients[client][1] #自己的名字
                        
                    # if arr[0]=='1' and arr[1]=='1':#注册
                    #     name = arr[2]
                    #     self.mainTask.players[arr[2]]=arr[2]
                    #     # self.mainTask.msgSendQueue.put((client,"you register ok."))
                    #     # client.transport.write("you register ok.".encode('utf8'))
                    #     conn=c.conn()
                    #     if (c.exists_of_table(conn,'P_name')==0):
                    #         print("P_name 表格创建成功！")
                    #         c.creatL(conn)
                    #         pass
                    #     else:
                    #         print("P_name 表格已经存在！")
                    #         pass
                        
                    #     if (c.exists_of_rname(conn,name)==0):
                    #         c.addP(conn,name)
                    #         self.mainTask.msgSendQueue.put((client," you register ok."))
                    #     else:
                    #         self.mainTask.msgSendQueue.put((client," The name already been register,please chang name."))
                    #         print("该名字已被注册，请换个名字!")
                    #         pass

                    # elif arr[0]=='1' and arr[1]=='2':#登录
                    #     conn=c.conn()
                    #     name = arr[2]
                    #     if (c.exists_of_rname(conn,name)==1):
                    #         self.mainTask.register(client,arr[2]) #登录
                    #         self.mainTask.msgSendQueue.put((client,"you logged on."))
                    #     else:
                    #          self.mainTask.msgSendQueue.put((client," The name has no register,please register first "))
                    #     # client.transport.write("you logged on.".encode('utf8'))
                    # elif arr[0]=='2' and arr[1]=='1':#私聊
                    #     cx=self.mainTask.findPlayerByName(arr[2])            
                    #     ddd="%s 对你说:%s"
                    #     s=ddd % (myname,arr[3])
                    #     self.mainTask.msgSendQueue.put((cx,s))
                    #     # cx.transport.write(s.encode('utf8'))
                    # elif arr[0]=='2' and arr[1]=='2':#满世界聊天
                    #     for cx in self.mainTask.clients:
                    #         ddd="%s speak to all people:%s"
                    #         s=ddd % (myname,arr[2])
                    #         # cx.transport.write(s.encode('utf8'))
                    #         self.mainTask.msgSendQueue.put((cx,s))
                    # elif arr[0]=='2' and arr[1]=='3':#组聊
                    #     for cx in self.mainTask.getPlayersInGroup(arr[2]):
                    #         ddd="%s speak:%s"
                    #         s=ddd % (myname,arr[3])
                    #         self.mainTask.msgSendQueue.put((cx,s))
                    #         # cx.transport.write(s.encode('utf8'))
                    # elif arr[0]=='3' and arr[1]=='1':#创建组
                    #     self.mainTask.groups[arr[2]]=[]
                    #     self.mainTask.msgSendQueue.put((client,"group created success."))
                    # elif arr[0]=='3' and arr[1]=='2':#加入组
                    #     self.mainTask.groups[arr[2]].append(myname) #这个不对，应该通知组内所有人
                    #     self.mainTask.msgSendQueue.put((client,"group created success."))
                    # elif arr[0]=='3' and arr[1]=='3':#退出组
                    #     pass

                    # client.transport.write(msg.encode('utf8'))
                except Exception as ex:
                    print(repr(ex))