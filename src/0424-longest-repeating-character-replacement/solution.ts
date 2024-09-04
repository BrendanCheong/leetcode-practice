function characterReplacement(s: string, k: number): number {
    const charCount: Map<string, number> = new Map();
    let left = 0;
    let maxFreq = 0;
    let maxLength = 0;

    for (let right = 0; right < s.length; right++) {
        // Add the current character to the frequency map
        const currentChar = s[right];
        charCount.set(currentChar, (charCount.get(currentChar) || 0) + 1);

        // Update maxFreq with the maximum count of any character in the current window
        maxFreq = Math.max(maxFreq, charCount.get(currentChar)!);

        const windowLength = right - left + 1;

        // If the window is invalid (too many replacements needed), shrink from the left
        if (windowLength - maxFreq > k) {
            const leftChar = s[left];
            charCount.set(leftChar, charCount.get(leftChar)! - 1);
            left++;  // Move the left pointer to the right
        }

        // Update maxLength with the size of the valid window
        maxLength = Math.max(maxLength, right - left + 1);
    }

    return maxLength;
}
