import matplotlib.pyplot as plt
import numpy as np
def describe_dataframe( dataframe ):
    print( "---------- Dataset describe ----------" )
    print( dataframe.describe() )
    print( "---------- Dataset info ----------" )
    print( dataframe.info() )
    print( "---------- Columns ----------" )
    print( dataframe.columns )
    print( "---------- Dtypes ----------" )
    print( dataframe.dtypes )
    print( "---------- Shape ----------" )
    print( dataframe.shape )
    print( "---------- Null values ----------" )
    print( dataframe.isna().sum() )
    # print( "---------- Correlation ----------" )
    # print( dataframe.corr() )  # Solo se i valori sono tutti numerici
    print( "---------- Moda ----------" )
    print( dataframe.mode() )

def replace_missing_values( salaries ):
    # Replace missing values for numeric features
    salaries['salary_in_usd'].fillna( salaries['salary_in_usd'].median(), inplace=True )
    # -- If the method dislay an error try this:
    # -- salaries.fillna( {'salary_in_usd': salaries['salary_in_usd'].median() }, inplace=True )

    # Replace missing values for categorical features
    salaries['job_title'].fillna( salaries['job_title'].mode()[0] )

    # Remove the rows that contains NULL values
    salaries = salaries.dropna()

    print( "---------- Null values ----------" )
    print( salaries.isna().sum() )

    return salaries

def impute_missing_values( x ):
    from sklearn.impute import SimpleImputer

    imputer = SimpleImputer(strategy='mean')
    x = imputer.fit_transform(x)

    return x

def handle_outliers( x ):
    import seaborn as sns

    # Visualize outliers
    # sns.boxplot( x )
    # plt.title("Outliers")
    # plt.show()

    q1 = np.percentile(x, 25)
    q3 = np.percentile(x, 75)

    iqr = q3 - q1

    lower_bound = q1 - ( 1.5 * iqr )
    upper_bound = q3 + ( 1.5 * iqr )

    lower_mask = x < lower_bound
    upper_mask = x > upper_bound

    x[lower_mask | upper_mask] = np.nan

    # Visualize outliers
    # sns.boxplot( x )
    # plt.title("Without outliers")
    # plt.show()

    print("---------- Null values after outliers removal ----------")
    print( x.isna().sum() )

    return x

def normalization(X_train, X_test):
    # AUTOMATIC #################################
    from sklearn.preprocessing import StandardScaler, RobustScaler

    # More robust to the outliers.
    # scaler = RobustScaler()
    # Standardize the features using StandardScaler.
    scaler = StandardScaler()

    # fit only on TRAIN data and transform on both TRAIN and TEST data
    scaler.fit(X_train)
    X_train_std = scaler.transform(X_train)
    X_test_std = scaler.transform(X_test)

    # MANUAL z-score normalization ##############
    '''
    # compute mean and standard deviation ONLY ON TRAINING SAMPLES
    mean = X_train.mean(axis=0)
    std = X_train.std(axis=0)

    # apply mean and std (standard deviation) compute on training sample to training set and to test set
    X_train_std = (X_train - mean)/std
    X_test_std = (X_test - mean)/std
    '''

    # MANUAL min-max normalization #############
    '''
    # Forces the values in the interval [a,b].
    foo[:, 1] = (v - v.min()) / (v.max() - v.min())
    X_train_std = ( (X_train - X_train.min()) / (X_train.max() - X_train.min()) ) * ( b - a ) + a
    X_test_std = ( (X_test - X_train.min()) / (X_train.max() - X_train.min()) ) * ( b - a ) + a
    '''

    return X_train_std, X_test_std


