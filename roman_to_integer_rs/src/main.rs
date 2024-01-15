#[allow(unused_variables, dead_code, unused_mut)]

use std::collections::HashMap;

fn solution(s: String) -> i32 {
    32 as i32
}

fn main() {
    let s = String::from("LVIII");
    let res = solution(s);
    println!("{:?}", res);
}

#[cfg(test)]
#[allow(unused_variables, dead_code)]
mod test {
    use super::*;
    #[test]
    fn test1() {
        let s = String::from("III");
        let res = solution(s);
        assert_eq!(res, 3 as i32)
    }
    fn test2() {
        let s = String::from("LVIII");
        let res = solution(s);
        assert_eq!(res, 58 as i32)
    }
    fn test3() {
        let s = String::from("MCMXCIV");
        let res = solution(s);
        assert_eq!(res, 1994 as i32)
    }
}