#!/usr/bin/env python
"""
Creates a class object called "Assembler" which
"""

import numpy as np
import pandas as pd

class Seqlib():
    """
    An object for
    """
    def __init__(self, ninds, nsites):
        # store attributes
        self.ninds = ninds
        self.nsites = nsites
        self.seqs = self.simulate()
        self.maf = self.maf_array()
        
    def mutate(base):
        diff = set("ACTG") - set(base)
        return np.random.choice(list(diff))

    def simulate(self):
        pass
        oseq = np.random.choice(list("ACGT"), size=self.nsites)
        arr = np.array([oseq for i in range(self.ninds)])
        muts = np.random.binomial(1, 0.1, (self.ninds, self.nsites))
        for col in range(self.nsites):
            diff = set("ACTG") - set(arr[0, col])
            newbase = np.random.choice(list(diff))
            mask = muts[:, col].astype(bool)
            arr[:, col][mask] = newbase
        missing = np.random.binomial(1, 0.1, (self.ninds, self.nsites))
        arr[missing.astype(bool)] = "N"
        return arr

    def maf_array(self):
        freqs = np.sum(self.seqs != self.seqs[0], axis=0) / self.seqs.shape[0]
        maf = freqs.copy()
        return maf

    def filter_missing(self, anarray, maxmissing):
        freqmissing = np.sum(anarray == "N", axis=0) / anarray.shape[0]
        return anarray[:, freqmissing <= maxmissing]

    def filter_maf(self, minmaf):
        freqs = np.sum(self.seqs != self.seqs[0], axis=0) / self.seqs.shape[0]
        maf = freqs.copy()
        maf[maf > 0.5] = 1 - maf[maf > 0.5]
        return self.seqs[:, maf > minmaf]

    def filter(self, minmaf, maxmissing):
        return self.filter_missing(self.filter_maf(minmaf), maxmissing)

    def calculate_statistics(self):
        nd = np.var(self.seqs == self.seqs[0], axis=0).mean()
        mf = np.mean(np.sum(self.seqs != self.seqs[0], axis=0) / self.seqs.shape[0])
        inv = np.any(self.seqs != self.seqs[0], axis=0).sum()
        var = self.seqs.shape[1] - inv
        return pd.Series(
            {"mean nucleotide diversity": nd,
             "mean minor allele frequency": mf,
             "invariant sites": inv,
             "variable sites": var, }
        )