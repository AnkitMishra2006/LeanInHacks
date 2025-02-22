import pickle
import pandas as pd


def LTpredict(year, month):
    with open("./models/landTemperature.pkl", "rb") as LTfile:
        LTmodel = pickle.load(LTfile)

        future_year_df = pd.DataFrame([[year, month]], columns=['Year', 'Month'])

        prediction = LTmodel.predict(future_year_df)

        return prediction[0]

def SLpredict(year, month):
    with open("./models/seaLevel.pkl", "rb") as SLfile:
        SLmodel = pickle.load(SLfile)
        future_year_df = pd.DataFrame([[year, month]], columns=['Year', 'Month'])

        prediction = SLmodel.predict(future_year_df)

        return prediction[0]

def COpredict(year, month):
    with open("./models/co2.pkl", "rb") as COfile:
        COmodel = pickle.load(COfile)
        future_year_df = pd.DataFrame([[year, month]], columns=['year', 'Month'])

        prediction = COmodel.predict(future_year_df)

        return prediction[0]
    
def CHpredict(year, month):
    with open("./models/ch4.pkl", "rb") as CHfile:
        CHmodel = pickle.load(CHfile)
        future_year_df = pd.DataFrame([[year, month]], columns=['year', 'Month'])

        prediction = CHmodel.predict(future_year_df)

        return prediction[0]
    