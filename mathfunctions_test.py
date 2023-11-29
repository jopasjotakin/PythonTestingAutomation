import mathfunctions


class TestFunctions():

    def test_add(self):
        assert mathfunctions.add(2, 3) == 5

    def test_multiply(self):
        assert mathfunctions.multiply(4, 5) == 20

    def test_power(self):
        assert mathfunctions.power(2, 8) == 256
