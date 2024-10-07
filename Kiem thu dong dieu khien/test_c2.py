from calculate import calculate_total_cost

import pytest


@pytest.mark.parametrize(
    "x, y, expected_output",
    [
        (500, 2000, "invalid input"), 
        (2000, 200, 450000),  
        (10000, 450, 3875000),  
        (100000, 800, 64000000),  
    ]
)

def test_calculate_total_cost(x, y, expected_output):
    result = calculate_total_cost(x, y)
    print(f"Test case with x={x}, y={y}: expected {expected_output}, got {result}")
    assert result == expected_output

if __name__ == "__main__":
    pytest.main()