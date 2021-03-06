# Tree

## Introduction

Simple implementation of rooted, edge-labeled trees, that hold values at the
leaf nodes.

Examples of such trees are non-empty directory structures, where the directory
and file names are the edge labels, and the contents of a file are the values at
the leafs.

## Sample usage

```python
>>> from tree import Tree
>>> t = Tree()
>>> t[1, 2, 3] = 'x'
>>> t[1, 2, 3]
'x'
>>> t[2, 3] = 'y'
>>> t[3] = 'z'
>>> list(t.items())
[([1, 2, 3], 'x'), ([2, 3], 'y'), ([3], 'z')]
```

## Setup

Clone this repository, and run `make` for a set of options. To build the Sphinx documentation:

```
make build-docs
```

## Documentation

API documentation to be found at
https://bartfrenk.github.io/tree/build/index.html.
