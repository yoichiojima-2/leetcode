fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
    for (idx, num) in nums.iter().enumerate() {
        if *num >= target {
            return idx as i32;
        }
    }
    nums.len() as i32
}

fn main() {
    let nums: Vec<i32> = vec![1, 3, 5, 6];
    let target: i32 = 5;
    let res = search_insert(nums, target);
    println!("{:?}", res);
}

#[cfg(test)]
mod tests {
    use super::*;

    fn test_search_insert() {
        let nums: Vec<i32> = vec![1, 3, 5, 6];
        let target: i32 = 5;
        let res = search_insert(nums, target);
        assert!(res == 2 as i32);
    }
}
