import pandas as pd
import matplotlib.pyplot as plt
import sys
from PyQt5 import QtWidgets


drinks=pd.read_csv('http://bit.ly/drinksbycountry')
drinks.columns=['country','beer','spirit','wine','pure_alcohol','continent']
drinks_Africa=drinks[drinks.continent=="Africa"]
drinks_Europe=drinks[drinks.continent=="Europe"]
drinks_Asia=drinks[drinks.continent=='Asia']
drinks_NA=drinks[drinks.continent=="North America"]
drinks_SA=drinks[drinks.continent=="South America"]
drinks_Oceania=drinks[drinks.continent=="Oceania"]


def get_spirit():
    
    spirit_figure=plt.figure("Spirits consumption in the world")
    spirit_figure=drinks.groupby('continent').spirit.mean().plot.pie(y=None,autopct='%1.1f%%')
    spirit_figure.set_title('spirit')
    spirit_figure.set_ylabel('')
    plt.show()

    Europe_spirit=plt.figure("Spirits consumption in Europe")
    Europe_spirit=drinks_Europe.groupby('country').spirit.mean().plot.bar()
    plt.tight_layout()
    plt.show()

    Asia_spirit=plt.figure("Spirits consumption in Asia")
    Asia_spirit=drinks_Asia.groupby('country').spirit.mean().plot.bar()
    plt.tight_layout()
    plt.show()

    NA_spirit=plt.figure("Spirits consumption in North America")
    NA_spirit=drinks_NA.groupby('country').spirit.mean().plot.bar()
    plt.tight_layout()
    plt.show()

    SA_spirit=plt.figure("Spirits consumption in South America")
    SA_spritt=drinks_SA.groupby('country').spirit.mean().plot.bar()
    plt.tight_layout()
    plt.show()

    Africa_spirit=plt.figure("Spirits consumption in Africa")
    Africa_spirit=drinks_Africa.groupby('country').spirit.mean().plot.bar()
    plt.tight_layout()
    plt.show()

    Oceania_spirit=plt.figure("Spirits consumption in Oceania")
    Oceania_spirit=drinks_Oceania.groupby('country').spirit.mean().plot.bar()
    plt.tight_layout()
    plt.show()





def get_wine():
    wine_figure=plt.figure("Wine consumption in the world")
    wine_figure=drinks.groupby('continent').wine.mean().plot.pie(y=None,autopct='%1.1f%%')
    wine_figure.set_title('Wine')
    wine_figure.set_ylabel('')
    plt.show()

    Europe_wine=plt.figure("Wine consumption in Europe")
    Europe_wine=drinks_Europe.groupby('country').wine.mean().plot.bar()
    plt.tight_layout()
    plt.show()


    Asia_wine=plt.figure("Wine consumption in Asia")
    Asia_wine=drinks_Asia.groupby('country').wine.mean().plot.bar()
    plt.tight_layout()
    plt.show()

    NA_wine=plt.figure("Wine consumption in North America")
    NA_wine=drinks_NA.groupby('country').wine.mean().plot.bar()
    plt.tight_layout()
    plt.show()

    SA_wine=plt.figure("Wine consumption in South America")
    SA_wine=drinks_SA.groupby('country').wine.mean().plot.bar()
    plt.tight_layout()
    plt.show()

    Africa_wine=plt.figure("Wine consumption in Africa")
    Africa_wine=drinks_Africa.groupby('country').wine.mean().plot.bar()
    plt.tight_layout()
    plt.show()

    Oceania_wine=plt.figure("Wine consumption in Oceania")
    Oceania_wine=drinks_Oceania.groupby('country').wine.mean().plot.bar()
    plt.tight_layout()
    plt.show()



def get_beer():

    beer_figure=plt.figure("Beer consumption in the world")
    beer_figure=drinks.groupby('continent').beer.mean().plot.pie(y=None,autopct='%1.1f%%')
    beer_figure.set_title('beer')
    beer_figure.set_ylabel('')
    plt.show()

    Europe_beer=plt.figure("Beer consumption in Europe")
    Europe_beer=drinks_Europe.groupby('country').beer.mean().plot.bar()
    plt.tight_layout()
    plt.show()


    Asia_beer=plt.figure("Beer consumption in  Asia")
    Asia_beer=drinks_Asia.groupby('country').beer.mean().plot.bar()
    plt.tight_layout()
    plt.show()

    NA_beer=plt.figure("Beer consumption in  North America")
    NA_beer=drinks_NA.groupby('country').beer.mean().plot.bar()
    plt.tight_layout()
    plt.show()

    SA_beer=plt.figure("Beer consumption in  South America")
    SA_beer=drinks_SA.groupby('country').beer.mean().plot.bar()
    plt.tight_layout()
    plt.show()

    Africa_beer=plt.figure("Beer consumption in  Africa")
    Africa_beer=drinks_Africa.groupby('country').beer.mean().plot.bar()
    plt.tight_layout()
    plt.show()

    Oceania_beer=plt.figure("Beer consumption in  Oceania")
    Oceania_beer=drinks_Oceania.groupby('country').beer.mean().plot.bar()
    plt.tight_layout()
    plt.show()



def get_pure():
    pure_figure=plt.figure("Pure alcohol consumption in the world")
    pure_figure=drinks.groupby('continent').pure_alcohol.mean().plot.pie(y=None,autopct='%1.1f%%')
    pure_figure.set_title('pure alcohol')
    pure_figure.set_ylabel('')
    plt.show()

    Europe_pure=plt.figure("Pure alcohol consumption in Europe")
    Europe_pure=drinks_Europe.groupby('country').pure_alcohol.mean().plot.bar()
    plt.tight_layout()
    plt.show()


    Asia_pure=plt.figure("Pure alcohol consumption in Asia")
    Asia_pure=drinks_Asia.groupby('country').pure_alcohol.mean().plot.bar()
    plt.tight_layout()
    plt.show()

    NA_pure=plt.figure("Pure alcohol consumption in North America")
    NA_pure=drinks_NA.groupby('country').pure_alcohol.mean().plot.bar()
    plt.tight_layout()
    plt.show()

    SA_pure=plt.figure("Pure alcohol consumption in South America")
    SA_pure=drinks_SA.groupby('country').pure_alcohol.mean().plot.bar()
    plt.tight_layout()
    plt.show()

    Africa_pure=plt.figure("Pure alcohol consumption in  Africa")
    Africa_pure=drinks_Africa.groupby('country').pure_alcohol.mean().plot.bar()
    plt.tight_layout()
    plt.show()

    Oceania_pure=plt.figure("SPure alcohol consumption in Oceania")
    Oceania_pure=drinks_Oceania.groupby('country').pure_alcohol.mean().plot.bar()
    plt.tight_layout()
    plt.show()

def get_all():
    get_spirit()
    get_beer()
    get_wine()
    get_pure()

class window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initialize()
    def initialize(self):
        
        self.get_spirit_button=QtWidgets.QPushButton("Get the statistics on spirit consumption")
        self.get_wine_button=QtWidgets.QPushButton("Get the statistics on wine consumption")
        self.get_beer_button=QtWidgets.QPushButton("Get the statistics on beer consumption")
        self.get_pure_button=QtWidgets.QPushButton("Get the statistics on pure alcohol consumption")
        self.get_all_button=QtWidgets.QPushButton("Get all statistics")

        v_box=QtWidgets.QVBoxLayout()

        v_box.addWidget(self.get_spirit_button)
        v_box.addWidget(self.get_wine_button)
        v_box.addWidget(self.get_beer_button)
        v_box.addWidget(self.get_pure_button)
        v_box.addWidget(self.get_all_button)


        
        self.setLayout(v_box)

        self.setWindowTitle("Data on alcohol consumption")


        self.get_spirit_button.clicked.connect(get_spirit)
        self.get_wine_button.clicked.connect(get_wine)
        self.get_beer_button.clicked.connect(get_beer)
        self.get_pure_button.clicked.connect(get_pure)
        self.get_all_button.clicked.connect(get_all)
        
        self.show()
        sys.exit(app.exec_()) 
app=QtWidgets.QApplication(sys.argv)
a=window()

