using ll = long long int;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        ll l = 0;
        ll r = nums.size() - 1;
        while (l <= r) {
            ll mid = l + (r - l) / 2;
            if (nums[mid] == target)
                return mid;
            else if (nums[mid] > target)
                r = mid - 1;
            else
                l = mid + 1;
        }
        return -1;
    }
};
