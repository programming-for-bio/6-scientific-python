

## Mvanack Code Review for SeqLib

### 1.) Where did you get stuck in the assignment? What was the problem?


I got stuck when I needed to calculate the statistics for the array following filtering the array, the error was showing that SeqLib class had no attribute for calculate statistics 


### 2.) What changes did you make upon seeing a completed version?

I left the filter_missing and filter_MAF functions similar to the original code and instead made a new function to reassign minmaf and maxmissing to the maxfreq and minfreq as seen here:


``` python

def descriptive(self, minmaf, maxmissing):
        job1 = self.filter_missing(maxfreq = maxmissing)
        freqs = np.sum(job1 != job1[0], axis=0) / job1.shape[0]  
        maf = freqs.copy() 
        maf[maf > 0.5] = 1 - maf[maf > 0.5] 
        return job1[:, maf > minmaf] 

```

Whereas the example code example used minmaf and max missing directly with filter missing and filter maf. I added the get_maf function and the self.maf empty array at the top of the code to store the MAFs.


### 3.) What did you learn from reviewing the completed assignment?

I had not designated private and public functions in my code and had the simulate function as a public function, this was something I incorporated in the updated code. I also had not thought to make filter_missing and filter_maf a private function that could run within the public function filter. 
I did not provide and if;else statement for the statistics function which could be important depending on the input values. I did not think to make a copy of teh new filtered array either. The example code example used minmaf and max missing directly with filter missing and filter maf


### 4.) What aspect of the code/assignment is still confusing to you?

The self idea is still confusing to me. I understand it in simple code but do not understand when to implement it in more complicated coding like this. I also don't understand exactly what the get_maf function is doing in the exmaple code. 

I had originally tried to filter the missing sequences and then filter for MAF by nesting the two arguments in one function as in the following:

``` python

def decriptive(self, minmaf, maxmissing):
	obj1 = self.filter_maf(self.filter_missing(maxmissing), minmaf)
	return obj1

```

However, this code recieevd an error that it exceeded the postional arguments. Are you able to nest arguments within each other like this?