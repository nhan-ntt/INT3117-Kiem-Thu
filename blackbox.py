
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

import pytest

@pytest.mark.parametrize(
    "x, y, expected_output",
    [ 
        (950, 2000, "invalid input"), 
        (850, 200, "invalid input"),  
        (600000, 400, "invalid input"), 
        (800000, 600, "invalid input"),
        (10000, 3000, "invalid input"),  
        (20000, 150, 3050000),
        (30000, 450, 11525000),
        (40000, 650, 20800000)
    ]
)
def test_calculate_total_cost(x, y, expected_output):
    result = calculate_total_cost(x, y)
    print(f"Test case with x={x}, y={y}: expected {expected_output}, got {result}")
    assert result == expected_output

# Running the tests
if __name__ == "__main__":
    pytest.main()

