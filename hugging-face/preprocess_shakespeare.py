import pandas as pd
from hf_fine_tune_hello_world import dataset

df = hf_fine_tune_hello_world.dataset

df = pd.DataFrame.from_dict(df, orient='index')
