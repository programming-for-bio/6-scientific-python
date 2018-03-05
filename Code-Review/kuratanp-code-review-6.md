# Code Review

#### Q1. Where did you get stuck in the assignment? What was the problem?

I got stuck when I tried to modify my code to access information about the Class object using self. After modifying my code based on Deren's, I still got errors. So I copied all of Deren's code and tried again and got the following error message. 

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-34-36681df8858c> in <module>()
      1 import seqlib
----> 2 s = seqlib.Seqlib(10, 100)

TypeError: __init__() missing 3 required positional arguments: 'arr', 'maxfreq', and 'minfreq'
---------------------------------------------------------------------------
```

#### Q2. What changes did you make upon seeing a completed version?

a) added more import

```
import copy
```

b) made the following changes

```
def __init__(self, ninds, nsites, maxfreq, minfreq):   --->    def __init__(self, ninds, nsites):

self.seqs = self.simulate()   --->   self.seqs = self._simulate()
```

c) added more code

```
store maf of the full seq array
self.maf = self._get_maf()
```
d) changed public to private function

```
newbase = mutate(arr[0, col])  --->  newbase = self._mutate(arr[0, col])

def simulate(self):  --->   def _simulate(self):
```

e) inserted the entire code of the _get_maf function

```
    def _get_maf(self):
        "returns the maf of the full seqarray while not counting Ns"
        maf = np.zeros(self.nsites)
        for col in range(self.nsites)
            thiscol = self.seqs[:, col]
            nmask = thiscol != "N"
            no_n_len = np.sum(nmask)
            first_non_n_base = thiscol[nmask][0]
            freq = np.sum(thiscol[nmask] != first_non_n_base) / no_n_len
            if freq > 0.5:
                maf[col] = 1 - freq
            else:
                maf[col] = freq
        return maf
```

f) switched code as follows

```
def filter_missing(self):   --->   def _filter_missing(self, maxmissing):

freqmissing = np.sum(self.arr == "N", axis=0) / self.arr.shape[0] 
--->  
freqmissing = np.sum(self.seq == "N", axis=0) / self.seq.shape[0]
```

g) switched public to private function, added minmaf parameter

```
def filter_maf(self):
delete the rest and added

def _filter_maf(self, minmaf):
    
    "returns a boolean filter True for columns with maf < minmaf"
    return self.maf < minmaf
```

h) added the entire filter function

```
    ## public functions -----
    def filter(self, minmaf, maxmissing):
        """
        Applies maf and missing filters to the array 
        Parameters
        ----------
        minmaf: float
            The minimum minor allele frequency. Filter columns below this.
        maxmissing: float
            The maximum prop. missing data. Filter columns with prop Ns > this.
        """
        filter1 = self._filter_maf(minmaf)
        filter2 = self._filter_missing(maxmissing)
        fullfilter = filter1 + filter2
        return self.seqs[:, np.invert(fullfilter)]
```

i) added the filter_seqlib function

```
    def filter_seqlib(self, minmaf, maxmissing):
        """
        Applies maf and missing filters to the array and returns a copy 
        of the seqlib object where the .seqs array has been filtered
        Parameters
        ----------
        minmaf: float
            The minimum minor allele frequency. Filter columns below this.
        maxmissing: float
            The maximum prop. missing data. Filter columns with prop Ns > this.
        """
        ## apply filters to get new array size
        newseqs = self.filter(minmaf, maxmissing)

        ## make a new copy of the seqlib object
        newself = copy.deepcopy(self)       
        newself.__init__(newseqs.shape[0], newseqs.shape[1]) 

        ## store the array (overwrite it)
        newself.seqs = newseqs

        ## call the _get_maf to match new array
        newself._get_maf()
        return newself
```       
j) changed arr to seq

For example:
```
nd = np.var(self.arr == self.arr[0], axis=0).mean()  
---> 
nd = np.var(self.seqs == self.seqs[0], axis=0).mean()
```

Added below:
```
    def calculate_statistics(self):
        """ 
        Returns a dataframe of statistics on the seqs array. The earlier 
        example from the notebook had a bug where var and inv were switched.
        """
        if self.seqs.size:
            nd = np.var(self.seqs == self.seqs[0], axis=0).mean()
            mf = np.mean(
                np.sum(self.seqs != self.seqs[0], axis=0) / self.seqs.shape[0])
            inv = np.all(self.seqs == self.seqs[0], axis=0).sum()
            var = self.seqs.shape[1] - inv
            return pd.Series(
                {"mean nucleotide diversity": nd,
                 "mean minor allele frequency": mf,
                 "invariant sites": inv,
                 "variable sites": var,
                })
        else:
            print("seqs array is empty")
            
```



#### Q3. What did you learn from reviewing the completed assignment?

Reviewing the completed assignment was extremely helpful. It is very tough to ask questions through Gitter Chatroom, when you have no clue what went wrong. 
I am hoping that the lecture on Monday will clarify some of my questions. 

#### Q4. what aspect of the code/assignment is still confusing to you?

a) writing code to access information about the Class object using self is confusing to me.
Deren's working version didn't work for me and I am not sure why. 

b) more specifically, I am confused by how to write the __init__ function as to what parameters to add, what attributes to write etc. 

C) Other specific questions:

private vs public function - I understand the difference between those two but I am still kind of confused.
