class Solution(object):
    def compress(self, chars):
        i = 0
        write = 0

        while i < len(chars):
            j = i

            while j < len(chars) and chars[j] == chars[i]:
                j += 1

            count = j - i

            chars[write] = chars[i]
            write += 1

            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1

            i = j

        return write