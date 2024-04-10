fn main() {

}

#[derive(Debug)]
struct ListNode {
    val: i32,
    next: Option<Box<ListNode>>
}

impl ListNode {
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

type List = Option<Box<ListNode>>;

fn merge_two_sorted_lists(list1: List, list2: List) -> List {

}

#[cfg(test)]
mod tests {
    use super::*;

    fn array_to_list(array: Vec<i32>) -> List {
        for i in array {
            println!("{:?}", i);
        }
    }

    #[test]
    fn tests_1() {
        let list_1: Vec<i32> = [1, 2, 4];
        array_to_list(list_1);
    }

    #[test]
    fn tests_2() {
        // list_1 = [1, 3, 4]
    }
}
