import unittest


def formatted_name(first_name, last_name, middle_name=''):
    if len(middle_name) <= 0:
        full_name = first_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()


class TestFormattedName(unittest.TestCase):
    def test_without_middle_name(self):
        result = formatted_name("nikita", "drobot")
        self.assertEqual(result, "Nikita Drobot")
        self.assertIsInstance(result, str)

    def test_full_name(self):
        result = formatted_name("nikita", "drobot", "smith")
        self.assertEqual(result, "Nikita Smith Drobot")
        self.assertIsInstance(result, str)

    def test_with_empty_middle_name(self):
        result = formatted_name("nikita", "drobot", "")
        self.assertEqual(result, "Nikita Drobot")
        self.assertIsInstance(result, str)

    def test_just_with_first_name(self):
        result = formatted_name("nikita", "", "")
        self.assertEqual(result, "Nikita ")
        self.assertIsInstance(result, str)

    def test_just_with_last_name(self):
        result = formatted_name("", "drobot", "")
        self.assertEqual(result, " Drobot")
        self.assertIsInstance(result, str)

    def test_just_with_middle_name(self):
        result = formatted_name("", "", "smith")
        self.assertEqual(result, " Smith ")
        self.assertIsInstance(result, str)

    def test_without_all_parameters(self):
        result = formatted_name("", "", "")
        self.assertEqual(result, " ")
        self.assertIsInstance(result, str)

    def test_with_different_input_registers(self):
        result = formatted_name("nIkItA", "DrObOt", "sMiTh")
        self.assertEqual(result, "Nikita Smith Drobot")
        self.assertIsInstance(result, str)

    def test_invalid_int_input(self):
        with self.assertRaises(TypeError):
            formatted_name((22, "drobot"))

    def test_invalid_list_input(self):
        with self.assertRaises(TypeError):
            formatted_name(("nikita", [], "smith"))

    def test_invalid_dict_input(self):
        with self.assertRaises(TypeError):
            formatted_name((dict(), "drobot", ''))

    def test_invalid_tuple_input(self):
        with self.assertRaises(TypeError):
            formatted_name(("nIkItA", tuple(), "sMiTh"))

    def test_invalid_float_input(self):
        with self.assertRaises(TypeError):
            formatted_name((22.4, "", ""))

    def test_invalid_bool_input(self):
        with self.assertRaises(TypeError):
            formatted_name(("", True, ""))
