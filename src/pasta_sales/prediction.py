from pathlib import Path
import pandas as pd
from skforecast.utils import load_forecaster
from pasta_sales.create_ml_model import create_model


def predict_future_trend(brand, item):
    """Predict the future trend of the pasta sales in 870 days for a given brand and item.

     Parameters:
     brand: brand number.
     item: item number.

     Returns:
     pd.DataFrame: A rearranged DataFrame with the predicted sales for 870 days.
     """
    
    # Create the model if it does not exist
    create_model(brand, item)
    
    # Load the model and predict the future sales with and without promotion
    model_name = f"model_B{brand}_{item}.pkl"
    model_path = Path(__file__).parent.joinpath("models", model_name)
    date_index = pd.date_range("2019-01-01", periods=870, freq="D")
    model = load_forecaster(model_path, verbose=False)
    result_without_promotion = model.predict(exog=pd.Series([0]*870,
                                                            date_index))
    result_with_promotion = model.predict(exog=pd.Series([1]*870, date_index))

    # Rearrange the results into a DataFrame
    df_without_promotion = pd.DataFrame(
        {"Date": result_without_promotion.index,
         "Quantity": result_without_promotion,
         "Promotion": "Without Promotion"})
    df_with_promotion = pd.DataFrame(
        {"Date": result_with_promotion.index,
         "Quantity": result_with_promotion,
         "Promotion": "With Promotion"})
    df_result = pd.concat([df_without_promotion, df_with_promotion],
                          ignore_index=True)

    return df_result
