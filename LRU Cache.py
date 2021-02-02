class LRUCache: 
                
    def __init__(self, capacity: int):
        self.map = {}
        self.cap = capacity
        
        self.head = self.Node()
        self.tail = self.Node()
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        
        if key not in self.map:
            return -1
        
        cur_node = self.map[key]
        if self.head.next != cur_node:
            cur_node.prev.next = cur_node.next      #remove 
            cur_node.next.prev = cur_node.prev
            
            cur_node.next = self.head.next          #insert to front
            cur_node.prev = self.head
            
            self.head.next = cur_node
            cur_node.next.prev = cur_node
        
        return cur_node.val
        
    def put(self, key: int, value: int) -> None:
        
        if key not in self.map:
            cur_node = self.Node()
            self.map[key] = cur_node
            cur_node.key = key
            
        else:
            cur_node = self.map[key]
            
            cur_node.prev.next = cur_node.next
            cur_node.next.prev = cur_node.prev
            
        cur_node.val = value

        cur_node.next = self.head.next
        cur_node.prev = self.head

        self.head.next = cur_node
        cur_node.next.prev = cur_node
            
        if len(self.map) > self.cap:
            rem_node = self.tail.prev

            del self.map[rem_node.key]

            rem_node.prev.next = self.tail
            self.tail.prev = rem_node.prev
            
    class Node:
        def __init__(self):
            self.val = 0
            self.key = None
            self.next = None
            self.prev = None