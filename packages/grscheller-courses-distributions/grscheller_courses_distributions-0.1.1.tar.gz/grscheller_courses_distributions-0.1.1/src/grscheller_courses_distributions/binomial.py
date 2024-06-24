# Copyright 2024 Geoffrey R. Scheller
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# This module contains software derived from Udacity® exercises.
# Udacity® (https://www.udacity.com/)
#

"""Module for the Binomial class - derived from Udacity exercise template."""

from __future__ import annotations

from typing import Callable, List, Tuple
from math import ceil, comb, floor, pow, sqrt
import matplotlib.pyplot as plt
from .distribution import Distribution

__all__ = ['Binomial']

class Binomial(Distribution):
    """ Class for visualizing data as binomial distributions.

    The binomial distribution represents the number of events with probability
    p happening in n numbers of trials.

    Attributes (some inherited):

    * mean (float) representing the mean value of the distribution
    * stdev (float) representing the standard deviation of the distribution
    * data  extracted from a data file (taken to be a population)
    * p (float) representing the probability of an event occurring
    * n (int) the total number of trials
    """
    def __init__(self, p: float=0.5, n: int=20):
        if not (0.0 <= p <= 1.0) or n < 1:
            msg1 = 'For a binomial distribution, '
            msg2 = msg3 = ''
            if not (0.0 <= p <= 1.0):
                msg2 = '0 <= p <= 1'
            if n < 0:
                msg3 = 'the number of trials n must be non-negative'
            if msg2 and msg3:
                msg = msg1 + msg2 + ' and ' + msg3 + '.'
            else:
                msg = msg1 + msg2 + msg3 + '.'
            raise ValueError(msg)

        self.p: float = p  #: probability of a success
        self.n: int = n    #: number of events
        super().__init__(self.calculate_mean(), self.calculate_stdev())

    def calculate_mean(self) -> float:
        """Calculate the mean from p and n"""
        n = self.n
        p = self.p
        self.mean = mean = n*p
        return mean

    def calculate_stdev(self) -> float:
        """Calculate the standard deviation using p and n"""
        n = self.n
        p = self.p
        self.stdev = stdev = sqrt(n*p*(1-p))
        return stdev

    def read_data_file(self, file_name: str, sample: bool=False) -> None:
        """Read data from a file, DOES NOT UPDATE either `p` or `n`.

        * the data is always treated as the population randomly selected with replacement
        * the sample parameter is ignored (it is there for LSP)
        * the data is assumed to be one float per line
        * each value either 0.0 or 1.0 (0 or 1 interpreted as floats)
        """
        super().read_data_file(file_name, False)

    def replace_stats_with_data(self) -> tuple[float, int]:
        """Function to calculate p and n from the read in data set.

        Where the read in data set is taken as the population.
        """
        if self.data:
            self.n = n = len(self.data)
            self.p = p = sum(self.data)/n
            self.mean = n*p
            self.stdev = sqrt(n*p*(1-p))
        return self.p, self.n

    def plot_bar_data(self) -> None:
        """Produce a bar-graph of the data using the matplotlib pyplot library."""
        n = self.n
        p = self.p

        fig, axis = plt.subplots()
        axis.bar(('0', '1'), (n*(1-p), n*p), color ='maroon', width = 0.6)
        axis.set_title('Failures and Successes for a sample of {}'.format(n))
        axis.set_xlabel('prob = {}, n = {}'.format(p, n))
        axis.set_ylabel('Sample Count')
        plt.show()

    def pdf(self, kf: float) -> float:
        """Binomial prob density function for this Binomial object."""
        k = int(kf)
        n = self.n
        p = self.p
        return comb(n, k)*(p**k)*(1 - p)**(n-k)

    def plot_bar_pdf(self) -> Tuple[List[int], List[float]]:
        """Function to plot the pdf of the binomial distribution.

        Returns:
            list: x values used for the pdf plot
            list: y values used for the pdf plot
        """
        pdf: Callable[[int], float] = lambda ii: self.pdf(float(ii))

        xs: List[int] = list(range(self.n + 1))
        ys: List[float] = list(map(pdf, range(self.n + 1)))

        plt.bar(list(str(x) for x in xs), ys, color ='maroon', width = 0.4)
        plt.title('Probability Density of Success')
        plt.xlabel('Successes for {} trials'.format(self.n))
        plt.ylabel('Probability')
        plt.show()

        return xs, ys

    def __add__(self, other: Binomial) -> Binomial:
        """Add together two Binomial distributions with equal p."""
        if type(other) is not Binomial:
            msg = 'A binomial distribution cannot be added to a {}'
            msg = msg.format(type(other))
            raise TypeError(msg)
        if self.p != other.p:
            msg = 'p values are not equal'
            raise ValueError(msg)

        return Binomial(self.p, self.n + other.n)

    def __repr__(self) -> str:
        """Output the characteristics of the Binomial instance.

        Returns a string showing:

        * mean
        * standard deviation
        * p
        * n
        """
        repr_str = 'mean {}, standard deviation {}, p {}, n {}'
        return repr_str.format(self.mean, self.stdev, self.p, self.n)
