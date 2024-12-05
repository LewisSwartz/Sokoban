class ObjOnGameBoard:
    # This init method is to create isobstacle, ispushable, isdestination, isunder, path.
    def __init__(self,isobstacle,ismovable,ispushable,isdestination,isunder,path):
        self.__is_obstacle=isobstacle
        self.__is_movable=ismovable
        self.__is_pushable=ispushable
        self.__is_destination=isdestination
        self.__is_under=isunder
        self.__path=path
    # This method is to set_is_obstacle.
    def set_is_obstacle(self,isobstacle):
        self.__is_obstacle=isobstacle
    # This method is to set_is_movable.
    def set_is_movable(self,ismovable):
        self.__is_movable=ismovable
    # This method is to set_is_pushable.
    def set_is_pushable(self,ispushable):
        self.__is_pushable=ispushable
    # This method is to set_is_destination.
    def set_is_destination(self,isdestination):
        self.__is_destination=isdestination
    # This method is to set_is_under.
    def set_is_under(self,isunder):
        self.__is_under=isunder
    # This method is to set_path.
    def set_path(self,path):
        self._path=path
    # This method is to get_is_obstacle.
    def get_is_obstacle(self):
        return self.__is_obstacle
    # This method is to get_is_movable.
    def get_is_movable(self):
        return self.__is_movable
    # This method is to get_is_pushable.
    def get_is_pushable(self):
        return self.__is_pushable
    # This method is to get_is_destination.
    def get_is_destination(self):
        return self.__is_destination
    # This method is to get_is_under.
    def get_is_under(self):
        return self.__is_under
    # This method is get_path.
    def get_path(self):
        return self.__path

# This class is to create Floor object.
class Floor(ObjOnGameBoard):
    # This method is to know isobstacle, ismovable, ispushable, isdestination, isunder, path.
    def __init__(self):
        ObjOnGameBoard.__init__(self,isobstacle=False,ismovable=False,ispushable=False,isdestination=False,isunder="Floor",path="floor.png")
    # This method is to get Floor object.
    def __str__(self):
        return "Floor"

# This class is to create Wall object.
class Wall(ObjOnGameBoard):
    # This method is to know isobstacle, ismovable, ispushable, isdestination, isunder, path.
    def __init__(self):
        ObjOnGameBoard.__init__(self,isobstacle=True,ismovable=False,ispushable=False,isdestination=False,isunder=Floor(),path="wall.png")
    # This method is to get Wall object.
    def __str__(self):
        return "Wall"

# This class is to create Box object.
class Box(ObjOnGameBoard):
    # This method is to know isobstacle, ismovable, ispushable, isdestination, isunder, path.
    def __init__(self):
        ObjOnGameBoard.__init__(self,isobstacle=True,ismovable=False,ispushable=True,isdestination=False,isunder=Floor(),path="box.png")
    # This method is to get Box object.
    def __str__(self):
        return "Box"

# This class is to create Person object.
class Person(ObjOnGameBoard):
    # This method is to know isobstacle, ismovable, ispushable, isdestination, isunder, path.
    def __init__(self):
        ObjOnGameBoard.__init__(self,isobstacle=True,ismovable=True,ispushable=False,isdestination=False,isunder=Floor(),path="worker.png")
    # This method is to get Person object.
    def __str__(self):
        return "Person"

# This class is to create BoxOnDestination object.
class BoxOnDestination(ObjOnGameBoard):
    # This method is to know isobstacle, ismovable, ispushable, isdestination, isunder, path.
    def __init__(self):
        ObjOnGameBoard.__init__(self,isobstacle=True,ismovable=False,ispushable=True,isdestination=False,isunder=Destination(),path="box_docked.png")
    # This method is to get BoxOnDestination.
    def __str__(self):
        return "BoxOnDestination"

# This class is to create Destination object.
class Destination(ObjOnGameBoard):
    # This method is to know isobstacle, ismovable, ispushable, isdestination, isunder, path.
    def __init__(self):
        ObjOnGameBoard.__init__(self,isobstacle=False,ismovable=False,ispushable=False,isdestination=True,isunder="Destination",path="dock.png")
    # This method is to get Destination.
    def __str__(self):
        return "Destination"
