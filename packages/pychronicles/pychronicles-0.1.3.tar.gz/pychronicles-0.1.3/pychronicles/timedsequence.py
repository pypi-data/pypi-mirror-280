#!/bin/python3
# -*- coding: utf-8 -*-
"""
This module implements the class to model time sequences. A timed sequence is a sequence of 
events, represented by a label belonging to a vocabulary, that have a timestamp. 

For compatibility with chronicle recognition, we recommand to represent labels by strings 
(it should work with any object equipped with __eq__ operator, but at the time, it is 
not a safe usage).

The timestamp of an event in a time instant (not an interval). This time instant can 
be modeled in two different manners:

* float: basic representantion of a metric quantity, but that is definitivelly meaningless,
* numpy.datetime64: standard representation of date in Numpy. This allows to describe events 
    in real datasets is a natural way (without having to convert them as float).


The class is equipped with functions to ease their intuitive usage. For instance: select 
subsequences by date, event type, etc. This functionnalities are illustrated in the example below.

Warning
--------
Be careful to use numpy.datetime64 dates but not datetime (from the datetime package) that do 
not provide the same interface and that is not compatible with TimedSequences.

Example
--------

The following example illustrates the main functionalities of the `TimeSequence` class.

.. code-block:: python

    # Example of sequence
    seq = [ ("a", 1), ("c", 2), ("b", 3), ("a", 8), ("a", 10), ("b", 12), ("a", 15), ("c", 17), ("b", 20), ("c", 23), ("c", 25), ("b", 26), ("c", 28), ("b", 30) ]

    dates = np.array(
        [np.datetime64("1970-01-01") + np.timedelta64(e[1], "D") for e in seq],
        dtype="datetime64",
    )
    data = np.array([e[0] for e in seq])

    ts = TimedSequence(dates, data)
    print(ts)
    print("---- time based selection ------")
    tssel = ts[ts < np.datetime64("1970-01-07")]
    print(tssel)

    print("----- item based selection ------")
    tssel = ts[ts == "a"]
    print(tssel)

    print("----- start -----")
    print(tssel.start())

    print("----- at ------")
    print(ts.at(np.datetime64("1970-01-02")))
    print(ts.at(np.datetime64("1970-01-08")))

    ######################

    dates = np.array([float(e[1]) for e in seq], dtype="float")
    data = np.array([e[0] for e in seq])

    ts = TimedSequence(dates, data)
    print(ts)
    print("---- time based selection ------")
    tssel = ts[ts < 6.0]
    print(tssel)

    try:
        tssel = ts[ts < 6]
    except ValueError:
        print("Floats are mandatory")

    print("----- item based selection ------")
    tssel = ts[ts == "a"]
    print(tssel)

    print("----- start -----")
    print(tssel.start())

    print("----- at ------")
    print(ts.at(2))
    print(ts.at(7.0))


:Authors:
    Thomas Guyet, Inria
:Date:
    08/2023
"""

import warnings
import numpy as np
import scipy.sparse.csgraph
from datetime import datetime as dt

## typing features
from typing import TypeVar, Union, Dict, Mapping, Tuple, Sequence, Any

TimedSequence = TypeVar("pychronicles.timedsequence.TimedSequence")

TYPE_DELTATIME = 1
TYPE_FLOAT = 2


class TimedSequence:
    def __init__(
        self,
        dates: Union[Sequence[np.datetime64], Sequence[float]],
        data: Union[Sequence[str], Sequence[int]],
    ):
        """ """
        if len(dates) != len(data):
            raise ValueError("dates and data must have the same length")
        if not isinstance(dates, np.ndarray):
            raise ValueError("Dates must be a numpy.ndarray")

        if not np.issubdtype(dates.dtype, np.datetime64) and not dates.dtype == float:
            raise ValueError("Dates elements must be of kind datetime64 or float")
        if np.issubdtype(dates.dtype, np.datetime64):
            self.dtype = TYPE_DELTATIME
        else:
            self.dtype = TYPE_FLOAT

        self._dates = dates
        self._data = np.array(data)
        # ensure that it is ordered by dates
        reorder = np.argsort(self._dates)
        self._dates = self._dates[reorder]
        self._data = self._data[reorder]

    def __lt__(self, dt: Union[np.datetime64, float]) -> Sequence[bool]:
        if not isinstance(dt, np.datetime64) and not isinstance(dt, float):
            raise ValueError("Datetime/float expected")
        return self._dates.__lt__(dt)

    def __le__(self, dt: Union[np.datetime64, float]) -> Sequence[bool]:
        if not isinstance(dt, np.datetime64) and not isinstance(dt, float):
            raise ValueError("Datetime/float expected")
        return self._dates.__le__(dt)

    def __gt__(self, dt: Union[np.datetime64, float]) -> Sequence[bool]:
        if not isinstance(dt, np.datetime64) and not isinstance(dt, float):
            raise ValueError("Datetime/float expected")
        return self._dates.__gt__(dt)

    def __ge__(self, dt: Union[np.datetime64, float]) -> Sequence[bool]:
        if not isinstance(dt, np.datetime64) and not isinstance(dt, float):
            raise ValueError("Datetime/float expected")
        return self._dates.__ge__(dt)

    def __eq__(self, dt: Union[int, str, np.datetime64, float]) -> Sequence[bool]:
        if isinstance(dt, np.datetime64):
            return self._dates.__eq__(dt)
        elif isinstance(dt, str):
            return self._data.__eq__(dt)
        elif isinstance(dt, int):
            return self._data.__eq__(dt)
        elif isinstance(dt, float):
            return self._dates.__eq__(dt)
        raise ValueError("Datetime, str or int expected")

    def start(self) -> Union[np.datetime64, float]:
        return self._dates[0]

    def end(self) -> Union[np.datetime64, float]:
        return self._dates[-1]

    def len(self) -> int:
        return len(self._dates)

    def at(self, dt: Union[np.datetime64, float]) -> Union[int, str]:
        return self._data[self._dates.__eq__(dt)]

    def __str__(self, sep: str = "\n") -> str:
        elems = []
        for k, v in zip(self._dates, self._data):
            elems.append(str(k) + ":" + str(v))
        return sep.join(elems)

    def __getitem__(self, selection) -> TimedSequence:
        return TimedSequence(self._dates[selection], self._data[selection])
    
    def __len__(self) -> int :
        return self.len()


if __name__ == "__main__":
    seq = [
        ("a", 1),
        ("c", 2),
        ("b", 3),
        ("a", 8),
        ("a", 10),
        ("b", 12),
        ("a", 15),
        ("c", 17),
        ("b", 20),
        ("c", 23),
        ("c", 25),
        ("b", 26),
        ("c", 28),
        ("b", 30),
    ]

    dates = np.array(
        [np.datetime64("1970-01-01") + np.timedelta64(e[1], "D") for e in seq],
        dtype="datetime64",
    )
    data = np.array([e[0] for e in seq])

    ts = TimedSequence(dates, data)
    print(ts)
    print("---- time based selection ------")
    tssel = ts[ts < np.datetime64("1970-01-07")]
    print(tssel)

    print("----- item based selection ------")
    tssel = ts[ts == "a"]
    print(tssel)

    print("----- start -----")
    print(tssel.start())

    print("----- at ------")
    print(ts.at(np.datetime64("1970-01-02")))
    print(ts.at(np.datetime64("1970-01-08")))

    #############################""

    dates = np.array([float(e[1]) for e in seq], dtype="float")
    data = np.array([e[0] for e in seq])

    ts = TimedSequence(dates, data)
    print(ts)
    print("---- time based selection ------")
    tssel = ts[ts < 6.0]
    print(tssel)

    try:
        tssel = ts[ts < 6]
    except ValueError:
        print("Floats are mandatory")

    print("----- item based selection ------")
    tssel = ts[ts == "a"]
    print(tssel)

    print("----- start -----")
    print(tssel.start())

    print("----- at ------")
    print(ts.at(2))
    print(ts.at(7.0))
