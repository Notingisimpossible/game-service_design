from os import getenv
import pymssql
import re



class Connect():
  def __init__(self):
    self.pid = 0
  def conn(self):
      connect = pymssql.connect('127.0.0.1', 'sa', 's0217', 'game_Player') #服务器名,账户,密码,数据库名
      if connect:
          print("连接成功!")
          return connect

  # def creatL(self,conn):
  #   cursor = conn.cursor()   #创建一个游标对象,python里的sql语句都要通过cursor来执行
  #   cursor.execute("create table P_name(name varchar(20) primary key)")   #执行sql语句
  #   conn.commit()  #提交
  #   cursor.close()   #关闭游标
  #   # conn.close()  #关闭连接

  def addP(self,conn,na,pa,pData):
    cursor = conn.cursor()   #创建一个游标对象,python里的sql语句都要通过cursor来执行
    sql = "insert into P_name (name,password) values('%s','%s')"%(na,pa)
    cursor.execute(sql)   #执行sql语句
    self.pid=cursor.lastrowid

    if pData is not None:
      # sql2="insert into player (pid,playerContent) values('%d',%s)" % (pid,pymssql.Binary(pData))
      sql2="insert into player (pid,playerContent) values(%d,%s)"
      # print(type(pData))
      # xxx=str(pData)
      cursor.execute(sql2,(self.pid,pymssql.Binary(pData)))#,(pid,xxx) #pData.decode('gbk')
      conn.commit()
    cursor.close()   
    # conn.close()

  # def exists_of_table(self,conn,table_name): #判断表格是否已经存在
  #   cursor = conn.cursor()
  #   sql = "SELECT table_name, table_type FROM information_schema.tables;"
  #   cursor.execute(sql)
  #   tables = [cursor.fetchall()] #返回表格名

  #   table_list = re.findall('(\'.*?\')',str(tables)) #固定语句
  #   table_list = [re.sub("'",'',each) for each in table_list]
  #   if table_name in table_list:
  #     cursor.close()
  #     return 1
  #   else:
  #     cursor.close()
  #     return 0

  def exists_of_rname(self,conn,name):#判断该名字是否已经存在数据库表中
    cursor = conn.cursor()
    sql="SELECT name FROM P_name WHERE P_name.name='%s'"%(name)
    cursor.execute(sql)
    names=[cursor.fetchall()]

    name_list = re.findall('(\'.*?\')',str(names)) #固定语句
    name_list = [re.sub("'",'',each) for each in name_list]
    if name in name_list:
      cursor.close()
      return 1
    else:
      cursor.close()
      return 0

  def get_playerContent(self, conn):#获取游戏角色信息
    cursor = conn.cursor()
    # pid = cursor.lastrowid 
    # pid = Connect.get_id()
    sql = "select playerContent from player where player.pid='%d'"%(self.pid)
    cursor.execute(sql)
    conn.commit()
    players = cursor.fetchall()#接收游标返回的全部结果

    if players:
      cursor.close()
      conn.close()
      return players
    else:
      cursor.close()
      conn.close()
      return None
      
