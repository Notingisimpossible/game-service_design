from os import getenv
import pymssql
import re

class Dictionary():
  #连接数据库
  def conn():
    connect = pymssql.connect('127.0.0.1', 'sa', 's0217', 'dictionary') #服务器名,账户,密码,数据库名
    if connect:
      print("连接成功!")
      return connect

  #关闭数据库连接
  def closeConn(conn):
    conn.close()
    print('退出成功，欢迎您下次使用!')

  # 查单词
  def findWord(conn,key):
    cursor = conn.cursor()#创建游标，用来执行Sql语句
    key1 = '%' +key+'%' #创建数据库模糊查询字符串
    sql="SELECT * FROM dict WHERE keys like '%s'"%(key1) #sql语句
    cursor.execute(sql)
    words=[cursor.fetchall()]

    word_list = re.findall('(\'.*?\')',str(words)) #固定语句
    word_list = [re.sub("'",'',each) for each in word_list]
    i = 0
    if word_list:
      print('查询结果如下：')
      for strs in word_list:
        if i % 2 == 1:
          print(strs)
        else:
          print('%-20s'%(strs), end="")
        i += 1
      cursor.close()
    else:
      print('字典中没有该词！')
      cursor.close() #关闭游标

  #添加单词
  def addWord(conn, key, exp):
    cursor = conn.cursor()
    sql = "insert into dict (keys,explain) values('%s','%s')"%(key,exp)
    cursor.execute(sql)
    conn.commit()
    print('您已经成功添加该单词!')
    cursor.close()

  #删除单词
  def delectWord(conn, key):
    cursor = conn.cursor()
    sql = "delete from dict where keys = '%s'"%(key)
    cursor.execute(sql)
    conn.commit()
    print('您已经成功删除该单词!')
    cursor.close()

  #修改单词解释
  def changeWord(conn, key, ckey, exp):
    cursor = conn.cursor()
    if ckey == '':
      sql = "update dict set explain = '%s' where keys = '%s'"%(exp, key)
      cursor.execute(sql)
    else:
      sql = "update dict set explain = '%s' where keys = '%s'"%(exp, key)
      sql1 = "update dict set keys = '%s' where keys = '%s'"%(ckey, key)
      cursor.execute(sql)
      cursor.execute(sql1)
    conn.commit()
    print('您已经成功修改该单词！')
    cursor.close()

  #看所有单词
  def seeWord(conn):
    cursor = conn.cursor()
    sql = "select * from dict"
    cursor.execute(sql)
    words=[cursor.fetchall()]

    word_list = re.findall('(\'.*?\')',str(words)) #固定语句
    word_list = [re.sub("'",'',each) for each in word_list]
    print('字典中所有单词如下所示：')
    i = 0
    for strs in word_list:
      if i % 2 == 1:
        print(strs)
      else:
        print('%-20s'%(strs),end="")
      i += 1
    cursor.close()
  
  #判断单词是否已经存在数据库中
  def exists_key(conn, key):
    cursor = conn.cursor()
    sql="SELECT keys FROM dict WHERE dict.keys='%s'"%(key)
    cursor.execute(sql)
    words=[cursor.fetchall()]

    word_list = re.findall('(\'.*?\')',str(words)) #固定语句 获取数据库中所有符合要求字段
    word_list = [re.sub("'",'',each) for each in word_list]
    if key in word_list:
      cursor.close()
      return 1
    else:
      cursor.close()
      return 0
#主函数
if __name__ == "__main__":
  dic = Dictionary  #实例化字典类
  conn = dic.conn() #接收返回的数据库连接
  print('************欢迎使用简易英文词典**************')
  print('******请输入以下任一数字选择你需要的功能*******')
  print('查找：0  删除：1  添加：2  修改：3  查看：4  退出：5')
  key = int(input('请输入:'))
  while key != 5:  #判断选取的功能 格式化输出结果
    if key == 0:   #查询单词
      fkey = input('请输入您想查询的单词：')
      dic.findWord(conn, fkey)
    elif key == 1: #删除单词
      dkey = input('请输入您要删除的单词：')
      if dic.exists_key(conn, dkey) == 0: #判断单词是否存在
        print('您要删除的单词不存在！')
      else:
        dic.delectWord(conn, dkey)
    elif key == 2:  #添加单词
      akey = input('请输入您想要添加的单词：')
      aexp = input('请输入单词解释：')
      if dic.exists_key(conn, akey) == 1:  #判断单词是否存在，存在则不添加
        print('您输入的单词已经存在，无需重复添加！')
      else:
        dic.addWord(conn, akey, aexp)
    elif key == 3:  #修改单词解释
      ckey = input('请输入您想要修改的单词：')
      cfkey = input('请输入您要修改后的单词(不改单词则直接回车)：')
      cexp = input('请输入修改后的单词解释：')
      if dic.exists_key(conn, ckey) == 0: #判断要修改的单词是否存在
        print('字典中不存在该单词！')
      else:
        dic.changeWord(conn, ckey, cfkey, cexp)
    elif key == 4:  #查看全部单词
      dic.seeWord(conn)
    else:
      print('错误，请重新输入!')
    print('***********欢迎使用简易英文词典***************')
    print('******请输入以下任一数字选择你需要的功能*******')
    print('查找：0  删除：1  添加：2  修改：3  查看：4  退出：5')
    key = int(input('请输入：'))

  dic.closeConn(conn) #关闭数据库连接
