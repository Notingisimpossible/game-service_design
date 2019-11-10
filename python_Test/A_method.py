import math


the_map = [
[0,0,0,0,0,0,0],
[0,1,1,1,1,1,0],
[0,1,0,1,0,0,0],
[0,1,0,1,0,1,0],
[0,0,0,1,0,1,0]]

map_row = 5
map_col= 7

class Node(object):
    def __init__(self, _mine, _begin, _end):
        super(Node, self).__init__()

        self.m_own = _mine
        self.m_g = 0
        self.m_h = abs( _end[1] - _mine[1] ) + abs( _end[0] - _mine[0] )
        self.m_f = self.m_g + self.m_h
        self.m_begin = _begin
        self.m_end = _end
        self.m_tag = str( _mine )
        self.m_neighbors = []
        self.m_parent = None

    def set_gvalue(self, g):
        self.m_g = g
    def get_gvalue(self):
        return self.m_g
    gvalue = property( get_gvalue, set_gvalue )

    def set_parent(self, parent):
        self.m_parent = parent
    def get_parent(self):
        return self.m_parent
    parent = property( get_parent, set_parent )

    def get_tag(self):
        return self.m_tag

    def get_fvalue(self):
        return self.m_f

    def get_position(self):
        return self.m_own

    def get_neighbors(self):
        nei = [[0,1],[0,-1],[1,0],[-1,0]]
        for item in nei:
            x = item[0] + self.m_own[0]
            y = item[1] + self.m_own[1]
            if (x >= 0 and x < map_row) and (y >= 0 and y < map_col):
                if the_map[x][y] == 0:
                    self.m_neighbors.append( Node( (x, y), self.m_begin, self.m_end ) )

        return self.m_neighbors

def findMinNode( _list ):
    _min = _list[0]
    for x in _list:
        if x.get_fvalue() < _min.get_fvalue():
            _min = x

    return _min

def isContains( _list, _node ):
    for item in _list:
        if item.get_tag() == _node.get_tag():
            return True
    return False

def aStarSearch( _begin, _end ):
    openlist = []
    closelist = []
    #把起点加入open list

    begin_node = Node( _begin, _begin, _end )
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
                item.parent = _min
                item.gvalue = _min.gvalue + 1
                openlist.append( item )


        #如果终点在openlist中，直接返回终点格子
        for x in openlist:
            if x.get_tag() == str(_end):
                return x

    #openlist用尽，仍然找不到终点，说明终点不可到达，返回空
    return None


dst = aStarSearch( (2,2),(3,4) )
path = [dst.get_tag()]
while dst.parent:
    dst = dst.parent
    path.insert( 0, dst.get_tag() )

print( path )