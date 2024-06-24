# Using pytest for testing

from grscheller_courses_distributions.binomial import Binomial

class Test_Binomial:

    def test_initialization(self) -> None:
        self.binomial = Binomial(0.4, 20)
        self.binomial.read_data_file('data/numbers_binomial.txt')
        assert self.binomial.p == 0.4
        assert self.binomial.n == 20

    def test_readdata(self) -> None:
        self.binomial = Binomial(0.4, 20)
        self.binomial.read_data_file('data/numbers_binomial.txt')
        assert self.binomial.data == [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0]

    def test_calculate_mean(self) -> None:
        self.binomial = Binomial(0.4, 20)
        self.binomial.read_data_file('data/numbers_binomial.txt')
        mean = self.binomial.calculate_mean()
        assert mean == 8

    def test_calculate_stdev(self) -> None:
        self.binomial = Binomial(0.4, 20)
        self.binomial.read_data_file('data/numbers_binomial.txt')
        stdev = self.binomial.calculate_stdev()
        assert round(stdev,2) == 2.19

    def test_replace_stats_with_data(self) -> None:
        self.binomial = Binomial(0.4, 20)
        self.binomial.read_data_file('data/numbers_binomial.txt')
        p, n = self.binomial.replace_stats_with_data()
        assert round(p, 3) == .615
        assert n == 13

    def test_pdf(self) -> None:
        self.binomial = Binomial(0.4, 20)
        self.binomial.read_data_file('data/numbers_binomial.txt')
        assert round(self.binomial.pdf(5), 5) == 0.07465
        assert round(self.binomial.pdf(3), 5) == 0.01235

        self.binomial.replace_stats_with_data()
        assert round(self.binomial.pdf(5), 5) == 0.05439
        assert round(self.binomial.pdf(3), 5) == 0.00472

    def test_add(self) -> None:
        self.binomial = Binomial(0.4, 20)
        self.binomial.read_data_file('data/numbers_binomial.txt')
        binomial_one = Binomial(0.4, 20)
        binomial_two = Binomial(0.4, 60)
        binomial_sum = binomial_one + binomial_two

        assert binomial_sum.p == 0.4
        assert binomial_sum.n == 80
