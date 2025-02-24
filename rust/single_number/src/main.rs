use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        let mut counter = HashMap::new();
        for &i in nums.iter() {
            *counter.entry(i).or_insert(0) += 1;
        }
        for (&k, &v) in counter.iter() {
            if v == 1 {
                return k;
            }
        }
        0
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_single_number() {
        let nums = vec![2, 2, 3, 2];
        let result = Solution::single_number(nums);
        assert_eq!(result, 3);
    }
}
