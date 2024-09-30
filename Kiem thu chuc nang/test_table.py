from calculate import calculate_total_cost

import pytest

# Test cases for decision table testing
@pytest.mark.parametrize(
    "x, y, expected_output",
    [
        (999, 2000, "invalid input"), 
        (850, 200, "invalid input"),  
        (600000, 400, "invalid input"),  
        (800000, 600, "invalid input"),  
        (10000, 3000, "invalid input"),  
        (20000, 150, 3050000),  
        (30000, 450, 11525000), 
        (40000, 650, 20800000),
    ]
)


def test_calculate_total_cost(x, y, expected_output):
    result = calculate_total_cost(x, y)
    print(f"Test case with x={x}, y={y}: expected {expected_output}, got {result}")
    assert result == expected_output

if __name__ == "__main__":
    pytest.main()