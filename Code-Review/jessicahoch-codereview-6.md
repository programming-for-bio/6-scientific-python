## **Where did you get stuck in the assignment? What was the problem?**

I got stuck in the final question which involved stringing multiple functions together. There were a couple of substantial problems including the absence of a mutate function. I used a lot of the old code which resulted in the functions taking the wrong arguments, which is why most of the functions weren't working. 

## **What changes did you make upon seeing a completed version?**

Most of my arguments from old code had to be changed. For example: 

'''
def mutate(base):
    diff = set("ACTG") - set(base)
    return np.random.choice(list(diff))
    '''

'''
 def _mutate(self, base):
        "converts a base to another base"
        diff = set("ACTG") - set(base)
        return np.random.choice(list(diff))
        '''
        
## **What did you learn from reviewing the completed assignment?**

Assigning private/public and how functions fit together within a class. 

## **What aspect of the code/assignment is still confusing to you?**

I think I still struggle with setting up arguments when writing a function. 
