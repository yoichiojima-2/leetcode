fn solution(s: String, t: String) -> bool {
    if s.is_empty() {
        return true;
    }
    
    let mut s_chars = s.chars();
    let mut next_s_char = s_chars.next();

    for c in t.chars() {
        if let Some(expected_char) = next_s_char {
            if c == expected_char {
                next_s_char = s_chars.next();
                if next_s_char.is_none() {
                    return true; 
                }
            }
        } else {
            break;
        }
    }
    
    false
}

fn main() {
    solution(String::from("abc"), String::from("ahbgdc"));
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_1(){
        let res = solution(String::from("abc"), String::from("ahbgdc"));
        assert!(res);
    }

    #[test]
    fn test_2(){
        let res = solution(String::from("axc"), String::from("ahbgdc"));
        assert!(!res);
    }
}
