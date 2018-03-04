## Code Review for Wenyi909's `seqlib` package
### Code Examples to test modified package
Command_1 and Output:
```
import seqlib
s = seqlib.Seqlib(8, 20)
print(s.seqs)
```

```
[['A' 'T' 'A' 'C' 'G' 'A' 'C' 'A' 'A' 'C' 'G' 'C' 'C' 'G' 'G' 'C' 'N' 'A'
  'N' 'A']
 ['A' 'T' 'A' 'C' 'G' 'A' 'C' 'A' 'A' 'C' 'G' 'C' 'C' 'G' 'T' 'N' 'T' 'N'
  'C' 'N']
 ['A' 'T' 'A' 'C' 'G' 'A' 'N' 'A' 'A' 'C' 'T' 'C' 'C' 'C' 'T' 'C' 'T' 'A'
  'C' 'N']
 ['A' 'T' 'A' 'C' 'G' 'A' 'C' 'A' 'A' 'C' 'G' 'C' 'C' 'G' 'T' 'C' 'T' 'A'
  'C' 'G']
 ['A' 'N' 'A' 'C' 'G' 'A' 'C' 'G' 'A' 'C' 'G' 'C' 'T' 'G' 'N' 'N' 'T' 'A'
  'C' 'A']
 ['A' 'T' 'A' 'C' 'G' 'A' 'N' 'A' 'T' 'C' 'T' 'C' 'C' 'G' 'T' 'C' 'T' 'A'
  'C' 'N']
 ['N' 'T' 'A' 'N' 'G' 'A' 'C' 'A' 'A' 'T' 'G' 'C' 'C' 'G' 'T' 'C' 'T' 'A'
  'C' 'N']
 ['A' 'N' 'A' 'C' 'G' 'A' 'N' 'G' 'A' 'C' 'G' 'C' 'N' 'G' 'T' 'T' 'A' 'C'
  'C' 'G']]
```

Command_2 and Output:
`print(s.maf)`

```
[0.         0.         0.         0.         0.         0.
 0.         0.25       0.125      0.125      0.25       0.
 0.14285714 0.125      0.14285714 0.16666667 0.14285714 0.14285714
 0.         0.5       ]
```

Command_3 and Output:
`print(s.filter.seqlib(minmaf=0.1, maxmissing=0.0))`

`<seqlib.seqlib.Seqlib at 0x10d8346d8>`

Command_4 and Output:
`s.calculate_statistics()`

```
invariant sites                 4.000000
mean minor allele frequency     0.300000
mean nucleotide diversity       0.123438
variable sites                 16.000000
dtype: float64
```

Command_5 and Output:
`s.filter_seqlib(minmaf=0.1, maxmissing=0.0).calculate_statistics()`

```
invariant sites                4.000000
mean minor allele frequency    0.097222
mean nucleotide diversity      0.078125
variable sites                 5.000000
dtype: float64
```

### Where did you get stuck in the assignment? What was the problem?
I stuck at the last part of the assignment, in which we need to calculate statistics for an array after filtering it. I created two functions `filter` and `calculate_statistics`, which seems to work fine separatly. But when I performed: `seq.filter(minmaf=0.1, maxmissing=0.0).calculate_statistics()`

The program returned:

    AttributeError: 'numpy.ndarray' object has no attribute 'calculate_statistics'
I think this is because my `filter` function returns a numpy array object, instead of a seqlib object, shown below:

	def filter(self, maxmissing, minmaf):
        freqmissing = np.sum(self.seqs == "N", axis=0) / self.seqs.shape[0]
        arr = self.seqs[:, freqmissing <= maxmissing]
        freqs = np.sum(arr != arr[0], axis=0) / arr.shape[0]
        maf = freqs.copy()
        maf[maf > 0.5] = 1 - maf[maf > 0.5]
        return arr[:, maf > minmaf]
Therefore the object after filtering does not have `calculate_statistics` attribute.

### What changes did you make upon seeing a completed version?
1. I changed funtions `mutate`, `simulate`, `maf`, `filter_missing`, and `filter_maf` into private functions;
2. I fixed the bug in the function `calculate_statistics` where
`inv = np.all(self.seqs == self.seqs[0], axis=0).sum()`
3. I changed my functions `_maf` according to the completed version, so that before calculating maf, the function first gets rid of all the Ns.
4. In order to fix the problem where I got stuck, I did what the completed version did, which modified the functions `_filter_missing` and `_filter_maf` to return boolean filters instead of arrays. And then we added function `filter` and `filter_seqlib` which combined the two boolean filters together to the array and returns a copy of the seqlib object.

### What did you learn from reviewing the completed assignment?
I learnt that the type of variable being returned actually affects the results a lot. It's really important to always trace the function variables, seeing what are the inputs and what is the output.

### What aspect of the code/assignment is still confusing to you?
1. I do not understand the part in function `filter` where 
	`fullfilter = filter1 + filter2`
	If `filter1` is `True` and `filter2` is `false`, what would `fullfilter` be?
2. In function `filter_seqlib`, we copied self to newself by writing
	`newself = copy.deepcopy(self)`
	What does this mean?
3. At the end of funtion `filter_seqlib`, we write
	`newself.maf()`
	Why and what does this do?
