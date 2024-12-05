class ObjOnGameBoard:
    def __init__(self,isobstacle,ismovable,ispushable,isdestination,isunder,path):
        self.__is_obstacle=isobstacle
        self.__is_movable=ismovable
        self.__is_pushable=ispushable
        self.__is_destination=isdestination
        self.__is_under=isunder
        self.__path=path
    def set_is_obstacle(self,isobstacle):
        self.__is_obstacle=isobstacle
    def set_is_movable(self,ismovable):
        self.__is_movable=ismovable
    def set_is_pushable(self,ispushable):
        self.__is_pushable=ispushable
    def set_is_destination(self,isdestination):
        self.__is_destination=isdestination
    def set_is_under(self,isunder):
        self.__is_under=isunder
    def set_path(self,path):
        self._path=path
    def get_is_obstacle(self):
        return self.__is_obstacle
    def get_is_movable(self):
        return self.__is_movable
    def get_is_pushable(self):
        return self.__is_pushable
    def get_is_destination(self):
        return self.__is_destination
    def get_is_under(self):
        return self.__is_under
    def get_path(self):
        return self.__path

class Floor(ObjOnGameBoard):
    def __init__(self):
        ObjOnGameBoard.__init__(self,isobstacle=False,ismovable=False,ispushable=False,isdestination=False,isunder="Floor",path="D:\\Python programs\\sokoban\\floor.png")
    def __str__(self):
        return "Floor"
class Wall(ObjOnGameBoard):
    def __init__(self):
        ObjOnGameBoard.__init__(self,isobstacle=True,ismovable=False,ispushable=False,isdestination=False,isunder=Floor(),path="D:\\Python programs\\sokoban\\wall.png")
    def __str__(self):
        return "Wall"
class Box(ObjOnGameBoard):
    def __init__(self):
        ObjOnGameBoard.__init__(self,isobstacle=True,ismovable=False,ispushable=True,isdestination=False,isunder=Floor(),path="D:\\Python programs\\sokoban\\box.png")
    def __str__(self):
        return "Box"
class Person(ObjOnGameBoard):
    def __init__(self):
        ObjOnGameBoard.__init__(self,isobstacle=True,ismovable=True,ispushable=False,isdestination=False,isunder=Floor(),path="D:\\Python programs\\sokoban\\worker.png")
    def __str__(self):
        return "Person"
class BoxOnDestination(ObjOnGameBoard):
    def __init__(self):
        ObjOnGameBoard.__init__(self,isobstacle=True,ismovable=False,ispushable=True,isdestination=False,isunder=Destination(),path="D:\\Python programs\\sokoban\\box_docked.png")
    def __str__(self):
        return "BoxOnDestination"
class Destination(ObjOnGameBoard):
    def __init__(self):
        ObjOnGameBoard.__init__(self,isobstacle=False,ismovable=False,ispushable=False,isdestination=True,isunder="Destination",path="D:\\Python programs\\sokoban\\dock.png")
    def __str__(self):
        return "Destination"
