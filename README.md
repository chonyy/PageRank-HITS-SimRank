<p align=center>
    <img src="img/graph_4.png">
</p>

<p align=center>
    <a target="_blank" href="https://travis-ci.com/chonyy/AI-basketball-analysis" title="Build Status"><img src="https://travis-ci.com/chonyy/AI-basketball-analysis.svg?branch=master"></a>
    <a target="_blank" href="#" title="language count"><img src="https://img.shields.io/github/languages/count/chonyy/PageRank-HITS-SimRank"></a>
    <a target="_blank" href="#" title="top language"><img src="https://img.shields.io/github/languages/top/chonyy/PageRank-HITS-SimRank?color=orange"></a>
    <a target="_blank" href="https://opensource.org/licenses/MIT" title="License: MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
    <a target="_blank" href="#" title="repo size"><img src="https://img.shields.io/github/repo-size/chonyy/PageRank-HITS-SimRank"></a>
    <a target="_blank" href="http://makeapullrequest.com" title="PRs Welcome"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg"></a>
</p>

> Python implementation of famous link analysis algorithms.

- HITS Algorithm
- PageRank Algorithm
- SimRank Algorithm

## How to use

### Install the Pypi package using pip

```
pip install fpgrowth_py
```

Then use it like 

```python
from fpgrowth_py import fpgrowth
itemSetList = [['eggs', 'bacon', 'soup'],
                ['eggs', 'bacon', 'apple'],
                ['soup', 'bacon', 'banana']]
freqItemSet, rules = fpgrowth(itemSetList, minSupRatio=0.5, minConf=0.5)
print(freqItemSet)
print(rules)  
# [[{'beer'}, {'rice'}, 0.6666666666666666], [{'rice'}, {'beer'}, 1.0]]
# rules[0] --> rules[1], confidence = rules[2]
```

### Clone the repo

Get a copy of this repo using git clone
```
git clone https://github.com/chonyy/fpgrowth_py.git
```

Run the program with dataset provided and **default** values for *minSupport* = 0.5 and *minConfidence* = 0.5

```
python fpgrowth.py -f dataset.csv
```

Run program with dataset and min support and min confidence  

```
python fpgrowth.py -f tesco2.csv -s 0.5 -c 0.5
```
