# Code Review 

### Where did you get stuck in the assignment? What was the problem?
#### I had a hard time getting the function with multiple arguments to. This function was the one that had filter(min,max).calculate_statistics(). I couldn't figure out how to get the program to recognize both attributes of the function.

### What changes did you make upon seeing a completed version?
#### I had stored many more attributes in the init function than I needed too. So I went through and removed those. All that changed was how I needed to call the function when using it in python. I also changed the filter functions.
    
### What did you learn from reviewing the completed assignment?
#### The filter functions made more sense to me after reviewing the completed assignment. Also, how the functions fit into together within the larger class item made more sense to me. 

### What aspect of the code/assignment is still confusing you?
#### When I ran the altered code it was still telling me that simulate wasnt part of seqlib. So i went back to my seqlib.py file and added the self.simulate() into the init function. I'm a little confused as to how to make it work without that, since I feel like it should be running the simulate in order to make the array its supposed to output. I think I am also a little confused on how the double argument works, the same one that I mentioned in the first question. Also, I couldnt get this new code to actually fill in the filtered array, so the filter.calcualate_statistic was just giving me the 'else' response. "