fn is_palindrome(x: i32) -> bool {
    let x_str = x.to_string();
    let rev_x_str: String = x_str.chars().rev().collect();
    x_str == rev_x_str
}

fn main() {
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_ispalindrome_1() {
        let x: i32 = 121;
        assert!(is_palindrome(x));
    }

    #[test]
    fn test_ispalindrome_2() {
        let x: i32 = -121;
        assert!(!is_palindrome(x));
    }

    #[test]
    fn test_ispalindrome_3() {
        let x: i32 = 10;
        assert!(!is_palindrome(x));
    }
}
