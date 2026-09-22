class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = True

        s_char_freqs = {}

        # build source chars freq map
        for ch in s:
            updated_freq = s_char_freqs.setdefault(ch, 0) + 1

            s_char_freqs.update({ ch: updated_freq })

        t_char_freqs = {}

        # target char freqs
        for ch in t:
            s_char_freq = s_char_freqs.setdefault(ch, 0)
            updated_freq = t_char_freqs.setdefault(ch, 0) + 1
            
            # not anagram if the freqs in target is already more than source
            if (t_char_freqs[ch] > s_char_freq):
                result = False
                continue

            t_char_freqs.update({ch: updated_freq})
        
        if result:
            result = s_char_freqs == t_char_freqs

        return result
        