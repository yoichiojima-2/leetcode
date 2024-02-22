#[allow(dead_code)]

use std::collections::HashMap;

fn solution(nums: Vec<i32>) -> i32 {
    let mut counter = HashMap::new();
    for n in nums {
        *counter.entry(n).or_insert(0) += 1
    }

    let mut majority_num: i32 = 0;
    let mut majority_count: i32 = 0;
    for (num, count) in &counter {
        if *count > majority_count {
            majority_num = *num;
            majority_count = *count
        }
    }
    majority_num
}

fn main() {
    let arr: Vec<i32> = vec![2,2,1,1,1,2,2];
    let res = solution(arr);
    println!("{:?}", res);
}

#[cfg(test)]
#[allow(unused_imports)]
mod test {
    use super::*;
    
    #[test]
    fn test1() {
        let arr: Vec<i32> = vec![2,2,1,1,1,2,2];
        let res = solution(arr);
        assert_eq!(res, 2 as i32);
    }
}