#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on --30/04/2021--

@author: -- Jawad Tanana --

The purpose of this program is to find peaks in the graphs.
"""

def pattern_search_multiple(data_values, pattern_width, threshold):
    sim_list = []
    sliced = []

    # These sets of if statements check the data if they are 
    # sufficient to be analysed or not.
    if threshold > max(data_values):
        return "Not detected"
    if len(data_values) < pattern_width:
        return "Insufficient data"
    
    # This loop starts pattern width from the start of data_values start 
    # position, and ends a pattern width from the last value in data 
    # values
    for num in range(pattern_width, (len(data_values) - pattern_width - 1)):
        # The first if conidition checks if the number is above the threshold
        if data_values[num] > threshold:
            # If the number is above the threshold pattern width infront
            # and behind will be sliced out to be examined.
            sliced = data_values[num - pattern_width:num + pattern_width]
            # The number that the counter is on will be assessed 
            # if it is the max of the slice it will be appeneded, if 
            # it is not the program will proceed to the next value in the
            # list.
            if data_values[num] == max(sliced): 
                sim_list.append(data_values.index(data_values[num]))

    return sim_list

    """ Searches the data_values for all the values that satisfy the criteria
        mentioned below and in the assignment specification document.
        The function returns the indices of these values.

    #Parameters
    ----------
    data_values : [float]
        A list of float values representing similarity measures. You are looking
        for instances of the pattern inside this data_values.

    pattern_width : [float]
        A float value. The length/width of the pattern.

    threshold : [float]
        A float value. Selected similarity measure needs to be greater than or
        equal to the given threshold value.

    Returns
    -------

    One of the three possible outcomes: 
        - "Insufficient data", 
        - "Not detected" or 
        -  a list of non overlapping indices that are greater than or 
           equal to the given threshold value, and that satisfy the following criteria:
               - an index is not selected if the value at the index is less than a value 
                 at one of it's overlapping indices.
               - an index is not selected if it is overlapping with first or last index.
           Overlapping indices: We say two indices are overlapping if the distance 
           between them is less than the width of the pattern.

    """
