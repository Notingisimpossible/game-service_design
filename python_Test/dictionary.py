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
    key1 = '%'+key+'%'
    sql="SELECT * FROM dict WHERE keys like '%s'"%(key1)
    cursor.execute(sql)
    words=[cursor.fetchall()]

    word_list = re.findall('(\'.*?\')',str(words)) #固定语句
    word_list = [re.sub("'",'',each) for each in word_list]
    if key in word_list:
      print('查询结果如下：')
      print(word_list)
      cursor.close()
    else:
      print('字典中没有该词！')
      cursor.close()


  def addWord(conn, key, exp):
    
    print('您已经成功添加该单词!')


  def delectWord(conn, key):
    print('您已经成功删除该单词!')


  def changeWord(conn, key, exp):
    print('您已经成功修改该单词！')

  #看所有单词
  def seeWord(conn):
    cursor = conn.cursor()
    sql = "select * from dict"
    cursor.execute(sql)
    words=[cursor.fetchall()]

    word_list = re.findall('(\'.*?\')',str(words)) #固定语句
    word_list = [re.sub("'",'',each) for each in word_list]
    print('字典中所有单词如下所示：', word_list)

if __name__ == "__main__":
  dic = Dictionary
  conn = dic.conn()
  print('************欢迎使用简易英文词典**************')
  print('******请输入以下任一数字选择你需要的功能*******')
  print('查找：0  删除：1  添加：2  修改：3  查看：4  退出：5')
  key = int(input('请输入：'))
  while key != 5:
    if key == 0:
      fkey = input('请输入您想查询的单词：')
      dic.findWord(conn, fkey)
    elif key == 1:
      dkey = input('请输入您要删除的单词：')
      dic.delectWord(conn, dkey)
    elif key == 2:
      akey = input('请输入您想要添加的单词：')
      aexp = input('请输入单词解释：')
      dic.addWord(conn, akey, aexp)
    elif key == 3:
      ckey = input('请输入您想要修改的单词：')
      cexp = input('请输入修改后的单词解释：')
      dic.changeWord(conn, ckey, cexp)
    elif key == 4:
      dic.seeWord(conn)
    else:
      print('错误，请重新输入!')
    print('***********欢迎使用简易英文词典***************')
    print('******请输入以下任一数字选择你需要的功能*******')
    print('查找：0  删除：1  添加：2  修改：3  查看：4  退出：5')
    key = int(input('请输入：'))

  dic.closeConn(conn)
