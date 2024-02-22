fn solution(haystack: String, needle: String) -> i32 {
    let haystack_len = haystack.len();
    let needle_len = needle.len();
    if haystack_len < needle_len {
        return -1 as i32;
    }
    for i in 0..haystack_len  - needle_len + 1 {
        if haystack[i..i + needle_len] == needle {
            return i as i32
        }
    }
    -1 as i32 
}

fn main() {
}

#[cfg(test)]
mod test {
    use super::*;
    #[test]
    fn test_1() {
        let haystack = String::from("sadbutsad");
        let needle = String::from("sad");
        let res = solution(haystack, needle);
        assert_eq!(res, 0);
    }
    #[test]
    fn test_2() {
        let haystack = String::from("leetcode");
        let needle = String::from("leeto");
        let res = solution(haystack, needle);
        assert_eq!(res, -1)
    }
    #[test]
    fn test_3() {
        let haystack = String::from("abb");
        let needle = String::from("abaaa");
        let res = solution(haystack, needle);
        assert_eq!(res, -1);
    }
}