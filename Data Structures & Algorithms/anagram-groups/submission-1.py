class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # previous one was 0(m nlogn) time complexity with 0(m) space..
        # so now that i finally reasoned my way to theee right solution
        # let's do it with 0(mn) && 0(m)

        # my_dict = {}

        # for word in strs:
        #     key = tuple(sorted(word))

        #     if key in my_dict:
        #         my_dict[key].append(word)
        #     else:
        #         my_dict[key] = [word]
        # return list(my_dict.values())

        # here we go.... start with empty dictionary

        my_dict = {}

        # let's count it first (just the way we did for valid anagrams) under a loop followed by another loop

        for word in strs:
            # well every word needs its own fresh counter, so we did it inside the loop and initialising it everytime within the loop
            count = [0] * 26
        # now now now.. find the index.. and increase the count[index] +=1
            for char in word:
                index = ord(char) - ord('a')
                count[index] += 1

            # let's get our key's, means something immutable, key needs to be immutable.. tuple's the answer
            key = tuple(count)
            # rest is same as what we've done with valid anagrams
            if key in my_dict:
                my_dict[key].append(word)
            else:
                my_dict[key] = [word]
        return list(my_dict.values())