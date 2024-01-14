#[allow(dead_code, unused_mut)]

fn solution(nums: &mut Vec<i32>) {
    let mut last_looked_num: &i32 = &nums[0];
    println!("{:?}", last_looked_num);
}

fn main() {
    let mut nums: Vec<i32> = vec![0, 0, 1, 1, 1, 2, 2, 3, 3, 4];
    let result = solution(&mut nums);
    println!("{:?}", result);
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test1() {
        let mut nums: Vec<i32> = vec![1, 1, 2];
        let result = solution(&mut nums);
        assert_eq!(result, 2 as i32);
        assert_eq!(nums[0], 1 as i32);
        assert_eq!(nums[1], 2 as i32);
    }

    #[test]
   fn test2() {
        let mut nums: Vec<i32> = vec![0, 0, 1, 1, 1, 2, 2, 3, 3, 4];
        let result = solution(&mut nums);
        assert_eq!(result, 5 as i32);
        assert_eq!(nums[0], 0 as i32);
        assert_eq!(nums[1], 1 as i32);
        assert_eq!(nums[2], 2 as i32);
        assert_eq!(nums[3], 3 as i32);
        assert_eq!(nums[4], 4 as i32);
    }
}