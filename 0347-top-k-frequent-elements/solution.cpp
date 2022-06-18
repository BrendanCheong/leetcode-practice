#include<bits/stdc++.h>

using namespace std;
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        /**
        * This is the O(n) + O(m) + O(k log m) + O(k) solution 
        */
        unordered_map<int, int> mp;
        vector<vector<int>> ans;
        vector<int> output;
        for (auto& k : nums) {
            if (!mp.count(k))
                mp[k] = 1;
            else
                mp[k]++;
        }
        
        for (auto& [k, v] : mp) {
            vector<int> struc = {v, k};
            ans.push_back(struc);
        }
        
        partial_sort(ans.begin(), ans.begin() + k, ans.end(), greater<vector<int>>());
        
        for (int i = 0; i < k; i++) {
            output.push_back(ans[i][1]);
        }
        
        return output;
        
    }
};
