from unittest import TestCase
import pytest
from solver import add, square_equation_solver, TYPE_ERROR_TEXT

@pytest.mark.parametrize("args, excpected_result", [
    ((1,2 ), 3),
    (("foo", "bar"), "foobar"),
])
def test_add(args, excpected_result):
    res = add(*args)
    assert res== excpected_result


# unit test
class TestAddCase(TestCase):
    def test_ok(self):
        res = add(1, 2)
        self.assertEqual(res, 3)



class TestSquareEquationSolverUnittest(TestCase):
    def test_raises_type_error(self):
        with self.assertRaises(TypeError):  # Проверяем на то какую ошибку вернет.
            square_equation_solver('', 1, 1.4)

    def test_result_is_tuple(self):
        "Проверка на tuple"
        res = square_equation_solver(0, 0, 0)
        self.assertIsInstance(res, tuple)


    def test_no_results(self):
        "Проверка на возврат None"
        res = square_equation_solver(0, 0, 1)
        self.assertEqual(res, (None, None))

    def test_solver_ok(self):
        res = square_equation_solver(1, -3, -4)
        self.assertEqual(res, (4, -1))

class TestSquareEquationSolver:
    def test_raises_type_error(self):
        with pytest.raises(TypeError) as exp_info: # Проверяем поднято ли у нас исключение.
            square_equation_solver('', 1, 1.4)
        assert str(exp_info.value) == TYPE_ERROR_TEXT  # Проверяем правильное ли нам вернулось исключения.

    def test_result_is_tuple(self):
        "Проверка на tuple"
        res = square_equation_solver(0, 0, 0)
        assert isinstance(res, tuple)

    # У нас есть повторяющиеся элементы можно применить цикл, но при первом сломаном цикле, мы дальше не пойдем.
    # Поэтому нам нужно применить параметризацию. Чтобы передать параметры вешаем декоратор и в него передаем.
    # Он будет запускаться одельно для все строчек.
    # @pytest.mark.parametrize("args, expected_result", [((1,-3,-4), (4, -1)),((0,0,1), (None, None)),])
    # Делаем тесты с айди
    @pytest.mark.parametrize("args, expected_result", [
        pytest.param((1,-3,-4), (4, -1), id='general'),
        pytest.param((0,0,1), (None, None), id='No results'),
    ])
    def test_solves_ok(self, args, expected_result):
        res = square_equation_solver(*args)
        assert res == expected_result