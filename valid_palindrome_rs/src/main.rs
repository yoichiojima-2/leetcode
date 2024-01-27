fn solution(s: String) -> bool{
    let chars: String = s.chars()
        .filter(|c| c.is_alphanumeric())
        .map(|c| c.to_ascii_lowercase())
        .collect();
    if chars.is_empty() {
        return true
    }

    let rev_chars:String = chars.chars().rev().collect();
    chars == rev_chars
}

fn main() {
    solution(String::from("A man, a plan, a canal: Panama"));
}

#[cfg(test)]
mod test {
    use super::*;
    #[test]
    fn test_1() {
        assert!(solution(String::from("A man, a plan, a canal: Panama")));
    }
    #[test]
    fn test_2() {
        assert!(!solution(String::from("race a car")));
    }
    #[test]
    fn test_3() {
        assert!(solution(String::from(" ")));
    }
    #[test]
    fn test_4() {
        assert!(solution(String::from("aa")));
    }
}