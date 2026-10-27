# src/calculator.py

def add(a: float, b: float) -> float:
    """加法"""
    return a + b

def divide(a: float, b: float) -> float:
    """除法，若除以 0 則拋出例外"""
    if b == 0:
        raise ValueError("除數不可為 0")
    return a / b

def multiply(a: float, b: float) -> float:
    """乘法"""
    return a * b