from fastapi import FastAPI
from backend.data_processing import lunar_df, solar_df

app = FastAPI()


@app.get("/lunar/data")
def get_lunar_data():
    """Return the first 10 lunar eclipses."""
    return lunar_df.head(10).to_dict(orient="records")


@app.get("/solar/data")
def get_solar_data():
    """Return the first 10 solar eclipses."""
    return solar_df.head(10).to_dict(orient="records")