class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        cnt = [0] * 26

        for c in s1:
            cnt[ord(c) - ord('a')] += 1

        left = 0
        need = len(s1)

        for right in range(len(s2)):
            idx = ord(s2[right]) - ord('a')

            if cnt[idx] > 0:
                need -= 1
            cnt[idx] -= 1

            if need == 0:
                return True

            if right - left + 1 == len(s1):
                left_idx = ord(s2[left]) - ord('a')

                if cnt[left_idx] >= 0:
                    need += 1
                cnt[left_idx] += 1

                left += 1

        return False