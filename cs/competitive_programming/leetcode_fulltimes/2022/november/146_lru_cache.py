import collections

class LRUCache:

    def __init__(self, capacity: int):  
        self.key_value = collections.OrderedDict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        
        value = -1
        if key in self.key_value:
            value = self.key_value[ key ]
            self.key_value.move_to_end( key=key ,last=True )
        
        return value

    def put(self, key: int, value: int) -> None:
        
        self.key_value[ key ] = value
        self.key_value.move_to_end( key=key ,last=True )
        
        if( len( self.key_value ) > self.capacity ):
            self.key_value.popitem( last=False )

class LRUCache:

    def __init__(self, capacity: int):
        self.store = collections.OrderedDict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        val = -1
        if key in self.store:
            val = self.store[key]
            self.store.move_to_end(key=key)
        return val
        

    def put(self, key: int, value: int) -> None:
        self.store[key]=value
        self.store.move_to_end(key=key)
        if(len(self.store))>self.capacity:
            self.store.popitem(last=False)
