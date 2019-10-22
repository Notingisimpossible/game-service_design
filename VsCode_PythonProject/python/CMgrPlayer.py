

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
        # 如果重名，返回false；否则创建玩家，返回true
        # 更好的是用int，分别表示的各种不同的情况

    

