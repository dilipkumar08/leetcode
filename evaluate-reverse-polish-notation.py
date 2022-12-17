class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for t in tokens:
            try:
                stack.append(int(t))
            except:
                a=stack.pop()
                b=stack.pop()
                if t=="+":
                    c=b+a
                elif t=="-":
                    c=b-a
                elif t=="*":
                    c=b*a
                elif t=="/":
                    c=int(b/a)
                stack.append(c)
        return stack[-1]
