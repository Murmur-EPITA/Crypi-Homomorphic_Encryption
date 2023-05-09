from utils.Person import *

import matplotlib.pyplot as plt

complete, malades, nonmalades = PersonList.from_csv("../data/framingham_heart_disease_raw.csv")
#print(len(complete.persons), "=", len(nonmalades.persons), "+", len(malades.persons))
#print(complete.persons)

def create_tab():
    tab = []

    male_list = [person.male for person in complete.persons]
    tab.append(male_list)

    age_list = [person.age for person in complete.persons]
    tab.append(age_list)

    education_list = [person.education for person in complete.persons]
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

    totChol_list = [person.totChol for person in complete.persons]
    tab.append(totChol_list)

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

    return tab



"""""
#fonction pour les boites à moustaches
def stats_plot(tab):
    # Création de la figure et des axes
    fig, ax = plt.subplots(figsize=(10, 7))

    # Création du graphique en boîtes à moustaches
    bp = ax.boxplot(tab)

    # Ajout de l'axe des abscisses et des ordonnées
    ax.set_xlabel('Axe des abscisses')
    ax.set_ylabel('Axe des ordonnées')

    # Ajout d'une légende pour les boîtes à moustaches
    ax.legend([bp["boxes"][0]], ['Stats des ages'])

    # Ajout des valeurs du minimum, maximum, médiane et premier quartile
    for i, box in enumerate(bp['boxes']):
        # Coordonnées x et y de la boîte à moustaches
        x = i + 1
        y = box.get_ydata()[0]

        # Valeurs statistiques
        stats = {
            'Minimum': box.get_ydata()[0],
            'Premier quartile': bp['whiskers'][i*2].get_ydata()[1],
            'Médiane': box.get_ydata()[1],
            'Troisième quartile': bp['whiskers'][i*2 + 1].get_ydata()[1],
            'Maximum': box.get_ydata()[2]
        }

        # Affichage des valeurs statistiques
        for stat, value in stats.items():
            ax.text(x, value, f'{stat}: {value}', ha='center', va='bottom')

    # Affichage du graphique
    plt.show()

    return bp """""



def stats_plot(tab, labels):
    # Création de la figure et des axes
    fig, ax = plt.subplots(figsize=(10, 7))

    # Création du graphique en boîtes à moustaches
    bp = ax.boxplot(tab)

    # Ajout de l'axe des abscisses et des ordonnées
    ax.set_xlabel('Axe des abscisses')
    ax.set_ylabel('Axe des ordonnées')


    # Ajout des noms des boîtes en légende
    ax.set_xticklabels(labels)

    # Ajout d'une légende pour les boîtes à moustaches
    ax.legend([bp["boxes"][0]], ['statisques'])

    # Ajout des valeurs du minimum, maximum, médiane et premier quartile
    for i, box in enumerate(bp['boxes']):
        # Coordonnées x de la boîte à moustaches
        x = i + 1

        # Valeurs statistiques
        stats = {
            'Minimum': box.get_ydata()[0],
            'Premier quartile': bp['whiskers'][i*2].get_ydata()[1],
            'Médiane': box.get_ydata()[1],
            'Troisième quartile': bp['whiskers'][i*2 + 1].get_ydata()[1],
            'Maximum': box.get_ydata()[2]
        }

        # Affichage des valeurs statistiques
        for stat, value in stats.items():
            ax.text(x, value, f'{stat}: {value}', ha='center', va='bottom')

    # Affichage du graphique
    plt.show()

    return bp

colonnes = ["male", "age", "education", "currentSmoker", "cigsPerDay", "BPMeds", "prevalentStroke", "prevalentHyp", "diabetes", "totChol", 
                         "sysBP", "diaBP", "BMI", "heartRate", "glucose", "TenYearCHD"]

tab = create_tab()
stats_plot(tab, colonnes)