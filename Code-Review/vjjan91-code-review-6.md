{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Code Review of nb-6.5 with comments on where I was stuck"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#1. I was stuck  in running `calculate_statistics` on the `filter_maf_missing` function that I had created"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Below, one can see the original function and the error:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "def calculate_statistics(self):\n",
    "        nd = np.var(self.arr == self.arr[0], axis=0).mean() # This function calculates the variance along the mentioned axis and it's mean is then taken\n",
    "        mf = np.mean(np.sum(self.arr != self.arr[0], axis=0) / self.arr.shape[0]) # The mean minor allele frequency is calculated by taking the mean of the frequency of elements that are not the same as the first row\n",
    "        inv = np.any(self.arr != self.arr[0], axis=0).sum() # The sum of all elements that are not the same as the first row\n",
    "        var = self.arr.shape[1] - inv # A variable that subtracts the inv from the total lenght of all rows\n",
    "        return pd.Series(\n",
    "            {\"mean nucleotide diversity\": nd,\n",
    "             \"mean minor allele frequency\": mf,\n",
    "             \"invariant sites\": inv,\n",
    "             \"variable sites\": var,\n",
    "            })"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# calculate statistics for an array after filtering it in one shot\n",
    "seqs.calculate_statistics(seqs.filter_maf_missing(0.1, 0.0))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The above function gave an error suggesting that it cannot run on a numpy array. This was corrected by running the below lines of code:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "   def calculate_statistics(self, arr): # By adding an array argument, the above function ran perfectly\n",
    "        nd = np.var(arr == arr[0], axis=0).mean() # This function calculates the variance along the mentioned axis and it's mean is then taken\n",
    "        mf = np.mean(np.sum(arr != arr[0], axis=0) / arr.shape[0]) # The mean minor allele frequency is calculated by taking the mean of the frequency of elements that are not the same as the first row\n",
    "        inv = np.any(arr != arr[0], axis=0).sum() # The sum of all elements that are not the same as the first row\n",
    "        var = arr.shape[1] - inv # A variable that subtracts the inv from the total lenght of all rows\n",
    "        return pd.Series(\n",
    "            {\"mean nucleotide diversity\": nd,\n",
    "             \"mean minor allele frequency\": mf,\n",
    "             \"invariant sites\": inv,\n",
    "             \"variable sites\": var,\n",
    "            })"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#2. The above changes were made after seeing the modified code posted by Eaton Lab.\n",
    "#3. This assignment dived into class objects in detail. However, I am still confused after reading the modified code that was posted on the Eaton Lab assignment. \n",
    "#4. I am still extremely confused about where to use `self` and where you define `__init`, even within the private functions. It would be very helpful if we can run through the code in class on Monday. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
