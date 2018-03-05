# Code-review

#### Where did you get stuck in the assignment? What was the problem?

I got stuck when trying to initiate my seqlib object. For reasons I can't understand, my python does not read the `_mutate()` function definition and keeps giving me the following error:
```
NameError: name 'mutate' is not defined
```
My code looks similar to the example, but still does not work.

#### What changes did you make upon seeing a completed version?

I made some changes:

(1) I forgot to account for missing data in my `_get_maf()` function, so I had to add that.

(2) I tried to make a single `filter()` function but then realized that they had to be split into `_filter_maf()` and `_filter_missing()`

#### What did you learn from reviewing the completed assignment?

I learned that making a package from scratch can be very challenging, specially when several functions depend on each other.

#### What aspect of the code/assignment is still confusing to you?

I still can't figure out why I keep getting this error when trying to create my seqlib object.
