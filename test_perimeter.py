import pytest
from calculate_primeter import perimeter  

def test_perimeter_valid():
    assert perimeter(3, 4) == 14  # Normal case

def test_perimeter_zero():
    assert perimeter(0, 5) == 10  # Zero length, valid case

def test_perimeter_negative_length():
    with pytest.raises(ValueError, match='Dimension cannot be negative'):
        perimeter(-1, 5)  # Negative length

def test_perimeter_negative_breadth():
    with pytest.raises(ValueError, match='Dimension cannot be negative'):
        perimeter(5, -1)  # Negative breadth

def test_perimeter_none_length():
    with pytest.raises(ValueError, match='Undefined'):
        perimeter(None, 5)  # Length is None

def test_perimeter_none_breadth():
    with pytest.raises(ValueError, match='Undefined'):
        perimeter(5, None)  # Breadth is None

def test_perimeter_non_number_length():
    with pytest.raises(TypeError, match='Not a number'):
        perimeter("three", 4)  # Non-number length

def test_perimeter_non_number_breadth():
    with pytest.raises(TypeError, match='Not a number'):
        perimeter(3, "four")  # Non-number breadth