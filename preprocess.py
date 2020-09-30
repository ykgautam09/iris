import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import pickle
from configparser import ConfigParser

config=ConfigParser()
config.read('./config.ini')
MODEL_PATH=config['DEFAULT']['MODEL_PATH']
DATA_PATH=config['DEFAULT']['DATA_PATH']


def generate_data():
    raw_data = pd.read_csv(DATA_PATH,
                           names=['s_length', 's_width', 'p_length', 'p_width', 'category'])
    shuffled_data = raw_data.sample(frac=1).reset_index(drop=True, inplace=True)
    x = raw_data[['s_length', 's_width', 'p_length', 'p_width']]
    y = raw_data['category']
    model = KNeighborsClassifier(n_neighbors=3, n_jobs=6)
    model.fit(x, y)
    with open(MODEL_PATH, 'wb')as f:
        pickle.dump(model, f, protocol=2)
        print('model generated')
    Y = model.predict(x)
    print(np.sum(y == Y))


if __name__ == "__main__":
    generate_data()
