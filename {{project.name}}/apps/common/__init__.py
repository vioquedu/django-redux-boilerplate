# -*- coding: utf-8 -*-
from collections import defaultdict
import time

nvd3datefmt = lambda d: int(time.mktime(d.timetuple()) * 1000)

REPL = {True: u"Sí", False: u"No"}


class Table(dict):

    def __init__(self, header='', margin=None, bottom=None, right=None, replace=None):
        self.header = header
        self.margin = margin
        self.bottom = bottom
        self.right = right
        self.repl = REPL if replace is None else replace
        self.cols = set()
        self.rows = set()

    def __setitem__(self, key, value):
        c, r = key
        self.cols.add(c)
        self.rows.add(r)
        return super(Table, self).__setitem__(key, value)

    def __iter__(self):
        if self.margin is None:
            return self.get_values()
        else:
            return self.get_values_with_margins()

    def replace(self, value):
        return self.repl.get(value, value)

    def get_values(self):
        cols = sorted(list(self.cols))
        rows = sorted(list(self.rows))
        if self.right:
            header = [self.header] + cols + [self.right[0]]
        else:
            header = [self.header] + cols
        yield map(self.replace, header)
        for i, r in enumerate(rows, 1):
            row_values = []
            for c in cols:
                value = self.get((c, r), 0.0)
                row_values.append(value)
            if self.right:
                yield map(self.replace, [r] + row_values + [self.right[i]])
            else:
                yield map(self.replace, [r] + row_values)
        if self.bottom:
            yield map(self.replace, self.bottom)

    def get_values_with_margins(self):
        cols = sorted(list(self.cols))
        rows = sorted(list(self.rows))
        header = [self.header] + cols + ["Total"]
        yield map(self.replace, header)
        col_values = defaultdict(list)
        for r in rows:
            row_values = []
            for c in cols:
                value = self.get((c, r), 0.0)
                row_values.append(value)
                col_values[c].append(value)
            yield map(self.replace, [r] + row_values + [self.margin(row_values)])
        footer = [self.margin(col_values[c]) for c in cols]
        yield map(self.replace, ["Total"] + footer + [self.margin(footer)])
