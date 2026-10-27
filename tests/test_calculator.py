# tests/test_calculator.py
import pytest
from src.calculator import add, divide, multiply

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    # 驗證除以 0 是否會正確拋出 ValueError
    with pytest.raises(ValueError, match="除數不可為 0"):
        divide(5, 0)
# 在檔案末尾加上：
def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 100) == 0        