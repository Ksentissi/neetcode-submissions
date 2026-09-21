class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict= {} # index :value    value = target -key
    
        for i, n in enumerate(nums) : 
           
            if n in dict :
                return [dict[n],i]
            dict[target-n] = i
        

        
        return {}
    
    
        