

import pandas as pd

def encoder_onehot(dataframe, columns_onehot):
    df_encoded = dataframe.copy()
    
    # Apply One-Hot Encoding
    df_encoded = pd.get_dummies(
        data=df_encoded,
        prefix='ohe',
        prefix_sep='_',
        columns=columns_onehot,
        drop_first=True,
        dtype='int8'
    )
    
    return df_encoded

import sys
print(sys.path)