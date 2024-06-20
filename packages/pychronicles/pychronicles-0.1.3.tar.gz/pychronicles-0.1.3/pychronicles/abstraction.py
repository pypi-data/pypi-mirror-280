#!/bin/python3
# -*- coding: utf-8 -*-
"""
The abstraction module offers a class for the generalisation of a collection of sequences as a chronicle.

The problem of generalisation is the construction of a unique chronicle that occurs in every sequences to 
generalize, such that it represents the "common" part of them. 

It is worth noticing that the empty chronicle is a possible solution but is useless. 
To be meaningfull, the algorithm extracts the "largest" chronicle. The notion of "largest" is defined as
the chronicle with the largest multiset and the narrowest temporal constraints. This minimum exists in 
the specific case of finite collection of timed sequences (for more formal details, see "Chronicles: 
Formalization of a Temporal Model", Besnard and Guyet, 2023).


Example
---------

The following example illustrates the generalization of 4 sequences as a chronicle.

.. code-block:: python

    seq = [("a", 1), ("c", 2), ("b", 3), ("a", 8), ("a", 10), ("b", 12)]

    dates = np.array([e[1] for e in seq], dtype="float")
    data = np.array([e[0] for e in seq])

    ts1 = TimedSequence(dates, data)

    seq = [("a", 1), ("b", 12), ("c", 23), ("b", 30)]

    dates = np.array([e[1] for e in seq], dtype="float")
    data = np.array([e[0] for e in seq])

    ts2 = TimedSequence(dates, data)

    seq = [("a", 25), ("b", 26), ("c", 28), ("b", 30)]

    dates = np.array([e[1] for e in seq], dtype="float")
    data = np.array([e[0] for e in seq])

    ts3 = TimedSequence(dates, data)

    seq = [("b", 20), ("c", 23), ("a", 25), ("b", 30)]

    dates = np.array([e[1] for e in seq], dtype="float")
    data = np.array([e[0] for e in seq])

    ts4 = TimedSequence(dates, data)

    #########################
    abs = Abstracter()
    c = abs.abstract([ts1, ts2, ts3, ts4])

    print(c)

:Authors:
    Thomas Guyet, Inria
:Date:
    08/2023
"""

from pychronicles import Chronicle
from pychronicles import TimedSequence

from multiset import FrozenMultiset, Multiset
from numpy import argsort
from typing import Sequence, Union


class Abstracter:
    def __init__(self):
        pass

    def abstract(self, sequences: Sequence[TimedSequence]) -> Chronicle:
        """
        Parameters
        -----------
        sequences: [TimedSequence]
            List of timed sequences to generalize as a chronicle

        Returns
        ---------
        Chronicle
            The largest chronicle that occurs in all the timed sequences.
        """
        # compute the largest multiset of events that occurs in all sequences
        ms = None
        for seq in sequences:
            lms = Multiset(seq._data.tolist())
            if ms is None:
                ms = lms
            else:
                ms = ms.intersection(lms)

        if len(ms) == 0:
            # return empty chronicle
            return Chronicle()

        # init the temporal constraints
        tconst = {}
        for i in range(len(ms)):
            for j in range(i + 1, len(ms)):
                tconst[(i, j)] = [float("inf"), -float("inf")]

        # define the convexhull of the interval between each pairs of events
        for seq in sequences:
            ret = seq[
                Abstracter.first_occurrence(seq, ms)
            ]  # get the sequence with only the shared events (first occurrences)
            dates = ret._dates[
                argsort(ret._data)
            ]  # get the dates of the shared events in the lexical order of events
            # update the temporal constraints
            for i in range(len(ms)):
                for j in range(i + 1, len(ms)):
                    d = dates[j] - dates[i]
                    tconst[(i, j)][0] = min(tconst[(i, j)][0], d)
                    tconst[(i, j)][1] = max(tconst[(i, j)][1], d)

        c = Chronicle()
        ms = list(ms)
        ms.sort()
        i = 0
        for e in ms:
            c.add_event(i, e)
            i += 1
        for k, v in tconst.items():
            c.add_constraint(k[0], k[1], (v[0], v[1]))
        return c

    @staticmethod
    def first_occurrence(
        sequence: TimedSequence, ms: Multiset
    ) -> Union[Sequence[int], None]:
        output = []
        ms = ms.copy()
        for i in range(len(sequence._data)):
            e = sequence._data[i]
            if e in ms:
                output.append(i)
                ms -= Multiset({e: 1})
                if len(ms) == 0:
                    return output

        return None


if __name__ == "__main__":
    import numpy as np

    seq = [("a", 1), ("c", 2), ("b", 3), ("a", 8), ("a", 10), ("b", 12)]

    dates = np.array([e[1] for e in seq], dtype="float")
    data = np.array([e[0] for e in seq])

    ts1 = TimedSequence(dates, data)

    seq = [("a", 1), ("b", 12), ("c", 23), ("b", 30)]

    dates = np.array([e[1] for e in seq], dtype="float")
    data = np.array([e[0] for e in seq])

    ts2 = TimedSequence(dates, data)

    seq = [("a", 25), ("b", 26), ("c", 28), ("b", 30)]

    dates = np.array([e[1] for e in seq], dtype="float")
    data = np.array([e[0] for e in seq])

    ts3 = TimedSequence(dates, data)

    seq = [("b", 20), ("c", 23), ("a", 25), ("b", 30)]

    dates = np.array([e[1] for e in seq], dtype="float")
    data = np.array([e[0] for e in seq])

    ts4 = TimedSequence(dates, data)

    #########################
    abs = Abstracter()
    c = abs.abstract([ts1, ts2, ts3, ts4])

    print(c)
