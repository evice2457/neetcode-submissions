class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_list = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                my_list.append(int(token))
            else:
                a = my_list.pop()
                b = my_list.pop()
                if token == "+":
                    my_list.append(b+a)
                elif token == "-":
                    my_list.append(b-a)
                elif token == "*":
                    my_list.append(b*a)
                else:
                    my_list.append(int(b/a))
        return my_list[0]
            