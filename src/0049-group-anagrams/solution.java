class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> anagrams = new HashMap<>();

        for (String s : strs) {
            int[] charArray = new int[26];
            for (char c : s.toCharArray()) {
                charArray[c - 'a']++;
            }

            StringBuilder key = new StringBuilder();
            for (int count : charArray) {
                key.append(count).append(',');
            }
            String serialisedKey = key.toString();

            if (!anagrams.containsKey(serialisedKey)) {
                anagrams.put(serialisedKey, new ArrayList<>());
            }
            anagrams.get(serialisedKey).add(s);
        }

        // convert hash map into list
        return new ArrayList<>(anagrams.values());
    }
}
