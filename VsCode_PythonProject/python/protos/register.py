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
      c.addP(conn,username,password,CMgrPlayer.savewithPickle(p))
      # c.addPlayer(CMgrPlayer.savewithPickle(p))
      res={
      "code":0,
      "msg":"register success",
      "data":{}
      }
      client.transport.write(json.dumps(res).encode('utf8'))
      print(username,' register success')
    else:
      client.transport.write(json.dumps({"msg":"The name has been register, please register first!"}).encode('utf8'))
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
    mainTask,client,data=recvData
    c=connect.Connect()
    conn=c.conn()
    data=recvData[2]
    username=data["data"]["username"]
    password=data["data"]["password"]

    
    if (c.exists_of_rname(conn,username)==1):
      if (c.judge_password(conn,username,password) == 1):
        playerData = CMgrPlayer.loadwithpickle(c.get_playerContent(conn))
        res={
        "code":0,
        "msg":"login success",
        "data":(playerData.baseInfo,playerData.dtInfo),
        "skill 1": "Fire attack",
        "skill 2":"thump"
        }
        client.transport.write(json.dumps(res).encode('utf8'))
        print(username," login success")
      else:
        client.transport.write(json.dumps({"msg":"password error, login fail!"}).encode('utf8'))
        print("密码错误，登录失败")
    else:
      client.transport.write(json.dumps({"msg":"please register first!"}).encode('utf8'))
      print(username,'用户不存在请先注册！')
      pass

  @staticmethod
  def useskill(recvData):
    mainTask,client,data=recvData
    c=connect.Connect()
    conn=c.conn()
    data=recvData[2]
    skill = data["data"]["skill"]
    if skill == "1":
      client.transport.write(json.dumps({"msg":"You use Fire attack, enemy's HP reduce 10"}).encode("utf8"))
    elif skill == "2":
      client.transport.write(json.dumps({"msg": "You use thump, enemy's HP reduce 50"}).encode("utf8"))
    else:
      client.transport.write(json.dumps({"msg":"You attack is miss"}).encode("utf8"))
    pass