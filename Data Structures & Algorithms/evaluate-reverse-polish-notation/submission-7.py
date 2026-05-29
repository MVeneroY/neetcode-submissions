class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        buffer = []

        for token in tokens:
            # print(buffer)
            # print(f'{token[-1]=}')

            if token[-1].isdigit():
                buffer.append(int(token))

            else:
                op2 = buffer.pop()
                op1 = buffer.pop()    
                
                if token == '+':
                    buffer.append(op1 + op2)
                elif token == '-':
                    buffer.append(op1 - op2)
                elif token == '*':
                    buffer.append(op1 * op2)
                elif token == '/':
                    buffer.append(int(op1 / op2))
        return buffer.pop()

