### Where did you get stuck in the assignment? What was the problem?

I think the first part I got stuck on was the concept of using the `__init__` function to make other functions only require `self` as an argument. I ended up figuring it out (at least in the context of the `simulate` function) but I think it could maybe be explained a bit more in class or if there's not enough time (since I know two hours is very little time to cover the amount of material that we need), maybe have a section in a notebook explain it more in depth.

I also struggled for a long time with getting functions in the class object to refer to one another. I actually ended up giving up. I explain it a bit more in the next question.

In general, I struggle a lot with explaining the functions inside the .py file. Sometimes I don't know how to explain it or if I do, whether or not the way I explained things would be sufficient or not for users. 


### What changes did you make upon seeing a completed version?

I had to add `import copy`, `_filter_missing`, `_filter_maf`, `filter`, and `filter_seqlib` functions. I thought my filter functions was properly filtering things but I realize now that it was only getting rid of the sites with missing data and not filtering by maf as well. I'm also having trouble interpretting the result of `seqs.maf` for both my .py file and the provided .py file. I can see they give different results but I'm not sure how or why they differ and whether or not it makes a difference in the functions that come after. 

I struggled to get the `simulate` function to use `mutate` so I just added the code for `mutate` directly into the `newbase` portion of `simulate`. 

My `simulate` code reads: 
```
def simulate(self):
        oseq = np.random.choice(list("ACGT"), size=self.nsites)
        arr = np.array([oseq for i in range(self.ninds)])
        muts = np.random.binomial(1, 0.1, (self.ninds, self.nsites))
        for col in range(self.nsites):
            newbase = np.random.choice(list(set("ACTG") - set(arr[0, col])))
            mask = muts[:, col].astype(bool)
            arr[:, col][mask] = newbase
        missing = np.random.binomial(1, 0.1, (self.ninds, self.nsites))
        arr[missing.astype(bool)] = "N"
        return arr
```

If you have time, could you clarify: Is it necessary to have them as separate functions? Or can they be smashed into one function like I did? Or is it better to keep them as separate functions? 

One thing that I would have liked to change but I couldn't is getting the final question (`seqs.filter(minmaf=0.1, maxmissing=0.0).calculate_statistics()`) to actually run. It didn't seem to work with my .py file nor the provided .py file so I couldn't make any changes. I'm not sure if it's something I'm doing wrong or if other people are struggling to get that to work as well but I'd like to bugfix that problem.


### What did you learn from reviewing the completed assignment?

I learned how to get functions within a class object to refer to one another. This going to be extremely useful moving forward. I'm still not entirely sure if it's necessary for the `mutate` and `simulate` functions to be separate or if they can be combined but seeing how to keep them separate and have `simulate` take advantage of `mutate` is extremely helpful. I didn't realize you could refer to other functions by using `self.nameoffunction`. For some reason it only occurred to me to use that for arguments such as `self.ninds` or `self.nsites` but now that I see it in a code example it makes sense to me.


### What aspect of the code/assignment is still confusing to you?

I'm still completely baffled as to why I can't get the last question (stringing multiple functions together) to work.

This assignment helped me understand what should go in the `__init__` function of a class object but I think I could still use a bit of clarification on that. I'm pretty sure I now understand how to get functions to only require `self` as an argument but a little clarification on that would be helpful as well.