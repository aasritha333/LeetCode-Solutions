class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Iterate through each element with index 'i'
        for (int i = 0; i < nums.length; i++) {
            // Iterate through the remaining elements with index 'j'
            // starting from 'i + 1' to avoid duplicate pairs and summing an element with itself
            for (int j = i + 1; j < nums.length; j++) {
                // Check if the sum of elements at 'i' and 'j' equals the target
                if (nums[i] + nums[j] == target) {
                    // If found, return a new array containing these two indices
                    return new int[]{i, j};
                }
            }
        }
        // If no solution is found (though the Two Sum problem guarantees one),
        // you might throw an exception or return an empty array depending on problem constraints.
        // For standard Two Sum, this line should ideally not be reached.
        throw new IllegalArgumentException("No two sum solution");
    }
}