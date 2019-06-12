
import os, pickle
import functools

def load_or_make(creator):
    """
    Loads data that is pickled at filepath if filepath exists;
    otherwise, calls creator(*args, **kwargs) to create the data 
    and pickle it at filepath.
    Returns the data in either case.
    
    Inputs:
    - filepath: path to where data is / should be stored
    - creator: function to create data if it is not already pickled
    - *args, **kwargs: arguments passed to creator()
    
    Outputs:
    - item: the data that is stored at filepath
    
    Usage:
    @load_or_make
    def data_creator(args):
        # code
        # return data
        
    my_data = data_creator(save_file_path, *args, **kwargs)
    """
    @functools.wraps(creator)
    def cached_creator(filepath, *args, **kwargs):
        if os.path.isfile(filepath):
            with open(filepath, 'rb') as pkl:
                item = pickle.load(pkl)
        else:
            item = creator(*args, **kwargs)
            with open(filepath, 'wb') as pkl:
                pickle.dump(item, pkl)
        return item
    return cached_creator
