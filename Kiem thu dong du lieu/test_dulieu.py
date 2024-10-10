from calculate import calculate_total_cost

import pytest


@pytest.mark.parametrize(
    "x, y, expected_output",
    [
        (1, 1, "invalid input"), 
        (1000, 100, 150000),  
        (1000, 100, 150000),  
        (1000, 300, 305000),  
        (1000, 1000, 800000),  
        (1, 1, "invalid input"), 
        (1000, 100, 150000),  
        (1000, 100, 150000),  
        (1000, 300, 305000),  
        (1000, 300, 305000),  
        (1000, 1000, 800000),  
        (1000, 100, 150000),  
        (1000, 300, 305000),  
        (1000, 1000, 800000), 
    ]
)

def test_calculate_total_cost(x, y, expected_output):
    result = calculate_total_cost(x, y)
    print(f"Test case with x={x}, y={y}: expected {expected_output}, got {result}")
    assert result == expected_output

if __name__ == "__main__":
    pytest.main()