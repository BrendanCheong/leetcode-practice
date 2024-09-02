function lengthOfLongestSubstring(s: string): number {
    if (s.length === 0) {
        return 0;
    }

    // The input string may not just be alphabets, could be any utf-8 chars.
    const charIndex = new Map<string, number>();
    let [first, result] = [0, 0];

    for (let i = 0; i < s.length; i++) {
        const secondChar = s[i];

        if (charIndex.has(secondChar) && charIndex.get(secondChar) >= first) {
            // shrink the window, duplicate found
            first = charIndex.get(secondChar) + 1
        }

        // update second pointer in map
        charIndex.set(secondChar, i);

        // calculate max window
        result = Math.max(result, i - first + 1);
    };

    return result;
};
