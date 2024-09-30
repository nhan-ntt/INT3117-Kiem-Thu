from calculate import calculate_total_cost

import pytest

# Test cases for boundary value testing
@pytest.mark.parametrize(
    "x, y, expected_output",
    [
        (1000, 500, 400000),  
        (500000, 500, 200000000),  
        (1001, 500, 400400), 
        (499999, 500, 199999600),  
        (999, 500, "invalid input"), 
        (500001, 500, "invalid input"),  
        (250000, 1, 300000),  
        (250000, 1000, 200000000),  
        (250000, 2, 550000),  
        (250000, 999, 199800000),  
        (250000, 0, "invalid input"), 
        (250000, 1001, "invalid input"),
        (250000, 500, 100000000),  
    ]
)

def test_calculate_total_cost(x, y, expected_output):
    result = calculate_total_cost(x, y)
    print(f"Test case with x={x}, y={y}: expected {expected_output}, got {result}")
    assert result == expected_output

if __name__ == "__main__":
    pytest.main()