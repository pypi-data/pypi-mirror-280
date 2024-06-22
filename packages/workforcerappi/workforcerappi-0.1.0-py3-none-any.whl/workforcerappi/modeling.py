import xgboost as xgb
from sklearn.metrics import mean_squared_error
import numpy as np

def train_xgboost_model(X_train, y_train, X_test, y_test):
    """
    Train an XGBoost regression model.

    Args:
    - X_train (pd.DataFrame): Features of the training set.
    - y_train (pd.Series): Target variable of the training set.
    - X_test (pd.DataFrame): Features of the test set.
    - y_test (pd.Series): Target variable of the test set.

    Returns:
    - xgb.XGBRegressor: Trained XGBoost model.
    """
    reg = xgb.XGBRegressor(base_score=0.5, booster='gbtree',
                           n_estimators=1000,
                           early_stopping_rounds=50,
                           objective='reg:linear',
                           max_depth=3,
                           learning_rate=0.01)
    reg.fit(X_train, y_train,
            eval_set=[(X_train, y_train), (X_test, y_test)],
            verbose=100)
    return reg
    

def make_predictions(model, X_test):
    """
    Make predictions using a trained XGBoost model.

    Args:
    - model (xgb.XGBRegressor): Trained XGBoost model.
    - X_test (pd.DataFrame): Features of the test set.

    Returns:
    - np.array: Predicted values.
    """
    return model.predict(X_test)


def make_future_predictions(model, future_data, FEATURES):
    future_predictions = model.predict(future_data[FEATURES])
    future_data['prediction'] = future_predictions
    return future_data


def calculate_rmse(y_true, y_pred):
    """
    Calculate the root mean squared error (RMSE).

    Args:
    - y_true (pd.Series): True target values.
    - y_pred (np.array): Predicted values.

    Returns:
    - float: RMSE value.
    """
    return np.sqrt(mean_squared_error(y_true, y_pred))


