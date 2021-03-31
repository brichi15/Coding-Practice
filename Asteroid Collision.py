class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        for ast in asteroids:
            
            ast_status = True
            while stack and stack[-1] > 0 and ast < 0:
                if abs(ast) > stack[-1]:
                    stack.pop()
                elif abs(ast) < stack[-1]:
                    ast_status = False
                    break
                else:
                    stack.pop()
                    ast_status = False
                    break
            
            if ast_status: stack.append(ast)
                
        return stack
                    