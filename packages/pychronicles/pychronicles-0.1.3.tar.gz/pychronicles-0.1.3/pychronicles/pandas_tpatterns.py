"""
This module is dedicated to pandas accessors. Thanks to this accessors, you can use 
chronicle recognition and abstraction from dataset represented in pandas dataframes.

The principle of the dataframe is to represent a timed sequence. Each row of the dataframe 
represents an event, and the columns are the feature representing the nature of an event. 
Contrary to internal representation of timed sequence, the events can be described with 
diverse and multiple features (int, str, float, ...)

Then, there are some (natural) requirements on the dataframe: first, the dataframe must 
at least be indexed by dates (dates of floats) and have a column to describe the 
even' feature. In addition, if your dataset is made of several sequences, you may have 
a column to identify the individuals. This column can either be a classical column or a 
second index. 

Once your dataset is represented with such a dataframe, all the functionalities of chronicles 
can be directly used with the dataframe (and using the `tpattern` accessor).

Note
-----

When using chronicle with dataframe, the event of chronicles are defined through the value of the 
features in the dataframe. The typical specification of an event is a column/value pair, for 
instance  `label=="a"` meaning that the label must be "a" in this case.
It is possible to express much complex situation that is used to evaluate a row of the dataframe (with combinaison 
with `and`/`or` operator for instance).

For more details about the acceptable syntax for the chronicle event, we recommend the user to read the 
pandas documentation: [https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html]


Example
--------

The following example illustrates the use of chronicle with pandas dataframes.

.. code-block:: python

    from pychronicle import Chronicle, TPatternAccessor

    df = pd.DataFrame(
        {
            "label": [e[0] for e in seq],
            "str_val": [
                e[0] * 2 for e in seq
            ],  # illustration of another columns than "label"
            "num_val": np.random.randint(
                10, size=len(seq)
            ),  # illustration of another columns than "label"
        },
        index=[np.datetime64("1970-01-01") + np.timedelta64(e[1], "D") for e in seq],
    )
    print("----------------")

    c = Chronicle()
    c.add_event(0, 'label=="a"')
    c.add_event(1, 'label=="b" & num_val>5')
    c.add_event(2, 'label=="c"')
    c.add_constraint(0, 1, (np.timedelta64(4, "D"), np.timedelta64(10, "D")))
    c.add_constraint(0, 2, (np.timedelta64(2, "D"), np.timedelta64(8, "D")))
    c.add_constraint(1, 2, (np.timedelta64(3, "D"), np.timedelta64(13, "D")))

    reco = df.tpattern.match(c)
    print(f"Reconnaissance numpy de la chronique: [{reco}]!")

    reco = df.tpattern.recognize(c)
    print(f"Reconnaissance numpy de la chronique: [{reco}]!")

    ##########################################################################
    # Use with a dataframe representing a collection of sequences

    # Create a dataframe representing several sequences with complex events, each sequence having its own id
    grpdf = pd.DataFrame(
        {
            "label": [e[0] for e in seq] * 3,
            "str_val": [e[0] * 2 for e in seq]
            * 3,  # illustration of another columns than "label"
            "num_val": np.random.randint(
                10, size=3 * len(seq)
            ),  # illustration of another columns than "label"
            "id": [1] * len(seq) + [2] * len(seq) + [3] * len(seq),
        },
        index=[np.datetime64("1970-01-01") + np.timedelta64(e[1], "D") for e in seq]
        * 3,
    )

    # the match function checks chronicle matches on all the sequences at the same time and
    # returns its answer for each chronicle
    print(f"Does the chronicle in a dataset of sequences?")
    reco = grpdf.groupby("id").apply(lambda d: d.tpattern.match(c))
    print(reco)

    print(f"What are the occurrences of a sequence in a dataset?")
    reco = grpdf.groupby("id").apply(lambda d: d.tpattern.recognize(c))
    print(reco)

    ##########################################
    # Abstraction example

    grpdf = pd.DataFrame(
        {
            "label": [np.random.choice(["a", "b", "c"]) for _ in range(20)],
            "id": [int(np.floor(i / 4)) for i in range(20)],
        }
    )

    chro = grpdf.tpattern.abstract("label", "id")
    print(chro)

:Authors:
    Thomas Guyet, Inria
:Date:
    08/2023
"""
import pandas as pd
from pandas.api.extensions import register_dataframe_accessor
import numpy as np
from pychronicles import Chronicle
from pychronicles import TimedSequence
from pychronicles.mtlformula import ExtractMTL
from pychronicles import Abstracter

## typing features
from typing import TypeVar, Union, Dict, Mapping, Tuple, Sequence, Any


@register_dataframe_accessor("tpattern")
class TPatternAccessor:
    def __init__(self, df: pd.DataFrame):
        self._validate(df)
        self._df = df
        self.simplifer = ExtractMTL()

    @staticmethod
    def _validate(df):
        """:meta private:"""
        # verify there is a no MultiIndex, and that the Index is made of Integers or Timestamps
        if isinstance(df.index, pd.MultiIndex):
            raise AttributeError("Can not handle multi-indexed dataframes.")
        if (
            df.index.dtype != float
            and df.index.dtype != int
            and df.index.dtype != np.dtype("datetime64[ns]")
        ):
            raise AttributeError("Dataframe index has to be convertible in float.")

    @staticmethod
    def __lemmatize_query(q):
        """:meta private:"""
        return q.replace(" ", "").replace("'", '"')

    def __transform(self, c: Chronicle):
        """:meta private:"""

        # each event string is associated to a unique integer label
        queries = {}
        i = 0
        for _, q in c.sequence.items():
            if not isinstance(q, str):
                raise ValueError("Chronicle events must be strings")
            queries[TPatternAccessor.__lemmatize_query(q)] = i
            i += 1

        # create a copy of the chronicle and replace event strings by their label
        Craw = c.copy()
        newevents = {
            id: queries[TPatternAccessor.__lemmatize_query(q)]
            for id, q in c.sequence.items()
        }
        Craw.sequence = newevents

        # create a time series from the queries applied on the dataset
        dates = None
        data = []
        for q, label in queries.items():
            # q is a query string
            qdates = self._df.query(q).index
            if dates is None:
                dates = qdates.to_numpy()
            else:
                dates = np.concatenate([dates, qdates.to_numpy()])
            data += [label] * len(qdates)

        if dates.dtype == "int":
            dates = dates.astype("float")

        ts = TimedSequence(dates, np.array(data))
        return Craw, ts

    def match(self, c: Chronicle):
        """
        Parameters
        -----------
        c: Chronicle
            Chronicle to recognize

        
        Returns
        --------
        bool
            True is the MTL is recognize in the sequence
        """
        Craw, ts = self.__transform(c)
        return Craw.match(ts)

    def recognize(self, c: Chronicle):
        """

        Parameters
        -----------
        c: Chronicle
            Chronicle to recognize

        Returns
        --------
        [[int]]
            Occurrences of the chronicle in the sequence
        """
        Craw, ts = self.__transform(c)
        if len(ts)==0:
            return []
        return Craw.recognize(ts)

    def __transform_mtl(self, atoms, dt=1):
        """:meta private:"""
        data = {}
        for k, v in atoms.items():
            data[v] = [(e, True) for e in self._df.query(k).index.to_list()]
            data[v] += [(e + dt, False) for e in self._df.query(k).index.to_list()]
            data[v].sort(key=lambda x: x[0])
        return data

    def match_mtl(self, formula: str, dt: float = 1):
        """Formula is a MTL formula

        Only for dataframe with index with floats or integers (not dates)

        Parameters
        -----------
        formula: str
            MTL formula to recognize
        dt: int, default 1
            Time delta used in the MTL recognition

        Returns
        --------
        bool
            True is the MTL is recognize in the sequence
        """
        if self._df.index.dtype == np.dtype("datetime64[ns]"):
            raise AttributeError("match_mtl works only with float or integer indexes.")
        mtl_formula = self.simplifer.parse(formula)
        data = self.__transform_mtl(self.simplifer.atoms, dt)
        return mtl_formula(data, dt=dt, quantitative=False)

    @staticmethod
    def __TSExtractor__(df, event):
        """
        Parameters
        -----------
        df: pandas.Dataframe
            dataframe indexed with time

        event: str
            name of the column
        """
        dates = df.index.to_numpy()
        if dates.dtype == "int":
            dates = dates.astype("float")
        data = df[event].tolist()

        return TimedSequence(dates, data)

    def abstract(self, event: str, groupby: str = None):
        """Abstract a dataframes into a chronicle
        
        Parameters
        ------------
        event: str
            name of the dataframe column to use as event (must contains integers or str)
        groupby: str, optional
            name of the column to identify groups of events. In this case the abstraction method
            outputs one chronicle that appear in each sequence identified by the `groupby` column.

        Returns
        ----------
        Chronicle
            a chronicle that abstract the collection of sequences represented in the dataset
        """
        abs = Abstracter()
        if groupby is None:
            ts = TPatternAccessor.__TSExtractor__(self._df, event)
            C = abs.abstract([ts])
        else:
            tss = (
                self._df.groupby(groupby)
                .apply(lambda d: TPatternAccessor.__TSExtractor__(d, event))
                .tolist()
            )
            C = abs.abstract(tss)
        if pd.api.types.is_string_dtype(self._df[event]):
            C.sequence = {k: event + "=='" + v + "'" for k, v in C.sequence.items()}
        else:  # events are integers
            C.sequence = {k: event + "==" + str(v) for k, v in C.sequence.items()}
        return C


if __name__ == "__main__":
    #################################
    # Example of sequence
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

    df = pd.DataFrame(
        {
            "label": [e[0] for e in seq],
            "str_val": [
                e[0] * 2 for e in seq
            ],  # illustration of another columns than "label"
            "num_val": np.random.randint(
                10, size=len(seq)
            ),  # illustration of another columns than "label"
        },
        index=[np.datetime64("1970-01-01") + np.timedelta64(e[1], "D") for e in seq],
    )
    print("----------------")

    c = Chronicle()
    c.add_event(0, 'label=="a"')
    c.add_event(1, 'label=="b" & num_val>5')
    c.add_event(2, 'label=="c"')
    c.add_constraint(0, 1, (np.timedelta64(4, "D"), np.timedelta64(10, "D")))
    c.add_constraint(0, 2, (np.timedelta64(2, "D"), np.timedelta64(8, "D")))
    c.add_constraint(1, 2, (np.timedelta64(3, "D"), np.timedelta64(13, "D")))

    reco = df.tpattern.match(c)
    print(f"Reconnaissance numpy de la chronique: [{reco}]!")

    reco = df.tpattern.recognize(c)
    print(f"Reconnaissance numpy de la chronique: [{reco}]!")

    ##########################################################################
    # Use with a dataframe representing a collection of sequences

    # Create a dataframe representing several sequences with complex events, each sequence having its own id
    grpdf = pd.DataFrame(
        {
            "label": [e[0] for e in seq] * 3,
            "str_val": [e[0] * 2 for e in seq]
            * 3,  # illustration of another columns than "label"
            "num_val": np.random.randint(
                10, size=3 * len(seq)
            ),  # illustration of another columns than "label"
            "id": [1] * len(seq) + [2] * len(seq) + [3] * len(seq),
        },
        index=[np.datetime64("1970-01-01") + np.timedelta64(e[1], "D") for e in seq]
        * 3,
    )

    # the match function checks chronicle matches on all the sequences at the same time and
    # returns its answer for each chronicle
    print(f"Does the chronicle in a dataset of sequences?")
    reco = grpdf.groupby("id").apply(lambda d: d.tpattern.match(c))
    print(reco)

    print(f"What are the occurrences of a sequence in a dataset?")
    reco = grpdf.groupby("id").apply(lambda d: d.tpattern.recognize(c))
    print(reco)
    ##########################################################################
    # Same dataframe indexed with float/int

    grpdf = pd.DataFrame(
        {
            "label": [e[0] for e in seq] * 3,
            "str_val": [e[0] * 2 for e in seq] * 3,
            "num_val": np.random.randint(10, size=3 * len(seq)),
            "id": [1] * len(seq) + [2] * len(seq) + [3] * len(seq),
        },
        index=[e[1] for e in seq] * 3,
    )

    query = ' F(label=="a" & F[2.9,5]( label=="b" & num_val>5 ))'
    print(f"Does the MTL formula '{query}' matches the sequences?")
    reco = grpdf.groupby("id").apply(lambda d: d.tpattern.match_mtl(query))
    print(reco)

    ##########################################################################
    # Abstraction example

    grpdf = pd.DataFrame(
        {
            "label": [np.random.choice(["a", "b", "c"]) for _ in range(20)],
            "id": [int(np.floor(i / 4)) for i in range(20)],
        }
    )

    chro = grpdf.tpattern.abstract("label", "id")
    print(chro)

    grpdf = pd.DataFrame(
        {
            "label": [int(np.random.choice([13, 6])) for _ in range(28)],
            "id": [int(np.floor(i / 7)) for i in range(28)],
        }
    )

    chro = grpdf.tpattern.abstract("label", "id")
    print(chro)
    # print(grpdf)
    reco = grpdf.groupby("id").apply(lambda d: d.tpattern.match(chro))
    print(reco)
