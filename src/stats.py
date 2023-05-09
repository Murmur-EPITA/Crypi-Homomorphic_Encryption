from utils.Person import *
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

complete, malades, nonmalades = PersonList.from_csv("../data/framingham_heart_disease_raw.csv")
#print(len(complete.persons), "=", len(nonmalades.persons), "+", len(malades.persons))
#print(complete.persons)

#complete.stats_plot()
#malades.stats_plot()
#nonmalades.stats_plot()
complete.plot_cholesterol_age_histogram()



def create_tab():
    tab = []

    #male_list = [person.male for person in complete.persons]
    #tab.append(male_list)

    age_list = [person.age for person in complete.persons]
    tab.append(age_list)

    """education_list = [person.education for person in complete.persons]
    tab.append(education_list)

    currentSmoker_list = [person.currentSmoker for person in complete.persons]
    tab.append(currentSmoker_list)

    cigsPerDay_list = [person.cigsPerDay for person in complete.persons] 
    tab.append(cigsPerDay_list)

    BPMeds_list = [person.BPMeds for person in complete.persons] 
    tab.append(BPMeds_list)

    prevalentStroke_list = [person.prevalentStroke for person in complete.persons] 
    tab.append(prevalentStroke_list)

    prevalentHyp_list = [person. prevalentHyp  for person in complete.persons] 
    tab.append(prevalentHyp_list)

    diabetes_list = [person. diabetes for person in complete.persons] 
    tab.append(diabetes_list)
"""
    totChol_list = [person.totChol for person in complete.persons]
    tab.append(totChol_list)
    """"
    sysBP_list = [person.sysBP for person in complete.persons] 
    tab.append(sysBP_list)

    diaBP_list = [person.diaBP for person in complete.persons]
    tab.append(diaBP_list)

    BMI_list = [person.BMI for person in complete.persons]
    tab.append(BMI_list)

    heartRate_list = [person.heartRate for person in complete.persons] 
    tab.append(heartRate_list)

    glucose_list = [person.glucose for person in complete.persons] 
    tab.append(glucose_list)

    TenYearCHD_list = [person.TenYearCHD  for person in complete.persons]
    tab.append(TenYearCHD_list)
    """
    return tab



#fonction pour les histogrammes utilisées que sur des variables continues

def plot_cholesterol_age_histogram(ages, cholesterol):
    plt.figure(figsize=(10, 7))
    plt.hist2d(ages, cholesterol, bins=10, range=[[0, 100], [0, 300]], cmap='YlOrRd')
    plt.colorbar(label='Nombre de personnes')
    plt.title("Taux de cholestérol en fonction de l'âge")
    plt.xlabel("Âge")
    plt.ylabel("Taux de cholestérol")
    plt.show()

""""
def plot_histogram(data):
    plt.figure(figsize=(10, 7))
    plt.hist(data, bins=10, range=(0, 100), align="mid", rwidth=0.9, color="y", edgecolor="r")
    plt.title("Histogramme des ages")
    plt.xlabel("Valeurs des ages")
    plt.ylabel("Fréquence")
    plt.show()

tab = create_tab()
plot_histogram(tab)

def stats_hist(tab):
    plt.figure(figsize=(12, 10))

    colonnes = ["age", "education", "cigsPerDay", "totChol", "sysBP", "diaBP", "BMI", "heartRate", "glucose"] # Liste de noms correspondant à chaque histogramme

    for i, data in enumerate(tab):
        color_map = cm.get_cmap('tab10')  # Crée une nouvelle carte de couleurs pour chaque histogramme
        color = color_map(i % 10)  # Utilise un index différent pour chaque histogramme
        plt.hist(data, bins= 5, range=(0, 400), align="mid", rwidth=0.9, color=color, edgecolor="black", label=f'Boîte {i+1}')

    plt.title("Nombre de personnes par catégories")
    plt.xlabel("proportions enn dizaines")
    plt.ylabel("Nombre de personnes")
    plt.legend(colonnes)
    plt.show()

    return 0

tab = create_tab()
stats_hist(tab)"""


#fonction pour diagramme à barres utilisées pour des variables nominales ou catégorielles
""""
def stats_bar(tab):
    plt.figure(figsize=(12, 10))

    columns = ["male", "currentSmoker", "BPMeds", "prevalentStroke", "prevalentHyp", "diabetes", "TenYearCHD"]
    num_columns = len(columns)
    num_subplots = len(tab)

    bar_width = 0.8 / num_columns
    index = np.arange(num_subplots)

    color_map = plt.cm.get_cmap('tab10')

    for i, data in enumerate(tab):
        color = color_map(i / num_subplots)
        for j in range(num_columns):
            plt.bar(index[i] + (j - (num_columns // 2)) * bar_width, data[j], width=bar_width, color=color, edgecolor="black")

    plt.title("Diagramme à barres")
    plt.xlabel("Sous-tableau")
    plt.ylabel("Valeurs")
    plt.xticks(index, [])
    plt.xticks(ticks=index, labels=columns)  # Utilise set_xticks et set_xticklabels
    plt.legend(columns)  # Ajoutez des légendes si nécessaire
    plt.show()

    return 0

tab = create_tab()
stats_bar(tab)
"""