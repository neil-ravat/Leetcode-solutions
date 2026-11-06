class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
    vector<int> rs(nums.size());
    int sum = 0;
    for (int i =0 ; i < nums.size() ; i++){
        rs[i] = sum + nums [i];
        sum = rs[i];
     }
     return rs;
    }
};