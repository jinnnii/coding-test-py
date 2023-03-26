def solution(price):
    sales = 1
    if price >= 500000:
        sales = 0.8
    elif price >= 300000:
        sales = 0.9
    elif price >= 100000:
        sales = 0.95
    return price*sales//1
