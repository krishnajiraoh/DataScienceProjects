import pickle, json
import numpy as np

__model = None
__columns = None
__locations = None


def get_locations():

    global __locations
    load_artifacts()
    
    return __locations

def load_artifacts():

    global __model
    global __columns
    global __locations

    with open("../model/model.pickle", 'rb') as f:
        __model = pickle.load(f)

    with open("../model/columns.json", 'rb') as f:
        __columns = json.load(f)['data_columns']

    __locations = __columns[3:]

def get_predicted_price(location,sqft,bath,bhk):

    load_artifacts()
    
    global __model
    global __columns

    cols = np.array(__columns)
    #location = ("location_" + location).lower()
    loc_index = np.where(cols==location)[0]

    x = np.zeros(len(cols))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1


    return int(__model.predict([x])[0])


if __name__ == "__main__" : 
    #print(get_locations())
    print(get_predicted_price("1st Phase JP Nagar", 2000, 2, 3))