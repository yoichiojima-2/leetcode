fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    for (i, &num_i) in nums.iter().enumerate() {
        for (j, &num_j) in nums.iter().enumerate().skip(i + 1) {
            if num_i + num_j == target {
                return vec![i as i32, j as i32];
            }
        }
    }
    vec![]
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_two_sum() {
        let nums = vec![2, 7, 11, 15];
        let target = 9;
        let result = two_sum(nums, target);

        assert_eq!(result, vec![0, 1]);
    }
}

fn main() {
    let nums = vec![2, 7, 11, 15];
    let target = 9;
    let indices = two_sum(nums, target);
    println!("Indices: {:?}", indices);
}

