import unittest
from parameterized import parameterized
from Collections.super_teacher import get_super_teacher


class TestSuperTeacher(unittest.TestCase):
    @parameterized.expand(
        [
            (
                "two_courses without super_teacher",
                [
                    ["Евгений Шмаргунов", "Олег Булыгин"],
                    ["Филипп Воронов", "Анна Юшина"],
                ],
                ["Python-разработчик с нуля", "Java-разработчик с нуля"],
                [
                    "На курсах 'Python-разработчик с нуля' и 'Java-разработчик с нуля' преподают: "
                ],
            ),
            (
                "two_courses with super_teacher",
                [
                    ["Евгений Шмаргунов", "Олег Булыгин"],
                    ["Филипп Воронов", "Анна Юшина", "Олег Булыгин"],
                ],
                ["Python-разработчик с нуля", "Java-разработчик с нуля"],
                [
                    "На курсах 'Python-разработчик с нуля' и 'Java-разработчик с нуля' преподают: Олег"
                ],
            ),
            (
                "tree_courses with super_teacher",
                [
                    ["Евгений Шмаргунов", "Олег Булыгин"],
                    ["Филипп Воронов", "Анна Юшина"],
                    ["Александр Бардин", "Александр Иванов"],
                ],
                [
                    "Python-разработчик с нуля",
                    "Java-разработчик с нуля",
                    "Fullstack-разработчик на Python",
                ],
                [
                    "На курсах 'Python-разработчик с нуля' и 'Java-разработчик с нуля' преподают: ",
                    "На курсах 'Python-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: ",
                    "На курсах 'Java-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: ",
                ],
            ),
            (
                "two_courses without super_teacher",
                [
                    ["Евгений Шмаргунов", "Олег Булыгин"],
                    ["Евгений Шмаргунов", "Анна Юшина", "Александр Иванов"],
                    ["Александр Бардин", "Александр Иванов", "Олег Булыгин"],
                ],
                [
                    "Python-разработчик с нуля",
                    "Java-разработчик с нуля",
                    "Fullstack-разработчик на Python",
                ],
                [
                    "На курсах 'Python-разработчик с нуля' и 'Java-разработчик с нуля' преподают: Евгений",
                    "На курсах 'Python-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: Олег",
                    "На курсах 'Java-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: Александр",
                ],
            ),
        ]
    )
    def test_super_teachers(self, name, mentors, courses, expected):
        result = get_super_teacher(mentors, courses)
        self.assertEqual(result, expected)
