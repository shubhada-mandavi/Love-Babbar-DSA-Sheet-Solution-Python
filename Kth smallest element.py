{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "be4e2dc7",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Solution:\n",
    "    def kthSmallest(self,arr, l, r, k):\n",
    "        '''\n",
    "        arr : given array\n",
    "        l : starting index of the array i.e 0\n",
    "        r : ending index of the array i.e size-1\n",
    "        k : find kth smallest element and return using this function\n",
    "        '''\n",
    "        arr.sort()\n",
    "        return arr[k-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f8ead2bd",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
