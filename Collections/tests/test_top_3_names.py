import unittest
from parameterized import parameterized
from Collections.top_3_names import get_top_3_names


class TestSuperTeacher(unittest.TestCase):
    @parameterized.expand(
        [
            (
                "unique_names_only",
                [
                    ["Евгений Шмаргунов", "Олег Булыгин"],
                    ["Филипп Воронов"],
                ],
                "Евгений: 1 раз(а), Олег: 1 раз(а), Филипп: 1 раз(а)",
            ),
            (
                "repeated_names_only",
                [
                    ["Евгений Шмаргунов", "Олег Булыгин"],
                    ["Филипп Воронов", "Евгений Шмаргунов"],
                    ["Евгений Шлейко", "Алена Батицкая", "Олег Ежков"],
                ],
                "Евгений: 3 раз(а), Олег: 2 раз(а), Алена: 1 раз(а)",
            ),
        ]
    )
    def test_super_teachers(self, name, mentors, expected):
        result = get_top_3_names(mentors)
        self.assertEqual(result, expected)
