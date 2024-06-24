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

"""Module for the Gaussian class - derived from Udacity exercise template."""

from __future__ import annotations

from math import exp, pi, sqrt
import matplotlib.pyplot as plt
from .distribution import Distribution

__all__ = ['Gaussian']

class Gaussian(Distribution):
    """ Class for visualizing data as Gaussian distributions.

    The Gaussian, also called Normal, distribution is a continuous probability
    distribution with probability density function
    ```
       f(x) = (1/√(2πσ²))exp(-(x-μ)²/2σ²)
    ```
    where

    * μ = mu = mean value of the distribution
    * σ = sigma = standard deviation of the distribution

    """
    def __init__(self, mu: float=0.0, sigma: float=1.0):
        if sigma <= 0:
            msg = 'For a Gaussian distribution, sigma must be greater than 0'
            raise ValueError(msg)
        # self.mu = mu       # Not using these, but conceptually
        # self.sigma = sigma # similar to p and n for Binomial class.
        super().__init__(mu, sigma)

    def plot_histogram_data(self) -> None:
        """Produce a histogram of the data using the matplotlib pyplot library."""
        fig, axis = plt.subplots()
        axis.hist(self.data)
        axis.set_title('Histogram of Data')
        axis.set_xlabel('Data')
        axis.set_ylabel('Count')
        plt.show()

    def pdf(self, x: float) -> float:
        """Gaussian prob density function for this Gaussian object."""
        c = 1.0/sqrt(2*pi)
        mu = self.mean
        sigma = self.stdev
        return (c/sigma)*exp(-0.5*((x - mu)/sigma)**2)

    def plot_histogram_pdf(self, n_spaces: int = 100) -> tuple[list[float], list[float]]:
        """Method to plot the normalized histogram of the data and a plot of the
        probability density function along the same range

        Args:
            n_spaces (int): number of data points to plot

        Returns:
            list: x values used for the pdf plot
            list: y values used for the pdf plot
        """
        data = self.data
        pdf = self.pdf

        if len(data) == 0:
            return [], []

        min_x, max_x = min(data), max(data)
        if min_x == max_x:
            min_x, max_x = min_x - 0.5, max_x + 0.5
        interval = (max_x - min_x)/n_spaces

        x: list[float] = list((min_x + interval*n for n in range(n_spaces + 1)))
        y: list[float] = list((pdf(x) for x in x))

        # make the plots
        fig, axes = plt.subplots(2,sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for the\n Sample Mean and Sample Standard Deviation')
        axes[1].set_xlabel('sample mean = {}, sample stdev = {}'.format(self.mean, self.stdev))
        axes[1].set_ylabel('Density')
        plt.show()

        return x, y

    def __add__(self, other: Gaussian) -> Gaussian:
        """Add together two Gaussian distributions."""
        if type(other) is not Gaussian:
            msg = 'A gaussian distribution cannot be added to a {}'
            msg = msg.format(type(other))
            raise TypeError(msg)
        return Gaussian(self.mean + other.mean, sqrt(self.stdev**2 + other.stdev**2))

    def __repr__(self) -> str:
        repr_str = "mean {}, standard deviation {}"
        return repr_str.format(self.mean, self.stdev)
