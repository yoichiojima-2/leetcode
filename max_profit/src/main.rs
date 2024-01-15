#[allow(unused_variables)]

fn solution(prices: Vec<i32>) -> i32 {
    let mut min_price = prices[0];
    let mut max_profit = 0;
    for price in prices {
        max_profit = std::cmp::max(max_profit, price - min_price);
        min_price = std::cmp::min(min_price, price);
    }
    max_profit
}

fn main() {
    let prices: Vec<i32> = vec![7, 1, 5, 3, 6, 4];
    solution(prices);
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test1() {
        let prices: Vec<i32> = vec![7, 1, 5, 3, 6, 4];
        let res = solution(prices);
        assert_eq!(res, 5 as i32)
    }
}