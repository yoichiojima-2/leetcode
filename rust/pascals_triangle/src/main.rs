
struct Solution;

impl Solution {
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        let mut res = vec![vec![1]];
        for _ in 0..num_rows - 1 {
            let last_row = &res[res.len() - 1];
            let mut row_to_add = vec![last_row[0]];
            for j in 0..last_row.len() - 1 {
                row_to_add.push(last_row[j] + last_row[j + 1]);
            }
            row_to_add.push(last_row[last_row.len() - 1]);
            res.push(row_to_add);
        }
        res
    }
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::generate(5), vec![vec![1], vec![1, 1], vec![1, 2, 1], vec![1, 3, 3, 1], vec![1, 4, 6, 4, 1]]);
    }
}