from pathlib import Path
import pandas as pd
from skforecast.utils import load_forecaster

date_index = pd.date_range("2019-01-01", "2019-01-10", freq="D")

model_path = Path(__file__).parent.joinpath("models", "model_B1_1.pkl")
model = load_forecaster(model_path, verbose=False)
# print(model.predict(len(date_index), exog=pd.Series([0]*10, date_index)))

print(pd.Series([0]*10, date_index).info())