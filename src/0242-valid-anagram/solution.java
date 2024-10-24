class Solution {
    public boolean isAnagram(String s, String t) {
        // Bucket sort to allow for O(n) time complexity
        // But with O(26) Space, so this is most optimal
        int[] counts = new int[26];
        for (char c : s.toCharArray()) {
            counts[c - 'a']++;
        }
        // you can decrement or create another char array
        for (char c : t.toCharArray()) {
            counts[c - 'a']--;
        }

        for (int num : counts) {
            if (num != 0) {
                return false;
            }
        }
        return true;
    }
}
