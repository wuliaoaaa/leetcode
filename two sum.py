class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        num_index = dict()
        index = 0
        for n in num:
            num_index.update({n:index})
            index = index + 1 
        
        for first_index in xrange(len(num)):
            second_num = target - num[first_index]
            second_index = num_index.get(second_num, -1)
            if second_index != -1 and first_index != second_index:
                if first_index <= second_index:
                    return [first_index+1, second_index+1]
                else:
                    return [second_index+1, first_index+1]
                    
        return []
