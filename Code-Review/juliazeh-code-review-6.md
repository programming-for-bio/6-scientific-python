# Code Review Assignment 6 - juliazeh

## Where did you get stuck in the assignment? What was the problem?

I first got stuck on using `mutate` in `simulate`, something which I worked out eventually but which made more sense after I saw the private functions which could be used in later functions. Part of the issue was also that I wasn't sure if I had to put `mutate` in `__init__` in order for me to be able to call it in the `mutate` function.

I also got stuck importing my package into python because I wasn't able to install it in the command line. I was still unclear on which files are necessary for CLI and which are for API.

Everything else I was able to figure out after a few tries, this assignment just took me a really long time to complete. The final question in checking to make sure my class object worked was a really difficult question that I was not able to figure out before the assignment was due. I could not figure out how to combine two functions from `seqlib` even after trying for over an hour.

## What changes did you make upon seeing a completed version?

My original code did not use any private functions, mostly because I'm still a little unclear on when to make a function private and when to make it public. I didn't import `copy` because my original code used `copy` through `numpy`. I also forgot to add comments and definitions for functions, so I added those.

My original code for getting an array of maf values looked like this:
```
freqs = np.sum(self.seqs != self.seqs[0], axis=0) / self.seqs.shape[0]
maf = freqs.copy()
return maf
```
I had a lot of trouble coming up with code that would ouptut the maf values correctly and realize now that my code only found maf for the first column. I needed to iterate over the whole array, which I see now is easily done after initiating an array of 0s first.

In my original code for the  `filter_missing` function, I added `anarray` so that in `filter()` later I had the right number of arguments:
```
def filter_missing(self, anarray, maxmissing):
        freqmissing = np.sum(anarray == "N", axis=0) / anarray.shape[0]
        return anarray[:, freqmissing <= maxmissing]
```

For the `filter` function I simply applied both `filter_missing` and `filter_maf` and added `anarray` to `filter_missing` so that I could input the result of `filter_maf` into `filter_missing`:
```
    def filter(self, minmaf, maxmissing):
        return self.filter_missing(self.filter_maf(minmaf), maxmissing)
```

I also didn't reduce `filter_maf` after adding `_get_maf()`, which I did after seeing a completed version. This makes the code less cluttered, but the original function I had copied from the assignment notebook did not cause any problems.

## What did you learn from reviewing the completed assignment?

Reviewing the completed assignment, I reviewed defining functions and classes and I learned that I need __init__.py and __setup__.py files for writing a class object for API even without also writing it for CLI. I also learned that I need to set aside a lot of time for trial and error when working on programming assignments!

## What aspect of the code/assignment is still confusing to you?
I'm still confused about the different data types that were created by the functions which led me to problems with the last question. I'm not sure why an array was created instead of a Seqlib object and how to get around an error like this in the future. I'm also still a little confused about when to use private functions. I also could probably learn to be more efficient in an assignment like this because it took me so long.
