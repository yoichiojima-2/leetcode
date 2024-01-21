fn solution(strs: Vec<&str>) -> String {
    if strs.len() == 0 {
        return String::from("");
    }
    if strs.len() == 1 {
        return strs[0].to_string();
    }
    let min_length = strs.iter().map(|x| x.len()).min().unwrap_or(0) as i32;
    for i in 0..min_length {
        for s in &strs {
            let char_a = &strs[0].chars().nth(i as usize).unwrap();
            let char_b = &s.chars().nth(i as usize).unwrap();
            if char_a != char_b {
                return strs[0][..i as usize].to_string();
            }
        }
    }
    strs[0][..min_length as usize].to_string()
}

fn main() {
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_1() {
        let res = solution(vec!["flower", "flow", "flight"]);
        assert_eq!(res, "fl");
    }

    #[test]
    fn test_2() {
        let res = solution(vec!["dog", "racecar", "car"]);
        assert_eq!(res, "");
    }

    #[test]
    fn test_3() {
        let res = solution(vec![""]);
        assert_eq!(res, "");
    }

    #[test]
    fn test_4() {
        let res = solution(vec!["a"]);
        assert_eq!(res, "a");
    }

    #[test]
    fn test_5() {
        let res = solution(vec!["ab", "a"]);
        assert_eq!(res, "a");
    }

    #[test]
    fn test_6() {
        let res = solution(vec!["flower", "flower", "flower", "flower", "flower"]);
        assert_eq!(res, "flower");
    }
}
