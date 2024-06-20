---
title: README
author: Thomas Guyet
---

[![PyPI version](https://badge.fury.io/py/pychronicles.svg)](https://badge.fury.io/py/pychronicles)
[![Downloads](https://static.pepy.tech/badge/pychronicles)](https://pepy.tech/project/pychronicles)
[![GitHub license](https://img.shields.io/static/v1?label=Licence&message=LGPL-3&color=green)](https://www.gnu.org/licenses/lgpl-3.0.txt)


# PyChronicles package

A chronicle is a specification of the complex temporal behaviors as a graph of temporal constraints. More specifically, a chronicle is a multiset of events and a set of temporal constraints specifying that occurrences of pairs of events must occurs within a given temporal interval.
It can be used to recognize complex behaviors in sequence the temporal events.
PyChronicle is now compatible with Pandas and makes chronicle features [available on dataframes](#dataframe-accessor) representing timed sequences.

This library proposes a Python class to define a timed sequence, a chronicle, to read/save them in a standard CRS format. The main useful functionnality for chronicle is their efficient matching in a timed sequence, or pandas dataframes (including an accessor).
The Abstracter class enables to create a chronicle from a collection of sequences.

For more details about the usage of this package, have a look at the [documentation](https://tguyet.gitlabpages.inria.fr/pychronicles/). And for more (formal) information about the temporal model of chronicle, see our [book](https://link.springer.com/book/10.1007/978-3-031-33693-5) and :
~~~bibtex
@book{chroniclesbook,
  title = {Chronicles: Formalization of a Temporal Model},
  author = {Besnard, Philippe and Guyet, Thomas},
  publisher={Springer Nature},
  pages = {121},
  year = {2023}
}
~~~

## Package installation

The [PyChronicles package](https://pypi.org/project/hydronaut) is available in [Python Package Index](https://pypi.org/) and can be installed using any standard Python package manager.
~~~sh
pip install pychronicles
~~~

It can also be installed from source. For example, to install it with pip, either locally or in a virtual environment, run the following commands:

~~~sh
git clone --recursive https://gitlab.inria.fr/tguyet/pychronicles
cd pychronicles
pip install -r requirements.txt
pip install --upgrade .
~~~

You can also use pip to install the repo from sources. For instance, run the following commands: 
~~~sh
git clone --recursive https://gitlab.inria.fr/tguyet/pychronicles
cd pychronicles
pip install .
~~~

In case you want to visualize chronicles, you will need to install manually the `networkx` and `matplotlib`. By default, they are not installed and the plotting functions is disabled.
~~~sh
pip install networkx matplotlib
~~~

## Basic Usage Example

```python
import pychonicles

# create a timed sequence
seq = [('a',1),('c',2),('b',3),('a',8)]
ts = TimedSequence(np.array([e[2] for e in seq], dtype='float'), [e[0] for e in seq])

#create a chronicle
c=Chronicle()
c.add_event(0,'a')
c.add_event(1,'b')
c.add_constraint(0,1, (0.4,2.3))

reco=c.match(ts)
print(f"Does the chronicle matches the sequence? [{reco}]")

reco=c.recognize(ts)
print(f"What are the occurrences of the chronicle in the sequence? [{reco}]")
```


## Efficient chronicle recognition

The chronicle recognition package is a pure python package implemented using numpy features. To make it more efficient, it is possible to compile a cythonized version.

### Timed Sequences

A timed sequence is be created from different manners:
* a pair of lists containing the events and the dates.
* a simple list of items (`str`, `int` or `None`) with implicit timestamps : `['a', 'b', ..., None, 'c', None, 'd']`. In this case, `None` means that there is no event at the corresponding time instant.
* a list of explicitly timestamped items (`str` or `int`) : `[ (1,'a'), (23,'b'), (30,'c'), (45, 'd')]`

The dates can be represented with dates (only with `np.datetime64` type) or floats. In case the dates are coded as `int`, they will be converted in `float`.

The type of events must be `str` or `int`.

_Usage Example_:
```python
>>> seq = [('a',1),('c',2),('b',3),('a',8),('a',10),('b',12),('a',15),('c',17), ('b',20),('c',23),('c',25),('b',26),('c',28),('b',30)]
>>> dates = np.array([np.datetime64('1970-01-01') + np.timedelta64(e[1],'D') for e in seq], dtype='datetime64')
>>> data = np.array([e[0] for e in seq])
>>>  ts = TimedSequence(dates, data)
```

### Chronicles

The core of the this package is the chronicle class that represents a chronicle temporal model which also offers efficient matching functionalities.


The chronicles handles two models of time (that must be consistent with the model of time in timed sequences):
* discrete timestamps using floats
* continuous timestamps using `datetime64` format. In this case the temporal constraints of a chronicle must be defined using `np.timedelta64` values.

A chronicle can not combine constraints of the two different kinds. The first defined constraint defines the model of time of the chronicle. 

<br>

The package implements efficient algorithms to recognize it. It benefits from numpy functionalities to increase their efficiency. There are three different ways to _recognize_ a chronicle in a sequence of a events:

* the absence/presence recognition (`c.match(seq)`): its result is a boolean stating whether the chronicle occur at least once in the sequence, this is the most efficient algorithm
* the occurrence enumeration (`c.recognize(seq)`): its result is a list of occurrences of the chronicle in a sequence. Contrary to the first function, it looks for all possible combination of events. Thus it is less efficient, but more informative.

Note that a chronicle is somehow similar to a simple temporal network and the set of constraints may be inconsistent or redundant. It is possible to _minimize_ the temporal constraints of a chronicle using the corresponding function.

```python
>>> c=Chronicle()
>>> c.add_event(0,'a')
>>> c.add_event(1,'b')
>>> c.add_event(2,'c')
>>> c.add_constraint(0,1, (1.0,2.0))
>>> c.add_constraint(0,2, (2.0,5.0))
>>> c.add_constraint(1,2, (0.0,2.0))
>>> print(c)
C1       {{[a],[b],[c]}}
0,1: (1.0, 2.0)
0,2: (2.0, 5.0)
1,2: (0.0, 2.0)

>>> c.minimize()
>>> print(c)
C1       {{[a],[b],[c]}}
0,1: (1.0, 2.0)
0,2: (2.0, 4.0)
1,2: (0.0, 2.0)
```

### Fuzzy chronicles

The `FuzzyChronicle` class represents a class for approximated recognition of a chronicle. The chronicle is defined in the same way of a chronicle. 
The temporal model is enriched with the modeling of a fuzzyness of temporal constraints (`lbda` parameter)

In addition to the matching function presented above, it proposes a `cmp` function that finds occurrences of a chronicle with a degree of matching (parameter `threshold`).

More details about fuzzy chroniclesis available in the [article](https://hal.archives-ouvertes.fr/hal-03698361) (in French):
```bibtex
@inproceedings{fchronicles,
  title = {{\'E}num{\'e}ration des occurrences d'une chronique},
  author = {Guyet, Thomas and Besnard, Philippe and Ben Salha, Nasreddine and Samet, Ahmed and Lachiche, Nicolas},
  booktitle = {Actes de la conférence Extraction et Gestion des Connaissances},
  publisher = {{\'E}ditions RNTI},
  pages = {253--260},
  year = {2020}
}
```

# Dataframe accessor

The `pychronicles` package include an new accessor for pandas dataframe. 
This accessor enables, denoted `tpattern` to use chronicle functionnalities directly with the pandas packages. In this case, you do not even need to manage your timed sequences by hand ... everything can be done directly with pandas.

The pandas accessor enables:

* to match or enumerate occurrences of a chronicle
* to match an Metric Temporal Logic (MTL) formula
* to abstract a collection of sequences 


## Spirit of the accessor

The spirit of our accessor is to use a pandas dataframe to encode a sequence or a collection of sequence. The index of the dataframe models the time ... it can be integer, float or date index. 

A column of the dataframe acn be defined to specify the identifier of the sequence. In the following example, the column name `id` denotes this identifier. Intuitivelly, it can be used to make `groupby` operations, to process a collection of timed sequences. 

The important feature of our package is that any other column can be added to the dataframe. The idea behind this modeling is that the dataframe gather all the information about the events. The columns describes each event (an can contain `None`). 


The example below illustrates the representation of a collection of sequences with a Pandas dataframe. 
The basic sequence is repeated three times to create a collection of three timed sequences. The index of the dataframe is defined with dates in this case. 
The event names of the basic sequence feed the column `label`, and we added two columns:


* a column `str_val` with the string values (twice the label)
* a column `num_val` with random numbers
* a column `id` that represents the identifier of a sequence.

```python
#create a basic sequence
seq = [('a',1),('c',2),('b',3),('a',8),('a',10),('b',12),('a',15),('c',17)]
df = pd.DataFrame({
    "label": [e[0] for e in seq]*3,
    "str_val": [e[0]*2 for e in seq]*3,
    "num_val": np.random.randint(10,size=3*len(seq)),
    'id': [1]*len(seq)+[2]*len(seq)+[3]*len(seq)
    },
    index = [np.datetime64('1980-01-01') + np.timedelta64(e[1],'D') for e in seq ]*3
)
```

<br>

Then, the definition of the event of a chronicle are no more the name of an event, but the description of a event of interest throught its description features. 
When used with pandas dataframe, the events of a chronicle are queries on the dataframe.
In the example above, an event could be defined by "`label=='a' & num_val>3`".

At the time, our framework handles string and number attributes. The specification of an event uses the classical operators defined in the [Pandas documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html). 

## Matching / enumerate occurrences of a chronicle

Let us now use a dataframe defined as explained in the previous section with chronicle. 

For that, we first need to define a chronicle. It works exactly as before but, the definition of chronicle's events are queries.

For instance, the following example illustrates the definition a simple chronicle that uses queries as event:
```python
c=Chronicle()
c.add_event(0,'label=="a"')
c.add_event(1,'label=="b" & num_val>5')
c.add_constraint(0,1, (np.timedelta64(4,'D'),np.timedelta64(10,'D')))
``` 

For more details about the syntax of queries, please refer to the [Pandas documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html). 

This chronicle is semantically sound for being used in with the dataframe defined in the example of the previous section. 

### Dataframe representing a sequence

In this section, we consider that the dataframe represents a unique sequence (for instance, we selected the first sequence of the previous dataframe with `df[df.id==1]`).

The recognition functionalities are now accessible throught the Pandas dataframe:

* `df.tpattern.match(c)` will return a boolean indicating whether the chronicle occurs in the sequence or not
* `df.tpattern.recognize(c)` will return the list of occurrences of `c` in the sequence

Note that the `tpattern` keyword gives access to the features of our package.

<br>

Using chronicles becomes very easy with Pandas dataframe and it also gains in expressivity thanks to the use of queries as event. 
We keep good computational efficiency of the recognition algorithms thanks to the use of the rewritting principle developed with semantic chronicles (see reference below). 

```bibtex
@inproceedings{semantic_chronicles,
  title = {An extension of chronicles temporal model with taxonomies -- Application to epidemiological studies},
  author = {Bakalara, Johanne and Guyet, Thomas and Dameron, Olivier and Happe, Andr{\'e} and Oger, Emmanuel},
  booktitle = {Proceedings of the 14th International Conference on Health Informatics (HEALTHINF)},
  pages = {1--10},
  year = {2021}
}
```

### Dataframe representing a collection of sequences

To proceed with a dataframe containing several sequences, you can use the following idioms based on `apply`:

```python
reco=df.groupby('id').apply(lambda d: d.tpattern.match(c))
```

In this case, the attribute `id` is used to select the events for each sequence, and then the `match` algorithm is applied to this selection.
The result is a dataframe containing a boolean value for each sequence id.

The same applies with `recognition` function.

## Use of MTL formula

For situation recognitinon, there are strong connection between chronicles and metric temporal logics such as MTL or TPTL. See the [article](https://hal.archives-ouvertes.fr/hal-03777471):
~~~bibtex
@inproceedings{chronicle_templogics,
  title = {Logical forms of chronicles},
  author = {Guyet, Thomas and Markey, Nicolas},
  booktitle = {Proceedings of the 29th International Symposium on Temporal Representation and Reasoning (TIME)},
  pages = {1--15},
  year = {2022}
}
~~~

To illustrate that the principle of semantic chronicles can be broader, we extended it to the case of MTL formulae. This means that our framework enables to express a MTL formulae using query as events. 


The `tpattern` accessor provides a function `match_mtl` that is dedicated to the recognition of a MTL formulae in the timed sequence. This function returns a boolean value. There is not equivalent to the enumeration of occurrences of a chronicle.

The syntax of an MTL formula is based on the two operators `F` (eventually) and `G` (globally). These operators can be specified with temporal constraints (in brackets). They combines events defined in the same way as for chronicle events.

```python
query = ' F(label=="a" & F[2.9,5]( label=="b" & num_val>5 ))'
df.tpattern.match_mtl(query)
```

This feature is based on the [Python implementation of MTL](https://github.com/mvcisback/py-metric-temporal-logic). 

## Abstraction of a sequence

Finally, we also provide a function that enables to abstract a collection of sequences into a chronicle. 

Contrary to the recognition functions that can handle several columns, the abstraction requires to define a column that correspond to the event name. In addition, it requires to define the attribute name that correspond to the identifier of the sequences. 
Then, the function, named `abstract` takes two arguments and outputs a single chronicle that occurs in all the sequences.


The following example extracts a chronicle from the dataframe introduced above. It focuses event on the label attribute.
```python
chro = df.tpattern.abstract('label', 'id')
```

# Additional features

## Export / import of chronicles

It is possible to specify chronicles using the CRS format. The following code illustrate the syntax for specifying a chronicle in this format.

```
chronicle C27_sub_0[]()
{
    event(Event_Type1[], t006)
	event(Event_Type1[], t004)
    event(Event_Type2[], t002)
    event(Event_Type3[], t001)

    t004-t006 in [17,25]
    t006-t002 in [-16,-10]
    t002-t001 in [14,29]
    t004-t001 in [27,35]
}
```

## Perspectives

* implementation of chronicle mining algorithms
* graphical chronicle editor
* better cythonize the recognition
* optimized matching of several chronicles at the same time


If you think that this package can be improved ... do not hesitate to contact the author to request additional features. He will do his best to maintain the code and improve it continuously.


# Authorship

* **Author:** Thomas Guyet
* **Institution:** Inria/AIstroSight
* **date:** 06/2024

