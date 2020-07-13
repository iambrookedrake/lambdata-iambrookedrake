from sklearn.model_selection import train_test_split
# function to split data into train/VALIDATION/test sets
# val and test set should have same number of rows


def TrainValTest(df, target):

    train, test = train_test_split(df,
                                   train_size=0.80, test_size=0.20,
                                   random_state=42)
    train, val = train_test_split(train,
                                  train_size=0.75, test_size=0.25,
                                  random_state=43)

    features = df.columns.drop([target])
    X_train = train[features]
    y_train = train[target]
    X_val = val[features]
    y_val = val[target]
    X_test = test[features]
    y_test = test[target]

    return X_train, y_train, X_val, y_val, X_test, y_test


if __name__ == '__main__':
    df = input("Name of dataset to split: ")
    target = input("Target Columns: ")
    print(X_train, y_train, X_val, y_val, X_test, y_test)
