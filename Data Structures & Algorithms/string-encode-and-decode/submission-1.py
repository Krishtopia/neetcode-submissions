class Solution:

    def encode(self, strs: List[str]) -> str:
        
        # /// TIME TO REDO ITTTTTTTTTTT!!!!!!!!!!!
        
    #     encoded = ""

    #     for s in strs:
    #         encoded += str(len(s)) + "#" + s

    #     return encoded

    # def decode(self, s: str) -> List[str]:
    #     decoded = []
    #     i = 0

    #     while i < len(s):
    #         j = i

    #         # umm.. as i recall, let's find the separator
    #         while s[j] != "#":
    #             j += 1

    #         # length of the next string
    #         length = int(s[i:j])

    #         # now, now, read exactly `length` characters...
    #         word = s[j + 1:j + 1 + length]
    #         decoded.append(word)

    #         # let's move to the beginning of the next encoded string
    #         i = j + 1 + length
    #     return decoded

        encoded = ""

        for string in strs:
            encoded += str(len(string)) + "#" + string

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            word = s[j + 1:j + 1 + length]
            decoded.append(word)

            i = j + 1 + length
        return decoded


