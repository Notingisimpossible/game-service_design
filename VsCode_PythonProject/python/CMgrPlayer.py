import pickle

from CPlayer import CPlayer

class CMgrPlayer(dict):
    def __init__(self):
        dict.__init__(self)
        # self.mainTask=mainTask
        self.newPlayer("zhangasn")

    def addPlayer(self,player):
        self[player.baseInfo["id"]]=player
    
    def rmPlayer(self,player):
        self.pop(player.baseInfo["id"])

    def newPlayer(self,name):
        player=CPlayer()
        player.setName(name)
        player.baseInfo["id"]=len(self)
        player.new_skill()

        self.addPlayer(player)
        return player
        # 如果重名，返回false；否则创建玩家，返回true
        # 更好的是用int，分别表示的各种不同的情况
    @staticmethod
    def loadwithpickle(val):
        return pickle.loads(val)

    @staticmethod
    def savewithPickle(obj):
        return pickle.dumps(obj,protocol=3)   

    def initFromDB(self,data):
        player=CPlayer()
        player.__setstate__(data)
        return player

if __name__ == "__main__":
    c=CMgrPlayer(None)

    x=CPlayer()
    x.baseinfo["nickname"]="张三"
    t=CMgrPlayer.savewithPickle(x) #序列化
    print(t) #输出x的序列化


    k=CMgrPlayer.loadwithpickle(t)


    print(k.__dict__)
    

