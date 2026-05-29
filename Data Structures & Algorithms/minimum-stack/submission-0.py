class MinStack:
    _stack: list[int]
    _mins: list[int]

    def __init__(self):
        self._stack = []
        self._mins = []

    def push(self, val: int) -> None:
        if type(val) != int:
            return

        self._stack.append(val)
        if len(self._mins) == 0:
            self._mins.append(val)
        elif val < self._mins[-1]:
            self._mins.append(val)
        else:
            self._mins.append(self._mins[-1])

    def pop(self) -> None:
        self._stack.pop()
        self._mins.pop()
        

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._mins[-1]        
