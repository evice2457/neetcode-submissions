class MinStack:

    def __init__(self):
        self.my_list = []

    def push(self, val: int) -> None:
        self.my_list.append(val)

    def pop(self) -> None:
        self.my_list.pop()

    def top(self) -> int:
        return self.my_list[-1]

    def getMin(self) -> int:
        if len(self.my_list) == 0:
            return None
        else:
            mini = self.my_list[0]
            for i in self.my_list:
                if i <= mini:
                    mini = i 
            return mini
