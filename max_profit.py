def solution(prices: list[int]) -> int:
    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
    return max_profit
    
def main():
    prices = [7,1,5,3,6,4]
    res = solution(prices)
    print(res)

if __name__ == "__main__":
    main()
