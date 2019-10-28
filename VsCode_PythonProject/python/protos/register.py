import os,json
import sys
cur_dir = os.path.abspath(os.path.dirname(__file__))
pro_dir = os.path.split(cur_dir)[0]
sys.path.append(pro_dir)

from CMgrPlayer import CMgrPlayer
import connect
class Proto_01():
  @staticmethod
  def register(recvData):
    mainTask,client,data=recvData
    c=connect.Connect()
    conn=c.conn()
    # (mainTask,client,data) #连接数据
    data=recvData[2]
    username=data["data"]["username"]
    password=data["data"]["password"]
    if (c.exists_of_rname(conn,username)==0):

      # c.addP(conn,username)

      p=mainTask.players.newPlayer(data["data"]["username"])
      c.addP(conn,username,CMgrPlayer.savewithPickle(p))
      # c.addPlayer(CMgrPlayer.savewithPickle(p))

      res={
      "code":0,
      "msg":"register success",
      "data":{}
      }
      client.transport.write(json.dumps(res).encode('utf8'))
      print(username,' register success')
    else:
      print("该名字已被注册，请换个名字!")    
    # 做下面操作之前，应该先查数据库，名字不存在，才能继续
    
    # res={
    #   "code":0,
    #   "msg":"register success",
    #   "data":{}
    # }
    # client.transport.write(json.dumps(res).encode('utf8'))
    # print("register success")

    # 查询数据库，查看用户是否存在
    # 在，返回用户重复错误
    # 不在，创建player
    # 存储player
    pass

  @staticmethod
  def login(recvData):
    c=connect.Connect()
    conn=c.conn()
    data=recvData[2]
    username=data["data"]["username"]
    password=data["data"]["password"]
    if (c.exists_of_rname(conn,username)==1):
      print(username," login success")
    else:
      print(username,'please register first')
      pass

  @staticmethod
  def useskill():
    pass