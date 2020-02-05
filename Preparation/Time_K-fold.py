# The Dataset is from the "Store Item Demand Forecasting Challenge" where we are given store-item sales data, and have to predict future sales
# It's a competition with time series data. So, time K-fold cross-validation should be applied. Your goal is to create this cross-validation strategy and make sure that it works as expected.
# Note that the train DataFrame is already available in your workspace

# Import TimeSeriesSplit
# from sklearn.model_selection import TimeSeriesSplit

# Create TimeSeriesSplit object
time_kfold = TimeSeriesSplit(n_splits=3)

# Sort train data by date
train = train.sort_values('date')

# Iterate through each split
fold = 0
for train_index, test_index in ____.____(____):
    cv_train, cv_test = ____.____[____], ____.____[____]
    
    print('Fold :', fold)
    print('Train date range: from {} to {}'.format(cv_train.date.min(), cv_train.date.max()))
    print('Test date range: from {} to {}\n'.format(cv_test.date.min(), cv_test.date.max()))
    fold += 1
