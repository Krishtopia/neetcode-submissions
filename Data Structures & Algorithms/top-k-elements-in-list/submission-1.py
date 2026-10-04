class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # solution was okay but but doesn't meet the required optimal complexity...
        # my_dict = {}

        # # let's try to count the frequencies
        # for num in nums:
        #     my_dict[num] = my_dict.get(num, 0) + 1

        # # on my way to ~ sorting it
        # sorted_items = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)

        # # take the first k numbers....
        # return [item[0] for item in sorted_items[:k]]

        # here we go after messing up with mind lol

        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # since we've a dictionary as a frequency count let's move toward creating a bucket

        buckets = [[] for _ in range(len(nums)+1)]

        # successfully created, lets append the num's in the bucket, we'll use freq (value from dict/count) as the bucket index to access that specific list and store the num (that particular key).

        for num, freq in count.items():
            buckets[freq].append(num)
        
        # done!!!! done!!!! doneeeeeee!!!!!
        # let's move onto another step/final step where we'll create a answer list then the final loop for appending the top most frequent element 
        answer = []
        for freq in range(len(buckets)-1, 0, -1):
            for num in buckets[freq]:
                answer.append(num)

                # checking out the length of our very answer to see if it's == to k or not.. if it is we'll jusr return the answer
                if len(answer) == k:
                    return answer
                
        # & with that it's officiallyyy completed!!!!!!!!!!!!!!!!!
                

