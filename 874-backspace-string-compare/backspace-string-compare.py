class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_len = len(s) - 1
        t_len = len(t) - 1
        f = 0
        l = 0
        count = 0

        s_new = []
        t_new = []

        while f <= s_len:
            if s[f] == "#":
                if s_new:
                    s_new.pop()
            else:
                s_new.append(s[f])
            f += 1

        while l <= t_len:
            if t[l] == "#":
                if t_new:
                    t_new.pop()
            else:
                t_new.append(t[l])
            l += 1

        if s_new == t_new:
            return True
        else:
            return False