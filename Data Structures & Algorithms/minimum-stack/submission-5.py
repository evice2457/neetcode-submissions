class MinStack:

    def __init__(self):
        self.my_list = []
        self.minimum_list = []

    def push(self, val: int) -> None:
        if len(self.my_list) == 0:
            self.minimum_list.append(val)
        else:
            if val <= self.minimum_list[-1]:
                self.minimum_list.append(val)
        self.my_list.append(val)

    def pop(self) -> None:
        n = self.my_list.pop()
        if n == self.minimum_list[-1]:
            self.minimum_list.pop()

    def top(self) -> int:
        return self.my_list[-1]

    def getMin(self) -> int:
        return self.minimum_list[-1]
