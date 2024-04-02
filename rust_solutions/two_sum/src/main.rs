fn main(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let res: Vec<i32> = vec![];
    for (i, &num_i) in nums.iter().enumerate() {
        for (j, &num_j) in nums.iter().enumerate().skip(i + 1) {
            if (num_i + num_j) == target {
                return vec![i as i32, j as i32];
            }
        }
    }
    res
}


#[cfg(test)]
mod tests {
    use super::*; // This imports everything from the outer module, i.e., your Solution struct and its methods.

    #[test]
    fn test_two_sum() {
        // Example 1: Basic functionality
        let nums = vec![2, 7, 11, 15];
        let target = 9;
        let expected = vec![0, 1]; // Assuming the solution should be zero-based indices
        let result = main(nums, target);
        assert_eq!(result, expected, "Failed on basic functionality");

        // Example 2: Test with negative numbers
        let nums = vec![-3, 4, 3, 90];
        let target = 0;
        let expected = vec![0, 2]; // Indices of -3 and 3 which sum to 0
        let result = main(nums, target);
        assert_eq!(result, expected, "Failed with negative numbers");

        // Example 3: Test with multiple possible solutions, expecting the first correct pair
        let nums = vec![1, 2, 3, 4, 5];
        let target = 9;
        let expected = vec![3, 4]; // Indices of 4 and 5 which sum to 9
        let result = main(nums, target);
        assert_eq!(result, expected, "Failed on multiple solutions");
    }
}
