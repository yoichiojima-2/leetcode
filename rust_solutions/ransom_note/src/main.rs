// 383. Ransom Note

// Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
// Each letter in magazine can only be used once in ransomNote.

// Example 1:
// Input: ransomNote = "a", magazine = "b"
// Output: false

// Example 2:
// Input: ransomNote = "aa", magazine = "ab"
// Output: false

// Example 3:
// Input: ransomNote = "aa", magazine = "aab"
// Output: true

#[allow(dead_code, unused_variables)]
use std::collections::HashMap;


fn solution(ransom_note: &str, magazine: &str) -> bool {
    let mut counter = HashMap::new();
    for ch in magazine.chars() {
        *counter.entry(ch).or_insert(0) += 1;
    }
    for ch in ransom_note.chars() {
        let count = counter.entry(ch).or_insert(0);
        if *count == 0 {
            return false;
        }
        *count -= 1;
    }
    true
}

fn main() {
    println!("{:?}", solution("a", "b"));
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_1() {
        assert!(!solution("a", "b"));
    }

    #[test]
    fn test_2() {
        assert!(!solution("aa", "ab"));
    }

    #[test]
    fn test_3() {
        assert!(solution("aa", "aab"));
    }
}