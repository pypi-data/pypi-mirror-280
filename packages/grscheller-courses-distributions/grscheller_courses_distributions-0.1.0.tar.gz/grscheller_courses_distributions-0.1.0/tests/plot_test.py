# Using pytest for testing
#
# WARNING: Plotting tests depend on user input!!!
#          This is considered bad practice except for
#          single user/maintainer projects.
# 
#          - pytest must be run with the -s option
#          - test data hard coded, run tests from project root
#
# Example: $ pytest -s tests/plot_test.py
#

from grscheller_courses_distributions.gaussian import Gaussian
from grscheller_courses_distributions.binomial import Binomial

class Test_Gaussian:

    def test_plot_data_pdf(self) -> None:
        gauss = Gaussian()
        gauss.read_data_file('data/numbers.txt')
        gauss.calculate_stdev(True)
        gauss.plot_histogram_data()
        x_pdf, y_pdf = gauss.plot_histogram_pdf()

class Test_Binomial:

    def test_plot_data_pdf(self) -> None:
        bernoulli = Binomial()
        bernoulli.read_data_file('data/numbers_binomial.txt')
        bernoulli.replace_stats_with_data()
        bernoulli.plot_bar_data()
        x_pdf, y_pdf = bernoulli.plot_bar_pdf()
