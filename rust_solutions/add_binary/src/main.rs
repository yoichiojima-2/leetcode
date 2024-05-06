fn main(a: String, b: String) -> String {
    let base: u128 = 2;
    let a = a.chars().rev().collect::<String>();
    let b = b.chars().rev().collect::<String>();

    let mut a_int: u128 = 0;
    for (i, c) in a.chars().enumerate() {
        let val = c as u128 - '0' as u128;
        a_int += base.pow(i as u32) * val;
    }

    let mut b_int: u128 = 0;
    for (i, c) in b.chars().enumerate() {
        let val = c as u128 - '0' as u128;
        b_int += base.pow(i as u32) * val;
    }
    
    let mut sum_int = a_int + b_int;

    if sum_int == 0 {
        return "0".to_string();
    }

    let mut res = "".to_string();
    while sum_int > 0 {
        let str_to_push = (sum_int % 2).to_string();
        res.push_str(&str_to_push);
        sum_int /= 2;
    }
    res.chars().rev().collect::<String>()
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_1() {
        let res = main("11".to_string(), "1".to_string());
        assert!(res == "100".to_string());
    }

    #[test]
    fn test_2() {
        let res = main("1010".to_string(), "1011".to_string());
        assert!(res == "10101".to_string());
    }

    #[test]
    fn test_3() {
        let a = "10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101".to_string();
        let b = "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011".to_string();
        let expected = "110111101100010011000101110110100000011101000101011001000011011000001100011110011010010011000000000".to_string();
        assert!(main(a, b) == expected);
    }

    #[test]
    fn test_4() {
        let a = "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111".to_string();
        let b = "1".to_string();
        let expected = "100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000".to_string();
        assert!(main(a, b) == expected);
    }
}
