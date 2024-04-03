from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from skforecast.ForecasterAutoregDirect import ForecasterAutoregDirect
from skforecast.model_selection import grid_search_forecaster
from skforecast.utils import save_forecaster

data_path = Path(__file__).parent.parent.parent.joinpath("data", "dataset_prepared.csv")
data = pd.read_csv(data_path)
data["DATE"] = pd.to_datetime(data["DATE"])
data = data.set_index("DATE").asfreq("D")
data.fillna(0, inplace=True)

forecaster = ForecasterAutoregDirect(
    regressor=Ridge(random_state=123),
    steps=870,
    lags=5,
    transformer_y=StandardScaler()
)

param_grid = {'alpha': np.logspace(-5, 5, 10)}
lags_grid = [5, 12, 20]
print(len(data))

grid_search_forecaster(
    forecaster=forecaster,
    y=data['QTY_B1_1'],
    param_grid={'alpha': np.logspace(-5, 5, 10)},
    steps=870,
    metric='mean_squared_error',
    initial_train_size=len(data)//2,
    fixed_train_size=False,
    exog=data['PROMO_B1_1'],
    lags_grid=[5, 12, 20],
    refit=False,
    return_best=True,
    n_jobs='auto',
    verbose=False
)

model_path = Path(__file__).parent.joinpath("models", "model_B1_1.pkl")
save_forecaster(forecaster, model_path)
