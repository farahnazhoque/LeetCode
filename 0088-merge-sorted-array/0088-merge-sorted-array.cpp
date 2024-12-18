class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        // Here, nums1 =1st array, nums2 = 2nd array...
        for(int i = 0 ; i < n ; i++)
            nums1[i + m] = nums2[i];
            // Sort the 1st array...
            sort(nums1.begin() , nums1.end());
        // Print the required result...
        return;
    }
};
