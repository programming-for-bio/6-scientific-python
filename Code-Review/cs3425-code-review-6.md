### Where did you get stuck in the assignment? What was the problem?
I initially got stuck with being able to access the mutate function within the class in the `simulate` function, which I solved by referecing it as `self.mutate`

`newbase = self.mutate(self.arr[0, col])`

I then could not figure out how to make attributes of the class and return them from functions. I also wasn't sure what the instructions meant by "apply a new function `filter()`"
One thing I'm also not sure about why we do this is naming the class the same thing as the package but with a capital instead of lowercase. Does it make a difference or is it just good practice?

### What changes did you make upon seeing a completed version?
I added the `maf` attribute as `self.maf = self._get_maf()`, added the modified function to return `maf`, and set the internal functions as private as well. 
I added the public filter() function and had to change a few parts of the `_filter_missing()` and `_filter_maf()` functions to get it to work. 
I also imported the copy library since that was used in the `filter_seqlib()` function that was added. 
I added the correct `calculate_statistics()` function since mine was wrong. 

### What did you learn from reviewing the completed assignment?
Reviewing the assignment in class was really helpful because I was having a hard time with the Class/package relationship and use conceptually and understanding their components and when to use certain concepts. 
Reviewing it based on the complete library was helpful because I was able to add certain parts one at a time and see what changed. 

### What aspect of the code/assignment is still confusing to you?
I think I'm still a little unclear on the difference between returning and storing attributes and also how to create/use attributes like `maf`
I also still couldn't get the last question of the nb-6.5 notebook to work as it stringed up as `seqs.filter(minmaf=0.1, maxmissing=0.0).calculate_statistics()`
but it did work when I broke it in to two lines
