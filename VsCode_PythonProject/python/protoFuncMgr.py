import json
from protos import register

class protoFcunMgr(dict):
  def __init__(self):
    dict.__init__(self)
    self.addAll()

  def addFunc(self,bt,lt,funcName):
    key=bt<<16+lt
    self[key]=funcName

  def addAll(self):
    self.addFunc(1,1,register.Proto_01.register)
    self.addFunc(1,2,register.Proto_01.login)

  def getFunc(self,bt,lt):
    key=bt<<16+lt
    if key in self:
      return self[key]
    return None

  def doRecvData(self,recvData):
    
    bt=int(recvData[2]["bt"])
    lt=int(recvData[2]["lt"])
    op=self.getFunc(bt,lt)
    if op:
      op(recvData)
      return True