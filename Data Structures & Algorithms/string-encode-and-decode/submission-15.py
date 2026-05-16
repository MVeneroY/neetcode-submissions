class Solution:

    def encode(self, strs: List[str]) -> str:
        msg = ""
        for s in strs:
            msg += str(len(s)) + '#' + s
        return msg

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            if s[i] == '0':
                i += 2
                strs.append("")

            else:
                ln = int(s[i])
                while s[i+1] != '#':
                    ln *= 10
                    ln += int(s[i+1])
                    i += 1
                start = i+2
                end = start + ln
                strs.append(s[start:end])
                i = end

        return strs