fn solution(nums1: &mut Vec<i32>, m: i32, nums2: Vec<i32>, n: i32) {
    let i = m as i32 - 1;
    let j = n as i32 -1;
    let k = m + n;
    println!("nums1: {:?}", nums1);
    println!("nums2: {:?}", nums2);
    println!("indexes: {:?}", vec![i, j, k]);
}

fn main() {
    let mut nums1: Vec<i32> = vec![1 ,2 ,3 ,0 ,0 ,0];
    let nums2: Vec<i32> = vec![2, 5, 6];
    solution(&mut nums1, 3, nums2, 3);
}