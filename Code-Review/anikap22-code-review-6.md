# where did you get stuck in the assignment? What was the problem?
The primary place where I got stuck was not understanding how to store the sequence array to access it later. I tried to make many work arounds which further degraded the code.
The correct solution was:
```python
self.maf = self._get_maf()
```

Initially I had tried to store the maf as:
```phython
self.maf = np.zeros(nsites, ninds)
```
which creates an object you cannot store into later.

I also ran into problems with using ```seq.filter().calculate_statistics()```. It worked ok when I called ```calculate_statistics()``` on it's own because it was remaking the sequence. But when I tried to pass it a filtered sequence it gave the error:
```python
AttributeError: 'numpy.ndarray' object has no attribute 'calculate_statistics'
```
The problem is that the ```seq.filter``` was completely disconnected from the calculate statistics part and so I couldn't pass arguments between the two parts. 

# what changes did you make upon seeing a completed version?
There were a number of sections in the code that needed changes. Here I have described the errors and how they were fixed.
1. I put ```#!/usr/bin/env python``` in the ```__main__.py``` file instead of the actual script ```seqlib.py```. (This was fixed by adding the environemnt to the ```seqlib.py``` file).
2. I didn't include ```import copy``` (added that to the ```seqlib.py``` file)
3. Mutate should have been a private function so that it is only seen internally. I changed the ```def mutate(self):``` to ```def _mutate(self):```. Same with the ```simulate``` function, ```filter_missing```, and ```filter_maf```.
4. I changed the ```get_maf``` function (changed the name from maf to get maf) to return the seqarray before counting the N's. This involved creating an array of 0's using ```np.zeros``` and filling it from a mask.Initially I had only included the part calculating frequencies and below.
5. I added ```filter_seqlib``` which returns the seqlib object rather than the array from the ```filter``` function. 

# What did you learn from reviewing the completed assignment?
I learned that it's very important to initialize objects in the init part of the class object so that they can be accessed by all functions. I also learned the difference between a seqlib object and an nparray. As many functions as possible should be hidden functions so as to not confuse the user. Furthermore, I learned that the python path needs to go at the top of the class object scripts rather than in the ```___main___.py``` file. 


# what aspect of the code/assignment is still confusing to you?
I am still a little bit confused aobut why we couldn't store the output in an array in the ```init``` part of the class object. I am also not sure what the two lines in ```filter_seqlib``` do that use ```deepcopy``` and ```newseqs```:
```python
newself = copy.deepcopy(self)       
newself.__init__(newseqs.shape[0], newseqs.shape[1]) 
````
I am also not sure what the reason for inverting on the last line of the ```filter``` function is:
```python
return self.seqs[:, np.invert(fullfilter)]
```
