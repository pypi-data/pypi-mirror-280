from ..utils import Logger
import pandas as pd

# df to list of lists of tuples
def df_to_evaluate_list(X,y):

    df = pd.concat([X, y], axis=1)

    eval_list = []

    for index, row in df.iterrows():
        features = []
        target = row[y.columns[0]]
        for i in df.columns:
            if(i != y.columns[0]):
                features.append((i, row[i]))

        eval_list.append((features, target, 1))

    return eval_list

# read from csv to pandas dataframe and then extract and return distinct feature_value pairs 
def read_data_to_pairs(X):

    logger = Logger()

    feature_value_pairs = set()

    #print titles of the dataframe
    logger.log(X.columns, 'DEBUG')
    logger.log(X.shape, 'DEBUG')
    #print first few entries of the dataframe
    logger.log(X.head(), 'DEBUG')
    
    #extract distinct feature_value pairs
    for i in X.columns:
        for j in X[i].unique():
            feature_value_pairs.add((i,j))
            # print(i,j)

    return feature_value_pairs