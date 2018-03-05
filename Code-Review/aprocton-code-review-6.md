# Assignment 6 Code Review

#### Alexander M. Procton
#### 3.5.2018

* __Where did you get stuck in the assignment? What was the problem?__
  
  I successfully completed most of the original assignment. The only parts I did not implement were the `self.maf` attribute for `Seqlib` objects, because I ran out of time. I did not expect as many challenges in working with stored attributes of objects as I encountered.

* __What changes did you make upon seeing a completed version?__

  My completed version was changed to match the test code by implementing `_get_maf()` and `filter_seqlib()` functions. I changed `filter_missing()` and `filter_maf()` to return boolean arrays that could be called by `filter()`. I also fixed `calculate_statistics` to match the updated example and reorganized my code so that `mutate()`, `filter_missing()`, and `filter_maf()` were private internal functions, instead of being defined them outside the class.

  _My original `mutate()`, `filter_missing()`, and `filter_maf()`:_

  ```python
  def mutate(base):
      diff = set("ACTG") - set(base)
      return np.random.choice(list(diff))

  def filter_missing(arr, maxfreq):
      # determine the frequency of missing reads at a site
      freqmissing = np.sum(arr == "N", axis=0) / arr.shape[0]
      
      # return arr, sliced to only include cols with freqmissing <= maxfreq
      return arr[:, freqmissing <= maxfreq]

  def filter_maf(arr, minfreq):
      # determine proportion of alleles in a col that do not match the first row
      freqs = np.sum(arr != arr[0], axis=0) / arr.shape[0]
      
      # create a copy of freqs with all values > 0.5 changed to their complement
      maf = freqs.copy()
      maf[maf > 0.5] = 1 - maf[maf > 0.5]
      
      return arr[:, maf > minfreq]
  ```

  _My modified `_mutate()`, `_filter_missing()`, and `_filter_maf()` and the new function `_get_maf()`:_

  ```python
  def _mutate(self, base):
      diff = set("ACTG") - set(base)
      return np.random.choice(list(diff))

  def _get_maf(self):
      # determine proportion of alleles in a col that do not match row 1
      freqs = np.sum(self.seqs != self.seqs[0], axis=0) / self.seqs.shape[0]

      # create a copy of freqs with all values > 0.5 changed to complements
      maf = freqs.copy()
      maf[maf > 0.5] = 1 - maf[maf > 0.5]

      return maf

  def _filter_missing(self, maxfreq):
      # determine the frequency of missing reads at a site
      freqmissing = np.sum(self.seqs == "N", axis=0) / self.seqs.shape[0]

      # return arr, sliced to only include cols with freqmissing <= maxfreq
      return freqmissing <= maxfreq

  def _filter_maf(self, minfreq):
      return self.maf > minfreq
  ```

* __What did you learn from reviewing the completed assignment?__
  
  I became much more familiar with how to call functions that are only defined within classes, and gained familiarity with `copy.deepcopy()`.

* __What aspect of the code/assignment is still confusing to you?__

  If the `+` operator can be used for boolean AND, is there a single operator that is used for boolean OR?