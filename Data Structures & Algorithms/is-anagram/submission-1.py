class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ch_list = list(s)
        t_ch_list = list(t)
        s_len = len(s_ch_list)

        if not s_len == len(t_ch_list): return False

        s_ch_list.sort()
        t_ch_list.sort()

        for i in range(s_len):
            if not s_ch_list[i] == t_ch_list[i]: return False
        
        return True
        