from itertools import imap


class Tree(object):
    def __init__(self):
        self._children = {}

    def __getitem__(self, path):
        if len(path) == 1:
            return self._children[path[0]]
        return self._children[path[0]].__getitem__(path[1:])

    def __setitem__(self, path, value):
        if len(path) == 1:
            self._children[path[0]] = value
        else:
            child = self._children.setdefault(path[0], Tree())
            child.__setitem__(path[1:], value)

    def paths(self, prefix=None):
        return imap(lambda (p, _): p, self.items(prefix))

    def values(self):
        return imap(lambda (_, v): v, self.items())

    def items(self, prefix=None):
        """Return iterator over the (path, value) pairs in the tree, where path
        is a path from the root to a leaf, and value is the value at that leaf.

        :param prefix: List that gets prepended to every path.

        :rtype: An iterator.
        """
        prefix = prefix or []
        for (segment, t) in self._children.items():
            if isinstance(t, Tree):
                for p in t.items(prefix + [segment]):
                    yield p
            else:
                yield (prefix + [segment], t)
