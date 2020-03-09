from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# n_estimators : k, the number of decisiontree
forest_model = RandomForestRegressor(random_state=1, n_estimators=10)
forest_model.fit(train_X, train_y)
melb_preds = forest_model.predict(val_X)
print(mean_absolute_error(val_y, melb_preds))