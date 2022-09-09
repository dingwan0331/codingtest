# Stack 클래스
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, value):
        self.items.append(value)
        
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print('Stack is empty')
        
    def top(self):
        try:
            return self.items[:-1]
        except IndexError:
            print('Stack is empty')
    
    def __len__(self):
        try:
            return len(self.items)
        except:
            print('range Error')

# infix를 postfix로 바꾸기
def infix_to_postfix(infix: list)-> list:
    operators = ['+', '-', '*', '/']
    level1_operators = ['+', '-']
    level2_operators = ['*', '/']
    stack = Stack()
    postfix = []
    
    for token in infix:
    	# 피연산자일 경우 바로 postfix로 push
        if type(token) in [int, float]:
            postfix.append(token)
            
        # '('일 경우 바로 스택으로
        elif token == '(':
            stack.push(token)
            
        # ')'일 경우 스택에서 '('를 만날때까지 스택의 토큰들을 posfix로 push
        elif token == ')':
            stack_token = stack.pop()
            while stack_token != '(':
                postfix.append(stack_token)
                stack_token = stack.pop()
        
        # 연산자일경우 우선순위를 따져서 수행
        elif token in operators:
            for i in range(len(stack.items)+1):
                if token in level1_operators:
                    if stack.top() in level2_operators:
                        postfix.append(stack.pop())
                    else:
                        stack.push(token)
                        break
                elif token in level2_operators:
                    if stack.top() in level1_operators:
                        postfix.append(stack.pop())
                    else:
                        stack.push(token)
                        break
    # 스택의 남은 연산자들을 모두 posfix로 push
    while len(stack)>0:
        postfix.append(stack.pop())
    return postfix
    
# postfix 실제로 계산하기
def calculator(postfix: list) -> list:
    stack = Stack()
    for token in postfix:
        # 피연산자일경우
        if type(token) in [int, float]:
            # 스택으로 push
            stack.push(token)
        # 연산자일경우
        else:
            # 두수를 연산자로 계산
            first_token = stack.pop()
            second_token = stack.pop()
            if token == '+':
                result = first_token + second_token
            elif token == '-':
                result = first_token - second_token
            elif token == '*':
                result = first_token * second_token
            else:
                result = first_token / second_token
            # 계산결과 스택에 push
            stack.push(result)
    
    # 스택에 남은 수를 return 
    return stack.pop()