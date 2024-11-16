import unittest
from HumanMoveTest.runner_and_tournament import Runner, Tournament


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        """
        test_walk - метод, в котором создаётся объект класса Runner с произвольным именем.
        Далее вызовите метод walk у этого объекта 10 раз.
        После чего методом assertEqual сравните distance этого объекта со значением 50.
        """
        runner = Runner('name')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        """
        test_run - метод, в котором создаётся объект класса Runner с произвольным именем.
        Далее вызовите метод run у этого объекта 10 раз.
        После чего методом assertEqual сравните distance этого объекта со значением 100.
        """
        runner = Runner('name')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        """
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
        results = self.__test_tournament(90, 'Усэйн', 'Ник')
        self.all_results['1'] = results
        self.assertTrue(results[max(results)] == 'Ник')

    def test_tournament2(self):
        results = self.__test_tournament(90, 'Андрей', 'Ник')
        self.all_results['2'] = results
        self.assertTrue(results[max(results)] == 'Ник')

    def test_tournament3(self):
        results = self.__test_tournament(90, 'Усэйн', 'Андрей', 'Ник')
        self.all_results['3'] = results
        self.assertTrue(results[max(results)] == 'Ник')

    """
    В данной задаче, а именно в методе start класса Tournament, допущена логическая ошибка. 
    В результате его работы бегун с меньшей скоростью может пробежать некоторые дистанции быстрее, 
    чем бегун с большей. Попробуйте решить эту проблему и обложить дополнительными тестами.
    """
    def test_tournament4(self):
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
2024/01/09 00:00|Домашнее задание по теме "Методы Юнит-тестирования"
Цель: освоить методы, которые содержит класс TestCase.

Задача:
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
В этом коде сможете обнаружить дополненный с предыдущей задачи класс Runner и новый класс Tournament.
Изменения в классе Runner:
Появился атрибут speed для определения скорости бегуна.
Метод __eq__ для сравнивания имён бегунов.
Переопределены методы run и walk, теперь изменение дистанции зависит от скорости.
Класс Tournament представляет собой класс соревнований, где есть дистанция, которую нужно пробежать и список участников. Также присутствует метод start, который реализует логику бега по предложенной дистанции.

Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:

setUpClass - метод, где создаётся атрибут класса all_results. Это словарь в который будут сохраняться результаты всех тестов.
setUp - метод, где создаются 3 объекта:
Бегун по имени Усэйн, со скоростью 10.
Бегун по имени Андрей, со скоростью 9.
Бегун по имени Ник, со скоростью 3.
tearDownClass - метод, где выводятся all_results по очереди в столбец.

Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90. У объекта класса Tournament запускается метод start, который возвращает словарь в переменную all_results. В конце вызывается метод assertTrue, в котором сравниваются последний объект из all_results (брать по наибольшему ключу) и предполагаемое имя последнего бегуна.
Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
Усэйн и Ник
Андрей и Ник
Усэйн, Андрей и Ник.
Как можно понять: Ник всегда должен быть последним.

Дополнительно (не обязательно, не влияет на зачёт):
В данной задаче, а именно в методе start класса Tournament, допущена логическая ошибка. В результате его работы бегун с меньшей скоростью может пробежать некоторые дистанции быстрее, чем бегун с большей.
Попробуйте решить эту проблему и обложить дополнительными тестами.
Пример результата выполнения тестов:
Вывод на консоль:
{1: Усэйн, 2: Ник}
{1: Андрей, 2: Ник}
{1: Андрей, 2: Усэйн, 3: Ник}

Ran 3 tests in 0.001s
OK

Примечания:
Ваш код может отличаться от строгой последовательности описанной в задании. Главное - схожая логика работы тестов и наличие всех перечисленных переопределённых методов из класса TestCase.
Файл tests_12_2.py c классами тестов загрузите на ваш GitHub репозиторий. В решении пришлите ссылку на него.
"""