#[allow(dead_code, unused_mut, unused_variables, unused_assignments)]

fn solution(nums: &mut Vec<i32>) -> i32 {
    let mut current_num = nums[0];
    let mut index = 1;
    loop {
        println!("index {}", index);
        if nums[index] == current_num {
            nums[index] = nums[index + 1];
            println!("swapped. {:?}", nums);
            index += 1;
        } else {
            current_num += nums[index + 1];
        }
        if nums[index] > nums[index + 1] {
            break
        }
    }
    index as i32 
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
