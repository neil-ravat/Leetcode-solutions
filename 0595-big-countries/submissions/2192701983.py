import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:

    condition = (world['population'] >= 25000000) | (world['area'] >= 3000000 )

    return world.loc[condition, ['name','population','area']]