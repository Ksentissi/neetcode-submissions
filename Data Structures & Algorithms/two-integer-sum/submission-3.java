class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] tab = new int[2];
        int j =0;
        for(int i =0 ; i < j+1; i++){
            for (j =i; j<nums.length; j++ ){
            if ((nums[i]+nums[j]==target) && (i!=j)){
                tab[0] = i;
                tab[1]=j;
                return tab;
            }
        }
        }
            return tab;
        }
    }

