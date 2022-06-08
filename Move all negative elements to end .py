{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cd91ab52",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Solution:\n",
    "    def segregateElements(self, arr, n):\n",
    "        neg = []\n",
    "        pos = []\n",
    "        \n",
    "        for i in arr:\n",
    "            if (i < 0):\n",
    "                neg.append(i)\n",
    "            else:\n",
    "                pos.append(i)\n",
    "                \n",
    "        j = 0\n",
    "        for i in pos+neg:\n",
    "            arr[j] = i\n",
    "            j+=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2bf72c8b",
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
