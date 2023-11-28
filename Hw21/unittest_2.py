import unittest


def formatted_name(first_name, last_name, middle_name=''):
    if len(middle_name) <= 0:
        full_name = first_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()


class TestFormattedName(unittest.TestCase):
    def test_valid_inputs(self):
        cases = {
            formatted_name("nikita", "drobot"): "Nikita Drobot",
            formatted_name("nikita", "drobot", "smith"): "Nikita Smith Drobot",
            formatted_name("nikita", "drobot", ""): "Nikita Drobot",
            formatted_name("nIkItA", "DrObOt", "sMiTh"): "Nikita Smith Drobot",
            formatted_name("nikita", "", ""): "Nikita ",
            formatted_name("", "", ""): " ",
            formatted_name("", "drobot", ""): " Drobot",
            formatted_name("", "", "smith"): " Smith "
        }
        for input_value, expected_result in cases.items():
            with self.subTest(n=input_value):
                result = input_value
                self.assertEqual(result, expected_result)
                self.assertIsInstance(result, str)

    def test_invalid_type(self):
        input_list = [
            (22, "drobot"),
            ("nikita", [], "smith"),
            (dict(), "drobot", ''),
            ("nIkItA", tuple(), "sMiTh"),
            (22.4, "", ""),
            ("", True, ""),
            (False, "drobot", ""),
        ]
        for input_value in input_list:
            with self.subTest(n=input_value):
                with self.assertRaises(TypeError):
                    formatted_name(input_value)
