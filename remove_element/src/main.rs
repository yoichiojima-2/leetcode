fn solution(nums: &mut Vec<i32>, val: i32) -> i32 {
    let mut ins_idx = 0;
    for i in 0..nums.len() {
        if nums[i] != val {
            nums[ins_idx] = nums[i];
            ins_idx += 1;
        }
    }
    ins_idx as i32 
}

fn main() {
    let mut nums: Vec<i32> = vec![3, 2, 2, 3];
    let val: i32 = 3;
    let result: i32 = solution(&mut nums, val);
    println!("{:?}", result);
}
