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

"""Module for base class of classes representing probability distributions"""

from __future__ import annotations

import math

__all__ = ['Distribution']

class Distribution():
    """Base Class for calculating and visualizing probability distributions."""

    def __init__(self, mean: float, stdev: float):
        self.mean: float = mean      #: mean of the distribution
        self.stdev: float = stdev    #: standard deviation of the distribution``
        self.data: list[float] = []  #: data determining parameters of the distribution
        self.is_sample = False       #: whether data is a sample or the entire population

    def read_data_file(self, file_name: str, sample: bool=True) -> None:
        """Method to read in data from a text file.

        The text file should have

        * one number (float) per line
        * the numbers are stored in the data attribute
        * the mean attribute is then calculated from the data
        * if `sample` true (default), calculate a sample stdev
        * if `sample` false, calculate calculate population stdev
        """
        self.is_sample = sample

        # Read in the data from the file given
        data_list: list[float] = []
        with open(file_name) as file:
            line = file.readline()
            while line:
                data_list.append(float(line))
                line = file.readline()

        self.data = data_list
        # self.calc_data_stats(sample)

    def calc_data_stats(self, sample: bool) -> None:
        """Calculate data statistics (mean/stdev for now)

        Note: Not used for course
        """
        self.is_sample = sample
        self.calculate_stdev(sample)
        # TODO: add other statistics? Maybe median, mode, other moments?

    def calculate_mean(self) -> float:
        """From the data set, calculate & return the mean if it exists."""
        n = len(self.data)
        if n > 0:
            self.mean = sum(self.data)/n
        return self.mean

    def calculate_stdev(self, sample: bool=True) -> float:
        """From the data set, calculate & return the stdev if it exists.

        * If sample is True, calculate a sample standard deviation.
        * If sample is False, calculate a population standard deviation.

        """
        # NOTE: Retaining sample parameter to keep consistent with course's API,
        #       otherwise I don't need it and could do things more cleanly.
        self.is_sample = sample
        mu = self.calculate_mean()
        n = len(self.data)

        if sample:
            # sample standard deviation
            if n > 1:
                self.stdev = math.sqrt(sum(((x - mu)**2 for x in self.data))/(n-1))
        else:
            # population standard deviation
            if n > 0:
                self.stdev = math.sqrt(sum(((x - mu)**2 for x in self.data))/n)

        return self.stdev
