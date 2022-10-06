from assertpy import assert_that, soft_assertions
from mini_calculator import MiniCalculator


def test_sum():
    mini_calculator = MiniCalculator()
    with soft_assertions():
        assert_that(mini_calculator.sum(5, 6)).is_equal_to(11)
        assert_that(mini_calculator.sum(5, 5)).is_equal_to(10)
        assert_that(mini_calculator.sum(0, 0)).is_equal_to(0)
        assert_that(mini_calculator.sum(8, 0)).is_equal_to(8)


def test_diff():
    mini_calculator = MiniCalculator()
    with soft_assertions():
        assert_that(mini_calculator.diff(5, 6)).is_equal_to(-1)
        assert_that(mini_calculator.diff(5, 5)).is_equal_to(0)
        assert_that(mini_calculator.diff(0, 0)).is_equal_to(0)
        assert_that(mini_calculator.diff(8, 0)).is_equal_to(8)
        assert_that(mini_calculator.diff(0, 7)).is_equal_to(-7)
        assert_that(mini_calculator.diff(10, 7)).is_equal_to(3)


def test_multuply():
    mini_calculator = MiniCalculator()
    with soft_assertions():
        assert_that(mini_calculator.multiply(5, 6)).is_equal_to(30)
        assert_that(mini_calculator.multiply(10, 15)).is_equal_to(150)
        assert_that(mini_calculator.multiply(4, 4)).is_equal_to(16)
        assert_that(mini_calculator.multiply(5, 100)).is_equal_to(500)
        assert_that(mini_calculator.multiply(14, 11)).is_equal_to(154)


def test_divide():
    mini_calculator = MiniCalculator()
    with soft_assertions():
        assert_that(mini_calculator.divide(10, 5)).is_equal_to(2)
        assert_that(mini_calculator.divide(200, 25)).is_equal_to(8)
        assert_that(mini_calculator.divide(155, 10)).is_equal_to(15.5)
        assert_that(mini_calculator.divide(20, 4)).is_equal_to(5)
        assert_that(mini_calculator.divide(350, 5)).is_equal_to(70)
