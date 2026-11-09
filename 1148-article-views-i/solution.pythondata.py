import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views = views.rename(columns={'author_id':'id'})
    condition = views['id'] == views['viewer_id']
    
    return  views.loc[condition].drop_duplicates(subset = "id",keep = "first").sort_values(by = "id",ascending = True)[['id']]