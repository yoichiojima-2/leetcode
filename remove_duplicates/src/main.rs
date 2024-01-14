#[allow(dead_code)]

fn solution(nums: &mut Vec<i32>) -> i32 {
    let mut replace: usize = 0;
    for i in 1..nums.len() {
        if nums[replace] != nums[i] {
            replace += 1;
            nums[replace] = nums[i]
        }
    }
    (replace + 1) as i32
}

fn main() {
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test1() {
        let mut nums: Vec<i32> = vec![1, 1, 2];
        let result = solution(&mut nums);
        assert_eq!(nums[0], 1 as i32);
        assert_eq!(nums[1], 2 as i32);
        assert_eq!(result, 2 as i32);
    }

    #[test]
    fn test2() {
        let mut nums: Vec<i32> = vec![0, 0, 1, 1, 1, 2, 2, 3, 3, 4];
        let result = solution(&mut nums);
        assert_eq!(nums[0], 0 as i32);
        assert_eq!(nums[1], 1 as i32);
        assert_eq!(nums[2], 2 as i32);
        assert_eq!(nums[3], 3 as i32);
        assert_eq!(nums[4], 4 as i32);
        assert_eq!(result, 5 as i32);
    }
}
