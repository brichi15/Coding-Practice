class BSTIterator:

    def __init__(self, root: TreeNode):
        
        self.stack = list()
        self.root = None
        self.visited = set()
        
        while root:
            
            self.stack.append(root)
            root = root.left


    def next(self) -> int:
        
        self.root = self.stack[-1]
                
        if not self.root:
            return self.root
    
        while self.root.left and self.root.left not in self.visited:

            self.stack.append(self.root.left)
            self.root = self.root.left
            
        if self.stack:    
            self.stack.pop()
        self.visited.add(self.root)
            
        if self.root.right and self.root.right not in self.visited:
            self.stack.append(self.root.right)
            
        
        return self.root.val
        

    def hasNext(self) -> bool:
        
        if self.stack: return True
        
        return False
        