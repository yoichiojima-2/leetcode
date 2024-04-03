fn main() {

}

fn valid_parentheses(s: String) -> bool {
    println!("input: {:?}", s);

    let mut stack: Vec<char> = vec![];

    for c in s.chars() {
        println!("{:?}", c);
        match c {
            '(' | '[' | '{' => stack.push(c),
            ')' => if stack.pop() != Some('(') { return false; },
            ']' => if stack.pop() != Some('[') { return false; },
            '}' => if stack.pop() != Some('{') { return false; },
            _ => {}
        }
    }
    stack.is_empty()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let s = String::from("()");
        assert!(valid_parentheses(s));
    }

    #[test]
    fn test_2() {
        let s = String::from("()[]{}");
        assert!(valid_parentheses(s));
    }

    #[test]
    fn test_3() {
        let s = String::from("(]");
        assert!(!valid_parentheses(s));
    }
}
