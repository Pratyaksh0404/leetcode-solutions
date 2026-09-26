class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {}

        for i, ch in enumerate(s):
            last[ch] = i

        st = []
        ins = set()

        for i, ch in enumerate(s):
            if ch in ins:
                continue

            while (st and st[-1] > ch and last[st[-1]] > i):
                ins.remove(st.pop())

            st.append(ch)
            ins.add(ch)

        return "".join(st)