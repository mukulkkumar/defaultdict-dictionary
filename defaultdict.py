{
 "nbformat": 4,
 "nbformat_minor": 2,
 "metadata": {
  "language_info": {
   "name": "python",
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   }
  },
  "orig_nbformat": 2,
  "file_extension": ".py",
  "mimetype": "text/x-python",
  "name": "python",
  "npconvert_exporter": "python",
  "pygments_lexer": "ipython2",
  "version": 2
 },
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from collections import defaultdict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "counts = {}\n",
    "sentence = \"able was I ere I saw elba\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "# first approach for getting the counts of letter in the sentence\n",
    "for c in sentence:\n",
    "    if c in counts:\n",
    "        counts[c]+=1\n",
    "    else:\n",
    "        counts[c]=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": "{'a': 4, 'b': 2, 'l': 2, 'e': 4, ' ': 6, 'w': 2, 's': 2, 'I': 2, 'r': 1}"
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "counts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "# second approach for getting the counts of letter in the sentence\n",
    "counts = {}\n",
    "for c in sentence:\n",
    "    counts[c] = counts.get(c, 0)+1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": "{'a': 4, 'b': 2, 'l': 2, 'e': 4, ' ': 6, 'w': 2, 's': 2, 'I': 2, 'r': 1}"
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "counts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "# third approac for getting the counts of letter in the sentence\n",
    "counts = defaultdict(lambda:0)\n",
    "for c in sentence:\n",
    "    counts[c]+=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": "defaultdict(<function __main__.<lambda>()>,\n            {'a': 4,\n             'b': 2,\n             'l': 2,\n             'e': 4,\n             ' ': 6,\n             'w': 2,\n             's': 2,\n             'I': 2,\n             'r': 1})"
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "counts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ]
}