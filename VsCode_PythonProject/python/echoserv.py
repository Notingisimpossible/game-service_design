from twisted.internet import reactor, defer,utils,task,protocol
from twisted.protocols.policies import TimeoutMixin

#from twisted.internet.protocol import Protocol,Factory
class YibinProto(protocol.Protocol,TimeoutMixin):
    def __init__(self, factory):              
        self.factory=factory
        self.terminate=1800 #秒
        self._gotdata=True
            
    def connectionMade(self):
        try:
            self.setTimeout(self.terminate)
            # self.factory.register(self)

        except Exception as ex:
            s='maxClients error:%s,行号：%d' % (repr(ex), ex.__traceback__.tb_lineno)
            self.factory.mainTask.logger.error(s)

    def timeoutConnection(self): 
        """Called when the connection times out. 
        Override to define behavior other than dropping the connection. 
        """ 
        try:
            ip=self.transport.getPeer().host
            self.connectionLost("socket:%s is closed for no data." %(str(ip)))
        except Exception as ex:
            s='maxClients error:%s,行号：%d' % (repr(ex), ex.__traceback__.tb_lineno)
            #self.factory.mainTask.logger.error(s)

    def connectionLost(self, reason):
        try:          
            self.setTimeout(None)            
            self.factory.unregister(self)         
            
            # if self in self.factory.mainTask.clients:
            #     self.factory.mainTask.clients.pop(self) #现在改为字典了，所以用popkey
            print("lost connect:with reason:%s"  % reason)
        except Exception as ex:
            s='maxClients error:%s,行号：%d' % (repr(ex), ex.__traceback__.tb_lineno)
            #self.factory.mainTask.logger.error(s)
    
    def dataReceived(self, data):
        #self.transport.write(data)
        self.resetTimeout()  
        self._gotdata = True
        try:

#            if data[15:19]==b'2051':
#                print(data)
                
            sdata=data.decode() #   
            self.factory.parseData(self,sdata)
        except Exception as e:
            #改为log到文件
            #print('发生错误的文件：', e.__traceback__.tb_frame.f_globals['__file__'])
            s='dataReceived error:%s,%s,行号：%d' % (str(data),repr(e), e.__traceback__.tb_lineno)
            #self.factory.mainTask.logger.error(s)
        return

class YibinFactory(protocol.Factory):
    
    def __init__(self, mainTask,max_clients=300):
        #self.dataToVals=DataToVals()
        self.mainTask=mainTask
        self.activeConnections=0
        self.max_clients=max_clients
        # self.Parser=self.mainTask.packetParser
        
    def buildProtocol(self, addr):
        return YibinProto(self)

    def register(self, client,data=None):
        #self.clients[client.peer] = {"object": client, "partner": None}
        self.mainTask.register(client,data)

    def unregister(self, client):
        return self.mainTask.unregister(client)
        #self.clients.pop(client.peer)

    def findPartner(self, func_name, val):
        return self.mainTask.findPartner(func_name, val)

    def parseData(self,client,msg):
        self.mainTask.msgRecvQueue.put((client,msg))

        #self.Parser.parseTCPData(client,msg)
        