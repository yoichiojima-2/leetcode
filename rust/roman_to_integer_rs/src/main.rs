use std::collections::HashMap;

#[allow(unused_variables, unused_mut)]
fn solution(s: String) -> i32 {
    let symbols = HashMap::from([
        ('I', 1),
        ('V', 5),
        ('X', 10),
        ('L', 50),
        ('C', 100),
        ('D', 500),
        ('M', 1000),
    ]);
    let mut roman: i32 = 0;
    for i in 0..s.len() {
        if let Some(letter) = s.chars().nth(i) {
            if let Some(cur_num) = symbols.get(&letter) {
                if i < s.len() - 1 {
                    if let Some(next_letter) = s.chars().nth(i + 1) {
                        if let Some(next_num) = symbols.get(&next_letter) {
                            if cur_num < next_num {
                                roman -= cur_num;
                            } else {
                                roman += cur_num;
                            }
                        }
                    }
                } else {
                    roman += cur_num;
                }
            }
        }
    }
    roman
}

fn main() {
    let s = String::from("LVIII");
    let res = solution(s);
    println!("{:?}", res);
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test1() {
        let s = String::from("III");
        let res = solution(s);
        assert_eq!(res, 3 as i32)
    }
    #[test]
    fn test2() {
        let s = String::from("LVIII");
        let res = solution(s);
        assert_eq!(res, 58 as i32)
    }
    #[test]
    fn test3() {
        let s = String::from("MCMXCIV");
        let res = solution(s);
        assert_eq!(res, 1994 as i32)
    }
}
