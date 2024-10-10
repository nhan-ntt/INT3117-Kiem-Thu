def calculate_total_cost(x, y):
    shipping = 50000

    if not (1000 <= x <= 500000) or not (1 <= y <= 1000):
        return "invalid input"

    if 1 <= y < 300:  # No discount
        return x * y + shipping
    elif 300 <= y < 500:  # 15% discount
        return x * y * 0.85 + shipping
    elif 500 <= y <= 1000:  # 20% discount and free shipping
        return x * y * 0.80
