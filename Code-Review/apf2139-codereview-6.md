# Code Review

### where did you get stuck in the assignment? What was the problem?

I was stuck in a number of places. For example, I did not understand the conversion to self.seqs from arr in the original code. See below:

```
    def _filter_missing(self, maxmissing):
        freqmissing = np.sum(self.seqs == "N", axis=0) / self.seqs.shape[0]
        return freqmissing > maxmissing
        # made fxn rpviate + replaced two instances of "arr" with "self.seqs"
```

There were a variety of other problems with my code but the usage of self was one of the things that confused me and tripped up my code.

### what changes did you make upon seeing a completed version?

I made a large number of changes. For example, I made many functions private (preceeded by an underscore); removed some entire attempts at adding new functions; and added some entire new functions that I still do not quite understand.

One exmple of a change I made:
```
    def _simulate(self):
        oseq = np.random.choice(list("ACGT"), size=self.nsites)
        arr = np.array([oseq for i in range(self.ninds)])
        muts = np.random.binomial(1, 0.1, (self.ninds, self.nsites))
        for col in range(self.nsites):
            newbase = self._mutate(arr[0, col])
            # made the above line self._mutate() instead of just mutate()
            mask = muts[:, col].astype(bool)
            arr[:, col][mask] = newbase
        missing = np.random.binomial(1, 0.1, (self.ninds, self.nsites))
        arr[missing.astype(bool)] = "N"
        return arr
        # self.arr = arr #this did not work.
        # using return arr means init will print out arr? or pass > next fxn?
        # I also made this fxn private
```

I commented some of the changes I made and some of the confusion I had.

### What did you learn from reviewing the completed assignment?

I learned a lot more about classes in python. Thankfully I was able to write, install and use the package effectively, even if the code itself was broken; however it was still a good exercise in that regard also.

### what aspect of the code/assignment is still confusing to you?

There is much that is still confusing, and this new code warrants much more time and in-depth analysis than I have been able to devote just yet. But two areas of confusion that appear first and foremost are the usage of the following code:

```
s.filter_seqlib(minmaf=0.1, maxmissing=0.0).calculate_statistics()
```

which calls an error. The second is the usage of the copy package, which does not appear to function properly for some reason. The nonfunctional line above may actually even be related to the nonfunctional copy package calling, since if filter_seqlib does not function then calculate stats won't function either. Copy is used in filter_seq lib; deepcopy is used, to make a "deep copy" including any embedded objects. But I am not so sure yet.