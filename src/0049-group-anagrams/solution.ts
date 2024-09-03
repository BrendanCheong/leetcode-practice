function groupAnagrams(strs: string[]): string[][] {
    /**
     * We can solve this by making each string a unique array of 26 characters
     * basically bucket sort in a sense but with 26 array characters
     */
     const anagrams = new Map<string, string[]>();

    for (const str of strs) {
        // O(26) operation
        const charArray = new Array(26).fill(0);
        for (const char of str) {
            // chosen character code - relative position to 'a' in 26 char alphabet
            charArray[char.charCodeAt(0) - 'a'.charCodeAt(0)] += 1;
        }
        // now serialize the charArray
        const serializedKey = charArray.join(',');
        if (!anagrams.has(serializedKey)) {
            anagrams.set(serializedKey, [str])
        } else {
            anagrams.get(serializedKey).push(str)
        }
    }
    // Now return hashmap values
    return Array.from(anagrams.values());
};
