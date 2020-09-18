import numpy as np
import pickle
data=[5.0,3.6,1.4,0.2]

def format_input(l):
    return np.array(l).reshape(1,-1)

with open('./model.pickle', 'rb') as f:
    model=pickle.load(f)

def predict_species(y):
    print(format_input(y).shape)
    predicted_output=model.predict(format_input(y))
    return predicted_output[0] 


if __name__ == '__main__':
    print(predict_species(data))
