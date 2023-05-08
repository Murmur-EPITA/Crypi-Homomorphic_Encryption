import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#pour charger le fichier csv
def load_data(filename):
    # Charger le fichier CSV dans un DataFrame pandas
    dataframe = pd.read_csv(filename)

    #rename the columns
    dataframe.columns = ["male", "age", "education", "currentSmoker", "cigsPerDay", "BPMeds", "prevalentStroke", "prevalentHyp", "diabetes", "totChol", 
                         "sysBP", "diaBP", "BMI", "heartRate", "glucose", "TenYearCHD"]

    # Convertir le DataFrame en un tableau NumPy
    #tableau_donnees = dataframe.to_numpy()

    #display 5 rows of dataset
    dataframe.head()

    return dataframe


#fonction pour les moyennes
def stats_mean(tab):
    mean_male = tab.male.mean()
    print(mean_male)
    
    mean_age = tab.age.mean()
    print(mean_age)
    
    mean_education = tab.education.mean()

    mean_cigsperday = tab.cigsPerDay.mean()
    print(mean_cigsperday)
    
    mean_currentsmoker = tab.currentSmoker.mean()
    print(mean_currentsmoker)

    mean_bpmeds = tab.BPMeds.mean()
    print(mean_bpmeds)

    mean_prevalentstroke = tab.prevalentStroke.mean()
    print(mean_prevalentstroke)
    
    mean_prevalenthyp = tab.prevalentHyp.mean()
    print(mean_prevalenthyp)
    mean_diabetes = tab.diabetes.mean()
    print(mean_diabetes)

    mean_totchol = tab.totChol.mean()
    print(mean_totchol)

    mean_sysbp = tab.sysBP.mean()
    print(mean_sysbp)

    mean_diabp = tab.diaBP.mean()
    print(mean_diabp)

    mean_bmi = tab.BMI.mean()
    print(mean_bmi)

    mean_heartrate = tab.heartRate.mean()
    print(mean_heartrate)

    mean_glucose = tab.glucose.mean()
    print(mean_glucose)
    
    mean_tenyearchd = tab.TenYearCHD.mean()
    print(mean_tenyearchd)

    #calcul de l'écart-type
    #np.std(tab.cigsPerDay)

    return 0


#fonction pour les boites à moustaches
def stats_plot(tab):

    #juste pour definir les dimensions de la figure
    fig = plt.figure(figsize =(10, 7))
 
    # Creating axes instance -> indique que les axes occuperont toute la figure.
    ax = fig.add_axes([0, 0, 1, 1])
 
    # Creating plot
    bp = ax.boxplot(tab)
    """bp = ax.boxplot(tab.age)
    bp = ax.boxplot(tab.male)
    bp = ax.boxplot(tab.education)

    bp = ax.boxplot(tab.currentSmoker)
    bp = ax.boxplot(tab.cigsPerDay)

    bp = ax.boxplot(tab.BPMeds)
    bp = ax.boxplot(tab.prevalentStroke)
    bp = ax.boxplot(tab.prevalentHyp)
    bp = ax.boxplot(tab.diabetes)

    bp = ax.boxplot(tab.totChol)
    bp = ax.boxplot(tab.sysBP)
    bp = ax.boxplot(tab.diaBP)
    bp = ax.boxplot(tab.BMI)
    bp = ax.boxplot(tab.heartRate)
    bp = ax.boxplot(tab.glucose)

    bp = ax.boxplot(tab.TenYearCHD)
"""
    # show plot
    plt.show()

    return bp


#fonction pour les histogrammes utilisées que sur des variables continues
def stats_hist(tab):

    plt.figure(figsize=(12,10))
    plt.hist(tab.age,bins=10,range=(0,100),align="mid",rwidth=0.9,color="y",edgecolor="r",label="age")
    plt.title("Nombre de personnes dont l'age est compris dans une decennie")
    plt.xlabel("age par decennie")
    plt.ylabel("Nbre de personnes")
    plt.legend()
    plt.show()

    return 0


#fonction pour diagramme à barres utilisées pour des variables nominales ou catégorielles
def stats_diag(tab):

    """nominal = tab["male"]
    nominal.append(tab["currentSmoker"])
    nominal.append(tab["BPMeds"])
    nominal.append(tab["prevalentStroke"]) 
    nominal.append(tab["prevalentHyp"]) 	
    nominal.append(tab["diabetes"])
    nominal.append(tab["TenYearCHD"]) """

    columns = ["male", "currentSmoker", "BPMeds", "prevalentStroke", "prevalentHyp", "TenYearCHD"]

    nominal = tab[columns]

    counts = nominal.sum().tolist()

    plt.barh(columns, counts)

    #plt.bar(columns, counts)
    plt.show()
    return 0


donnees = load_data("../data/data.csv")
stats_mean(donnees)

print(stats_mean(donnees))
stats_plot(donnees)
stats_hist(donnees)
stats_diag(donnees)
