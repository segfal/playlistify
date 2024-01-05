
'''
Simple way using the mean
'''
import numpy as np
from collections import Counter

def find_most(playlist):
    data = Counter(playlist)
    """
        It will look like this:
        {
            'pop': 2,
            'rock': 1,
            'jazz': 1,
            'hip-hop': 1
        }
    
    """
    return data.most_common(1)[0][1]
genres = [
    'pop',
    'rock',
    'jazz',
    'pop',
    'hip-hop',

]
find_most(genres)


