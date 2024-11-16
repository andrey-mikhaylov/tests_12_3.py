import unittest
from HumanMoveTest.runner_and_tournament import Runner, Tournament


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        """
        тест метода walk
        создаётся объект класса Runner с произвольным именем.
        Далее вызовите метод walk у этого объекта 10 раз.
        После чего методом assertEqual сравните distance этого объекта со значением 50.
        """
        runner = Runner('name')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        """
        тест метода run
        создаётся объект класса Runner с произвольным именем.
        Далее вызовите метод run у этого объекта 10 раз.
        После чего методом assertEqual сравните distance этого объекта со значением 100.
        """
        runner = Runner('name')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        """
        совместный тест методов run и walk
        test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами.
        Далее 10 раз у объектов вызываются методы run и walk соответственно.
        Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
        """
        runner1 = Runner('name1')
        runner2 = Runner('name1')
        for _ in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        создаётся атрибут класса all_results.
        Это словарь в который будут сохраняться результаты всех тестов.
        """
        cls.all_results = {}

    def setUp(self):
        """ создаются 3 объекта Runner """
        self.runners = [
            Runner("Усэйн", 10),
            Runner("Андрей", 9),
            Runner("Ник", 3),
        ]

    @classmethod
    def tearDownClass(cls):
        """ выводятся all_results по очереди в столбец. """
        for tournament, results in cls.all_results.items():
            print(f'{tournament}: {{{', '.join([f'{place}: {name}' for place, name in results.items()])}}}')

    def __test_tournament(self, distance:int, *people:str):
        participants = [runner for runner in self.runners if runner in people]
        tournament = Tournament(distance, *participants)
        # У объекта класса Tournament запускается метод start,
        # который возвращает словарь в переменную all_results.
        return tournament.start()

    # методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90.
    # Ник всегда должен быть последним.
    def test_tournament1(self):
        """ тест tournament для двух участников """
        results = self.__test_tournament(90, 'Усэйн', 'Ник')
        self.all_results['1'] = results
        self.assertTrue(results[max(results)] == 'Ник')

    def test_tournament2(self):
        """ тест tournament для двух других участников """
        results = self.__test_tournament(90, 'Андрей', 'Ник')
        self.all_results['2'] = results
        self.assertTrue(results[max(results)] == 'Ник')

    def test_tournament3(self):
        """ тест tournament для трех участников """
        results = self.__test_tournament(90, 'Усэйн', 'Андрей', 'Ник')
        self.all_results['3'] = results
        self.assertTrue(results[max(results)] == 'Ник')

    """
    В данной задаче, а именно в методе start класса Tournament, допущена логическая ошибка. 
    В результате его работы бегун с меньшей скоростью может пробежать некоторые дистанции быстрее, 
    чем бегун с большей. Попробуйте решить эту проблему и обложить дополнительными тестами.
    """
    def test_tournament4(self):
        """ тест исправления ошибки в tournament.start """
        results = self.__test_tournament(5, 'Усэйн', 'Андрей', 'Ник')
        self.all_results['4'] = results
        self.assertTrue(results[len(results)] == 'Ник')


if __name__ == '__main__':
    unittest.main()
    """
    Вывод на консоль:
    {1: Усэйн, 2: Ник}
    {1: Андрей, 2: Ник}
    {1: Андрей, 2: Усэйн, 3: Ник}
    """


"""
2024/01/11 00:00|Домашнее задание по теме "Систематизация и пропуск тестов".
Цель: понять на практике как объединять тесты при помощи TestSuite. Научиться пропускать тесты при помощи встроенных в unittest декораторов.

Задача "Заморозка кейсов":
Подготовка:
В этом задании используйте те же TestCase, что и в предыдущем: RunnerTest и TournamentTest.
Часть 1. TestSuit.
Создайте модуль suite_12_3.py для описания объекта TestSuite. Укажите на него переменной с произвольным названием.
Добавьте тесты RunnerTest и TournamentTest в этот TestSuit.
Создайте объект класса TextTestRunner, с аргументом verbosity=2.
Часть 2. Пропуск тестов.
Классы RunnerTest дополнить атрибутом is_frozen = False и TournamentTest атрибутом is_frozen = True.
Напишите соответствующий декоратор к каждому методу (кроме @classmethod), который при значении is_frozen = False будет выполнять тесты, а is_frozen = True - пропускать и выводить сообщение 'Тесты в этом кейсе заморожены'.
Таким образом вы сможете контролировать пропуск всех тестов в TestCase изменением всего одного атрибута.
Запустите TestSuite и проверьте полученные результаты тестов из обоих TestCase.
Пример результата выполнения тестов:
Вывод на консоль:
test_challenge (tests_12_3.RunnerTest.test_challenge) ... ok
test_run (tests_12_3.RunnerTest.test_run) ... ok
test_walk (tests_12_3.RunnerTest.test_walk) ... ok
test_first_tournament (tests_12_3.TournamentTest.test_first_tournament) ... skipped 'Тесты в этом кейсе заморожены'
test_second_tournament (tests_12_3.TournamentTest.test_second_tournament) ... skipped 'Тесты в этом кейсе заморожены'
test_third_tournament (tests_12_3.TournamentTest.test_third_tournament) ... skipped 'Тесты в этом кейсе заморожены'
----------------------------------------------------------------------
Ran 6 tests in 0.000s OK (skipped=3)

Файлы suite_12_3.py и tests_12_3.py, где произошли изменения загрузите на ваш GitHub репозиторий. В решении пришлите ссылку на него.
"""
