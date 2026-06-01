class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        records = [0 for _ in range(len(temperatures))]
        stack = []

        for index, temp in enumerate(temperatures):
            # print(records)
            
            # Case: temps waiting on the stack
            if len(stack) > 0:

                # add records whose timespan have been determined
                slen = len(stack)               
                for si, (_index, _temp) in enumerate(stack[::-1]):
                    if temp > _temp:
                        records[_index] = index - _index
                        # print(len(stack) - 1 - si)
                        stack.pop(slen - 1 - si)

            stack.append((index, temp))

        return records