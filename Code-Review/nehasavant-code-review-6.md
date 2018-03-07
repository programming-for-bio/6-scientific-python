## Neha Savant's Code Review for Assignment 6

#### Where did you get stuck in the assignment? What was the problem?
I got stuck when trying to understand how to modify the functions in the assignment to work as a class. And to get the functions to work together and within each other(i.e. `filter()` or `filter_seqlib()`). I also had some challenges putting together the Python package. I followed the examples from the last assignmnet on packaging but it was difficult to see which things were being referenced where (i.e. in the _init_.py and _main_.py files) because helloworld functions, packages and files were all named the same name. I think in general I understand how to set up a package and the basic functions involved in making it happen, but I need to understand more the functions of a _main_.py file or a setup.py file. 

#### What changes did you make upon seeing a completed version?
I didn't think to make separate public and private functions. So after seeing the completed version, I made that distinction. I also didn't think to have separate functions called `filter()` and `filter_seqlib()` . I also did not expect to see some of the functions changed as much as they were in the completed version (i.e. `_filter_missing`) to return a booleon array as opposed to the actual array of sequences. 

#### What did you learn from reviewing the completed assignment?
I learned that I need to go back to the numpy readings and readings about Python classes to get more familiar with how they operate. For example, I think I still get confused on when to call an internal attribute with `self.attribute`. I think having smaller, simpler exercises to explore the theoretical aspects of writing functions and classes in python would be helpful. Generally I undersatnd the way that the functions were written, but I'm not sure if I would be able to think up or write functions like that on my own. 

#### What aspect of the code/assignment is still confusing to you?
I addressed this question in some of my earlier answers (i.e. confused on using `self.`, how to write functions within classes and what the different parts of a package do). I'm also sitll unlcear about the distinction between API and CLI and which type is best to use when, which is likely a confusion I've carried over from Asmt 5. 