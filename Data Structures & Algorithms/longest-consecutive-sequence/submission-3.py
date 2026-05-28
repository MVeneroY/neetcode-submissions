class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        class Sequence:
            start: int
            end: int
            length: int

            def __init__(self, start):
                self.start = start
                self.end = self.start

            def length(self):
                return int(math.fabs(self.end - self.start) + 1)

            def merge(seq1, seq2):
                new = Sequence(min(seq1.start, seq2.start))
                new.end = max(seq1.end, seq2.end)
                return new

        if len(nums) == 0: return 0
        sequences = [Sequence(nums[0])]

        for num in nums[1:]:
            s_found = False
            for s in sequences:
                if num >= s.start and num <= s.end:
                    s_found = True
                    break
                if num + 1 == s.start:
                    s.start = num
                    s_found = True
                    break
                elif num - 1 == s.end:
                    s.end = num
                    s_found = True
                    break

            if not s_found:
                sequences.append(Sequence(num))

            else:
                for i1, s1 in enumerate(sequences):
                    for i2, s2 in enumerate(sequences):
                        if i1 == i2: continue
                        if s1.end + 1 == s2.start or s2.end + 1 == s1.start:
                            merged = Sequence.merge(s1,s2)
                            sequences.append(merged)
                            sequences.pop(i2)
                            sequences.pop(i1)

        m = max(sequences, key=Sequence.length)
        return m.length()
            