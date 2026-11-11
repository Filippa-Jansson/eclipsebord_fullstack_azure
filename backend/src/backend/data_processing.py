import pandas as pd
from backend.constants import DATA_PATH

lunar_df = pd.read_csv(DATA_PATH / "lunar.csv")
solar_df = pd.read_csv(DATA_PATH / "solar.csv")

# Replace missing values (NaN) with None, since NaN is not valid in JSON
lunar_df = lunar_df.astype(object).where(pd.notnull(lunar_df), None)
solar_df = solar_df.astype(object).where(pd.notnull(solar_df), None)