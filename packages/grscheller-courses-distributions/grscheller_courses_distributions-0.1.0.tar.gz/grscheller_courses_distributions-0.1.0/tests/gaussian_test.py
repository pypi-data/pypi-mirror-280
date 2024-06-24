# Using pytest for testing

from grscheller_courses_distributions.gaussian import Gaussian

class Test_Gaussian:

    def test_initialization(self) -> None:
        gauss1 = Gaussian(30, 3)
        gauss2 = Gaussian()
        assert gauss1.mean == 30
        assert gauss1.stdev == 3
        assert not gauss1.data
        assert gauss2.mean == 0.0
        assert gauss2.stdev == 1.0
        assert not gauss2.data

    def test_readdata(self) -> None:
        gauss = Gaussian(25, 2)
        assert gauss.mean == 25
        assert gauss.stdev == 2
        assert not gauss.data
        gauss.read_data_file('data/numbers.txt')
        assert gauss.data
        assert gauss.data == [1, 3, 99, 100, 120, 32, 330, 23, 76, 44, 31]
        assert gauss.mean == 25
        assert gauss.stdev == 2

    def test_mean_calculation(self) -> None:
        gauss = Gaussian()
        gauss.read_data_file('data/numbers.txt')
        assert gauss.mean == 0
        gauss.calculate_mean()
        assert round(gauss.mean, 2) == 78.09
        assert gauss.mean == sum(gauss.data)/float(len(gauss.data))
        assert gauss.stdev == 1.0   # code smell: you have to drive this from the outside.

    def test_stdev_calculation(self) -> None:
        gauss = Gaussian()
        gauss.read_data_file('data/numbers.txt', True)
        assert round(gauss.calculate_stdev(), 2) == 92.87
        assert gauss.is_sample
        gauss.read_data_file('data/numbers.txt', False)
        assert round(gauss.calculate_stdev(sample = False), 2) == 88.55
        assert not gauss.is_sample
        assert round(gauss.calculate_stdev(sample = True), 2) == 92.87
        assert gauss.is_sample

    def test_pdf(self) -> None:
        gauss = Gaussian(25, 2)
        assert round(gauss.pdf(25), 5) == 0.19947
        gauss.read_data_file('data/numbers.txt')           # is_sample false
        assert round(gauss.calculate_stdev(), 2) == 92.87  # is_sample true
        assert round(gauss.pdf(75), 5) == 0.00429

    def test_add(self) -> None:
        gaussian_one = Gaussian(25, 3)
        gaussian_two = Gaussian(30, 4)
        gaussian_sum = gaussian_one + gaussian_two

        assert gaussian_sum.mean == 55.0
        assert gaussian_sum.stdev == 5.0
