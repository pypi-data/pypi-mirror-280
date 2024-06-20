from .assets_utils import get_asset_properties

import re
def get_trailing_number(s):
    m = re.search(r'\d+$', s)
    return int(m.group()) if m else None

class Dataset:
    def __init__(self, name=None, description=None, mode=None, columns_type=None, data_type=None):
        self.name = name
        self.description = description
        self.columns_type = columns_type
        self.data_type = data_type
        self.info = get_asset_properties(name)
        
        self.index = str(get_trailing_number(name)) if get_trailing_number(name) is not None else "" 
        
        assert mode=="batch" or mode=="streaming"
        self.mode = mode
        

