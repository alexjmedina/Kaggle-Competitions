# Read train data
# taxi_train = pd.read_csv('taxi_train.csv') # taxi_train rename as train
train.columns.to_list()

# Read test data
# taxi_test = pd.read_csv('taxi_test.csv') # taxi_test rename as test
test.columns.to_list()

# Shapes of train and test data
print('Train shape:', train.shape)
print('Test shape:', test.shape)

# Train head()
print(train.head())

# Describe the target variable
print(train.fare_amount.describe())

# Train distribution of passengers within rides
print(train.passenger_count.value_counts())
