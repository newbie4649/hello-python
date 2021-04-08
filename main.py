import unittest


class TestHelloWorld(unittest.TestCase):
    def test_何も指定してない場合は既定の挨拶を返す(self):
        self.assertEqual(hello_world(), 'Hello from Python')

    def test_指定された名前で挨拶を返す(self):
        self.assertEqual(hello_world('VSCode'), 'Hello from VSCode')


def hello_world(name="Python"):
    return f"Hello from {name}"


unittest.main(argv=[''], verbosity=2, exit=False)
