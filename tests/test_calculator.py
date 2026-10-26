# tests/test_calculator.py
import pytest
from src.calculator import add, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    # 驗證除以 0 是否會正確拋出 ValueError
    with pytest.raises(ValueError, match="除數不可為 0"):
        divide(5, 0)