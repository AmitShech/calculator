import pytest
from  calculator import*
from exceptions import *

def test_empty_input_raises_error():
    with pytest.raises(EmptyInput):
        cal_expression("")

def test_white_space_input_raises_error():
    with pytest.raises(EmptyInput):
        cal_expression("           ")

def test_parenthesis_input_raises_error():
    with pytest.raises(UnbalanceParenthesis):
        cal_expression("(2+3")

@pytest.mark.parametrize("wrongSyntax", [
    "2+3-4&()",
    "5 *",
    "!2",
    "-",
    "12~",
    "4545...8",
    "4.8.7+9-(7%3$8)",
    "cr+4@1",
    "4i",
    ";;9",
    "4e10+8"
])
def test_empty_parenthesis_input(wrongSyntax):
    with pytest.raises(IncorrectSyntax):
        cal_expression(wrongSyntax)

@pytest.mark.parametrize("wrongFormat", [
    "2 + & 3",
    "2!2",
    "4@@4",
    "(6^)",
    "12#~3"
])
def test_incorrect_format_raises_error(wrongFormat):
    with pytest.raises(NotInFormat):
        cal_expression(wrongFormat)

def test_simple_op():
    assert cal_expression("2 + 2")==4
    assert cal_expression("2 - 2") == 0
    assert cal_expression("6 * 7") == 42
    assert cal_expression("2 / 2") == 1
    assert cal_expression("16 % 6") == 4
    assert cal_expression("2 & -2") == -2
    assert cal_expression("2 $ 2") == 2
    assert cal_expression("10@20") == 15
    assert cal_expression("123#") == 6
    assert cal_expression("4!") == 24
    assert cal_expression("~8") == -8
    assert cal_expression("-8") == -8
    assert cal_expression("5^3") == 125
    assert cal_expression("99") == 99

@pytest.mark.parametrize("expr, result", [
    ("(5 * (4 + 3 ^ 2) - 7) * (6 / 2) + (8 % 3) * 4 ^ 2 - (5 * 3) + 2! + 5$2 + ~3", 195),
    ("2 * (6 ^ 3 - 8 & 4) + (5 * 2 - 3) + 5 % 4 * (7 - 2) - 10 @ 5 + 3! + 5#", 439.5),
    ("-2 + (5 * 4 ^ 2 + 3 & 7) * 3 - 9 * 2 + (6 * 8 - 5) + 4! - 3$6 + ~5", 285),
    ("(7 * 6 - 4 ^ 2) & (5 * 2 ^ 3 + 10 % 3) * 3 - (8 + 3) + 3! * 5 @ 2 + ~4", 84),
    ("2 * (8 $ 4 ^ 2 - 6) + 3 ^ (4 - 2) - (2 % 5) * 3 + 7 - 6! + 3$7 + 5#", -582),
    ("(5 * 6 - 3 ^ 2) + (8 & 2 * 3) % 10 - (4 + 5) * 2 + 3! - 2 @ 3 + ~2", 10.5),
    ("4 ^ 3 + 2 * 5 - (8 % 6) * 3 + (7 * 2 - 3) + 10 @ 3 + 5$8 + ~3", 90.5),
    ("3 * (5 + 2 ^ 3 - 4 & 2) * 2 + 10 - (6 % 4) * 3 + 5! - 7$4 + 6#", 189),
    ("(2 ^ 4 + 5 * 3 - 7) & 3 * (6 - 2) + (10 % 4) * 3 - (2 + 7) + 6! + ~6", 723),
    ("8 % (3 + 7 * 5 ^ 2 - 6 ^ 2) + 3 & (5 * 2) - 4 + 2! + 5$3 + 4#", 18),
    ("(6 * 3 ^ 2 - 4 + 8) * (5 + 2) - (10 % 5) + 7 & 4 ^ 3 - 9 * 2 + 6!", 1172),
    ("(8 $ 5 ^ 3 + 6 * 2) + (3 - 7 % 2) * 2 + 5! + 6 @ 3 - 8 % 4", 652.5),
    ("9 * (4 ^ 2 + 2) - 3 % (5 * 2) + 10 @ 7 - 4 * 6 + 2! + 5$3", 150.5),
    ("5 + (8 * 3 ^ 2        - 6 % 4) * (7 & 2) + 3 @ 6 + 10 - 4 ^ 2", 143.5),
    ("(7 * 4 + 2) - 5 + 2 ^ 3 * (6 - 3) + 3$5 + 8 % 3 + ~7", 49),
    ("(5 & 6) * (4 + 3 ^ 2) + 10 % 6 - 2 @ 3 + (7 * 2) + 5!", 200.5),
    ("(3 * 7 ^ 2 - 4) + 8 @ 2 *         (5 - 9 % 4) + 6 + 5$3 - 4!", 150),
    ("6 * (4 ^ 3 + 5)    - (2 & 6) + 9 * 2 + 7 % 3 + 3$8 - 2!", 437),
    ("(8 + 6 ^ 2) * 3 - (5 & 3) + 9 @ 2 * 4 + 5 - 7 % 2", 155),
    ("5 ^ 4 + 2 * 3 - (6 & 8) * (4 + 5 % 7) + 10 @ 3 - 6!", -136.5)
])
def test_cal_complex_expression(expr, result):
    assert cal_expression(expr) == result

@pytest.mark.parametrize("expr, result", [ ("--3!",6), ("2--3!", NegativeInFactorial), ("~-5",5),("2+-(23-65)#", 8),
    ("2--0.3^4.5", RootToNegative), ("-4^0.5",-2)])

def test_sign_minus(expr, result):
    if isinstance(result, type) and issubclass(result, Exception):
        with pytest.raises(result):
            cal_expression(expr)
    else:
        assert cal_expression(expr) == result


def test_overflow():
    with pytest.raises(OverflowError):
        cal_expression("10!!!")

