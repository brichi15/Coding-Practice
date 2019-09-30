class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        map<int,int> hash;
        vector<int> sol(2);
        
        int val;
        int comp;
        
        
        for(int i=0; i<nums.size(); i++)
        {
            val = nums[i];
            comp = target - val;
            
            if(hash.count(val))
            {
                sol[0] = hash[val];
                sol[1] = i;
                break;
            }
            hash[comp] = i;
    
        }
        return sol;
    }
};