fn solution(s: String) -> i32 {
    let mut first_word_found = false;
    let mut count: i32 = 0;
    for c in s.chars().rev() {
        if first_word_found {
            if c != ' ' {
                count += 1;
            } else {
                return count;
            }
        } else if c != ' ' {
            first_word_found = true;
            count += 1;
        }
    }
    count
}

fn main() {
    let res = solution(String::from("Hello World"));
    println!("{:?}", res);
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_1() {
        let res = solution(String::from("Hello World"));
        assert_eq!(res, 5)
    }

    #[test]
    fn test_2() {
        let res = solution(String::from("   fly me   to   the moon  "));
        assert_eq!(res, 4)
    }

    #[test]
    fn test_3() {
        let res = solution(String::from("luffy is still joyboy"));
        assert_eq!(res, 6)
    }
}