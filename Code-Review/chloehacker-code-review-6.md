# Code Review

#### Q: Where did you get stuck in the assignment? What was the problem?

A: I got stuck with formatting the code properly in the seqlib.py file. None of my code was executable
and I struggled with formatting it properly.

#### Q: What changes did you make upon seeing a completed version?

A: First, I deleted my ```__main__.py``` file because I don't think you need that for the python (API) package but just for CLI?
I added 
```
import copy
## store maf of the full seq array
        self.maf = self._get_maf()
```
I added this whole function, as it was nonexistant before. 
```
def _get_maf(self):
 "returns the maf of the full seqarray while not counting Ns"
        ## init an array to fill and iterate over columns
        maf = np.zeros(self.nsites)
        for col in range(self.nsites):
            ## select this column of bases
            thiscol = self.seqs[:, col]

            ## mask "N" bases and get new length
            nmask = thiscol != "N"
            no_n_len = np.sum(nmask)

            ## mask "N" bases and get the first base
            first_non_n_base = thiscol[nmask][0]

            ## calculate maf of "N" masked bases
            freq = np.sum(thiscol[nmask] != first_non_n_base) / no_n_len
            if freq > 0.5:
                maf[col] = 1 - freq
            else:
                maf[col] = freq
        return maf
```
And also, for all of the other functions, I had parts of it that were correct but overall it was totally wrong and giving me an error, so I fixed all of that.
Example:
changed this
```
def filter_missing(self, maxfreq):   
        arr = self.seqs
        freqmissing = np.sum(arr == "N", axis=0) / arr.shape[0]  
        return arr[:, freqmissing <= maxfreq]
```
to this
```
    def _filter_missing(self, maxmissing):
        "returns a boolean filter True for columns with Ns > maxmissing"
        freqmissing = np.sum(self.seqs == "N", axis=0) / self.seqs.shape[0]
        return freqmissing > maxmissing
```
So it seemed like the general concept was kind of there but I didn't edit it properly to fit with the rest of the class object.
#### Q: What did you learn from reviewing the completed assignment?

A: I learned that I was at least on the right track but did not execute the actual code correctly so it made it impossible to runthe seqlib library. Also, I probably need to go back a few weeks and review some of that material so I am more comfortable with it. 

#### Q: What aspect of the code/assignment is still confusing to you?

A: How some of the functions actually work still confuses me. And then just generally, I still dont 
really get how to push files from my terminal to my github efficiently, and make them into a folder in github. 
I just upload them all manually which I know you aren't supposed to do but yeah that aspect is still difficult for me.
