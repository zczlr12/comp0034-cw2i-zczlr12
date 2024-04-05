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
        brand_num (int): The brand number.
        item_num (int): The item number.
    """

    # Read the data into a DataFrame
    data_path = Path(__file__).parents[2].joinpath("data", "dataset_prepared.csv")
    data = pd.read_csv(data_path)

    # Generate the quantity and promotion columns
    quantity = f"QTY_B{brand}_{item}"
    promotion = f"PROMO_B{brand}_{item}"
    column_names = data.columns

    # Check if the model file exists
    model_path = Path(__file__).parent.joinpath("models",
                                                f"model_B{brand}_{item}.pkl")
    print(model_path.as_posix())
    path_exists = model_path.is_file()
    
    # check whether the item is valid
    if quantity not in column_names or promotion not in column_names:
        raise ValueError("Invalid value for brand number or item number.")

    if not path_exists:

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
            y=data[quantity],
            param_grid={'alpha': np.logspace(-5, 5, 10)},
            steps=870,
            metric='mean_squared_error',
            initial_train_size=len(data)//2,
            fixed_train_size=False,
            exog=data[promotion],
            lags_grid=[5, 12, 20],
            refit=False,
            return_best=True,
            n_jobs='auto',
            verbose=False
        )

        # Save the model as a pickled file
        save_forecaster(forecaster, model_path)
