import pickle
import json
import numpy as np
import config


class MPG():
    def __init__(self, Cylinders,Displacement,Horsepower,Weight,Acceleration,Model_Year,Origin):
        print("** INIT Function ***")
        self.Cylinders = Cylinders
        self.Displacement = Displacement
        self.Horsepower = Horsepower
        self.Weight = Weight
        self.Acceleration = Acceleration
        self.Model_Year=Model_Year
        self.Origin = Origin

    def __load_saved_data(self):

        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)

    def get_predicted_mpg(self):
        self.__load_saved_data()

        Origin = 'Origin_'+ self.Origin

        mpg_index = self.json_data["Column Names"].index(Origin)

        test_array = np.zeros([1,self.model.n_features_in_])
        test_array[0,0] = self.Cylinders
        test_array[0,1] = self.Displacement
        test_array[0,2] = self.Horsepower
        test_array[0,3] = self.Weight
        test_array[0,4] = self.Acceleration
        test_array[0,5] = self.Model_Year
        test_array[0,mpg_index] = 1

        predicted_mpg = np.around(self.model.predict(test_array)[0],1)
        return predicted_mpg