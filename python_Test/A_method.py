#定义随机生成地图 实验五未用到此方法 故注释
# def creatMap(x):
#   print('hello')
#   map = []
#   print("Map is here:")
#   for i in range(x):
#     map.append([])
#     for j in range(x):
#       map[i].append(random.randint(0,1))
#       if j==x-1:
#         print(map[i][j])
#       else:
#         print(map[i][j],end="")
#   map[0][0] = 0
#   map [x-1][x-1] = 0
#   return map


#生成节点
class Node(object):
    #初始化节点
    def __init__(self, now, begin, end):
        super(Node, self).__init__()
        self.m_own = now
        self.m_g = 0
        self.m_h = abs( end[1] - now[1] ) + abs( end[0] - now[0] )#计算H值
        self.m_f = self.m_g + self.m_h
        self.m_begin = begin
        self.m_end = end
        self.m_flag = str( now )
        self.m_neighbors = []#用来存储当点节点的邻居节点
        self.m_parent = None
    
    #返回当前节点的字符串形式
    def get_flag(self):
        return self.m_flag
    #得到F值
    def get_fvalue(self):
        return self.m_f
    # 得到当前节点
    def get_position(self):
        return self.m_own
    #把邻居节点设为当前节点的父节点
    def set_parent(self, parentN):
        self.m_parent = parentN
    #得到父节点
    def get_parent(self):
        return self.m_parent
    #调用方法得到父节点
    parentN = property( get_parent, set_parent )
     # 设置G值
    def set_gvalue(self, g):
        self.m_g = g
    #得到G值
    def get_gvalue(self):
        return self.m_g
    #调用上面方法设置并得G值
    gvalue = property( get_gvalue, set_gvalue )
    #得到当前格子的相邻的格子
    def get_neighbors(self):
        #nei为上下左右四个方向，数组值为当前节点移动距离，例如[0,1]说明当前节点向右移动一格
        neb = [[0,1],[0,-1],[1,0],[-1,0]]
        #循环遍历当前节点四周节点
        for item in neb:
            x = item[0] + self.m_own[0]
            y = item[1] + self.m_own[1]
            if (x >= 0 and x < map_size) and (y >= 0 and y < map_size):
                if map[x][y] == 0:
                    self.m_neighbors.append( Node( (x, y), self.m_begin, self.m_end ) )

        return self.m_neighbors

#寻路函数
def aStarSearch( begin, end ):
    # 定义 未判断数组openList 已判断数组colseList
    openlist = []
    closelist = []

    #把起点加入open list
    begin_node = Node( begin, begin, end )
    begin_node.gvalue = 0
    openlist.append( begin_node )

    #主循环，每一轮检查一个当前方格节点
    while len(openlist) > 0:
        #在openlist中查找F值最小的节点作为当前方格节点
        _min = findMinNode( openlist )

        #当前方格节点从openlist中移除，进入closelist，代表这个格子已到达并检查过了。
        openlist.remove( _min )
        closelist.append( _min )

        #找到当前格上下左右所有可到达的格子，看它们是否在Openlist和Closelist中，如果不在，加入Openlist，计算出相应的G、H、F值，并把当前格子作为它们的“父节点”
        neighbors = _min.get_neighbors()
        for item in neighbors:
            if not isContains( openlist, item ) and not isContains( closelist, item ):
                item.parentN = _min
                item.gvalue = _min.gvalue + 1
                openlist.append( item )


        #如果终点在openlist中，直接返回终点格子
        for x in openlist:
            if x.get_flag() == str(end):
                return x

    #openlist用尽，仍然找不到终点，说明终点不可到达，返回空
    return None

#找到并返回openList中起点距离终点最近的点并返回
def findMinNode( _list ):
    _min = _list[0]
    for x in _list:
        if x.get_fvalue() < _min.get_fvalue():
            _min = x

    return _min
#判断节点是否在openList或closeList中
def isContains( _list, _node ):
    for item in _list:
        if item.get_flag() == _node.get_flag():
            return True
    return False


# 定义地图
map = [
[0,0,0,0,0],
[1,0,1,0,1],
[0,1,1,1,1],
[0,1,0,0,0],
[0,0,0,1,0]]

map_size = 5
dst= aStarSearch((0,0),(4,4))
# 异常处理 如果迷宫无解则dst最后一个节点为None,它将不会有get_flag方法，发生异常，此时对异常进行处理
try:
    path = [dst.get_flag()]
    while dst.parentN:
        dst = dst.parentN
        path.insert( 0, dst.get_flag() )
    print( path )
except AttributeError:
    print('该迷宫无解！')
    pass