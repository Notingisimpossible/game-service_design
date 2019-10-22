import os,json
import sys
cur_dir = os.path.abspath(os.path.dirname(__file__))
pro_dir = os.path.split(cur_dir)[0]
sys.path.append(pro_dir)

import connect
class Proto_01():
  @staticmethod
  def register(recvData):
    mainTask,client,data=recvData
    mainTask.players.newPlayer(data["data"]["username"])
    res={
      "code":0,
      "msg":"创建成功",
      "data":{}
    }
    client.transport.write(json.dumps(res).encode('utf8'))
    # c=connect.Connect()
    # conn=c.conn()
    # # (mainTask,client,data) #连接数据
    # data=json.loads(recvData[2])
    # username=data["data"]["username"]
    # password=data["data"]["password"]
    # if (c.exists_of_rname(conn,username)==0):
    #   c.addP(conn,username)
    #   print(username,' register success')
    # else:
    #   print("该名字已被注册，请换个名字!")
    # 查询数据库，查看用户是否存在
    # 在，返回用户重复错误
    # 不在，创建player
    # 存储player
    pass

  @staticmethod
  def login(recvData):
    c=connect.Connect()
    conn=c.conn()
    data=json.loads(recvData[2])
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