import matplotlib.pyplot as plt
import io
import base64
import pandas as pd

def LTplot(year):

    df = pd.read_csv("data/GlobalTemperatures.csv")

    df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(DAY=1))
    df_year = df[df['Year'] == year]


    if df_year.empty:
        print(f"No data available for the year {year}")
        return


    df_year = df_year.sort_values(by='Date')


    plt.figure(figsize=(10, 5))
    plt.plot(df_year['Date'], df_year['Anomaly'], marker='o', linestyle='-', color='r', label=f"{year} Land Temperature Anomaly")


    plt.xlabel('YYYY-MM')
    plt.ylabel('Land Temperature Anomaly')
    plt.title(f'Land Temperature Anomaly in {year}')


    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()


    img = io.BytesIO()
    plt.savefig(img, format='png',bbox_inches='tight')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return plot_url


# user_year = int(input("Enter the year to plot: "))
# print(LTplot(user_year))




def SLplot(year):

    df = pd.read_csv("data/SeaLevel.csv")

    df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(DAY=1))
    df_year = df[df['Year'] == year]


    if df_year.empty:
        print(f"No data available for the year {year}")
        return


    df_year = df_year.sort_values(by='Date')


    plt.figure(figsize=(10, 5))
    plt.plot(df_year['Date'], df_year['GMSL'], marker='o', linestyle='-', color='r', label=f"{year} Global Mean Sea Level")


    plt.xlabel('YYYY-MM')
    plt.ylabel('Sea Level (mm)')
    plt.title(f'Global Mean Sea Level')


    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()

    img = io.BytesIO()
    plt.savefig(img, format='png',bbox_inches='tight')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return plot_url
    




def COplot(year):

    df = pd.read_csv("data/CO2.csv")

    df['Date'] = pd.to_datetime(df[['year', 'month']].assign(DAY=1))
    df_year = df[df['year'] == year]


    if df_year.empty:
        print(f"No data available for the year {year}")
        return


    df_year = df_year.sort_values(by='Date')


    plt.figure(figsize=(10, 5))
    plt.plot(df_year['Date'], df_year['average'], marker='o', linestyle='-', color='r', label=f"{year} Carbon Dioxide Level")


    plt.xlabel('YYYY-MM')
    plt.ylabel('CO2 Level (ppm)')
    plt.title(f'Carbon Dioxide Level')


    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()

    img = io.BytesIO()
    plt.savefig(img, format='png',bbox_inches='tight')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return plot_url
    
