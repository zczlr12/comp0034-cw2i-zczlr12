from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from skforecast.ForecasterAutoregDirect import ForecasterAutoregDirect
from skforecast.model_selection import grid_search_forecaster
from skforecast.utils import save_forecaster


def create_model(brand, item):
    """Create a machine learning model for a given brand and item, and save it
    as a pickled file.

    Args:
        brand (int): The brand number.
        item (int): The item number.
    """
    # Check if the model file exists
    path_exists = Path.exists(Path(__file__).parent.joinpath("models",
                                                             f"model_B{brand}_{brand}.pkl"))

    if not path_exists:
        # Read the data into a DataFrame
        data_path = Path(__file__).parents[2].joinpath("data",
                                                       "dataset_prepared.csv")
        data = pd.read_csv(data_path)

        # Preprocess the data
        data["DATE"] = pd.to_datetime(data["DATE"])
        data = data.set_index("DATE").asfreq("D")
        data.fillna(0, inplace=True)

        # Initialize the model
        forecaster = ForecasterAutoregDirect(
            regressor=Ridge(random_state=123),
            steps=870,
            lags=5,
            transformer_y=StandardScaler()
        )

        # Train the model
        grid_search_forecaster(
            forecaster=forecaster,
            y=data[f'QTY_B{brand}_{item}'],
            param_grid={'alpha': np.logspace(-5, 5, 10)},
            steps=870,
            metric='mean_squared_error',
            initial_train_size=len(data)//2,
            fixed_train_size=False,
            exog=data[f'PROMO_B{brand}_{item}'],
            lags_grid=[5, 12, 20],
            refit=False,
            return_best=True,
            n_jobs='auto',
            verbose=False
        )

        # Save the model as a pickled file
        save_forecaster(forecaster, path_exists)
