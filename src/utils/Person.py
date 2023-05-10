from statistics import mean, stdev, median
from typing import Dict, List
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

class Person:
    def __init__(self, male, age, education, currentSmoker, cigsPerDay,
                 BPMeds, prevalentStroke, prevalentHyp, diabetes, totChol, 
                 sysBP,diaBP,BMI,heartRate,glucose,TenYearCHD):
        self.male = male
        self.age = age
        self.education = education
        self.currentSmoker = currentSmoker
        self.cigsPerDay = cigsPerDay
        self.BPMeds = BPMeds
        self.prevalentStroke = prevalentStroke
        self.prevalentHyp = prevalentHyp
        self.diabetes = diabetes
        self.totChol = totChol
        self.sysBP = sysBP
        self.diaBP = diaBP
        self.BMI = BMI
        self.heartRate = heartRate
        self.glucose = glucose
        self.TenYearCHD = TenYearCHD
    
    def to_list(self) -> List[float]:
        return [self.male, self.age, self.education, self.currentSmoker, self.cigsPerDay,
                 self.BPMeds, self.prevalentStroke, self.prevalentHyp, self.diabetes, self.totChol, 
                 self.sysBP,self.diaBP,self.BMI,self.heartRate,self.glucose,self.TenYearCHD]

class PersonList:
    def __init__(self, persons=[]):
        self.persons = persons
        if self.persons != []:
            self.stats = self.compute_stats()
        else:
            self.stats = {}
        self.tab =  self.create_tab()

    def create_tab(self):
        return {
            'male': [person.male for person in self.persons],
            'age': [person.age for person in self.persons],
            'education': [person.education for person in self.persons],
            'currentSmoker': [person.currentSmoker for person in self.persons],
            'cigsPerDay': [person.cigsPerDay for person in self.persons],
            'BPMeds': [person.BPMeds for person in self.persons],
            'prevalentStroke': [person.prevalentStroke for person in self.persons],
            'prevalentHyp': [person.prevalentHyp  for person in self.persons],
            'diabetes': [person.diabetes for person in self.persons],
            'totChol': [person.totChol for person in self.persons],
            'sysBP': [person.sysBP for person in self.persons],
            'diaBP': [person.diaBP for person in self.persons],
            'BMI': [person.BMI for person in self.persons],
            'heartRate': [person.heartRate for person in self.persons],
            'glucose': [person.glucose for person in self.persons],
            'TenYearCHD': [person.TenYearCHD  for person in self.persons]
        }


    def to_list(self) -> List[List[float]]:
        return [person.to_list() for person in self.persons]

    def compute_stats(self) -> Dict[str, Dict[str, float]]:
        data = {
            'male': [person.male for person in self.persons],
            'age': [person.age for person in self.persons],
            'education': [person.education for person in self.persons],
            'currentSmoker': [person.currentSmoker for person in self.persons],
            'cigsPerDay': [person.cigsPerDay for person in self.persons],
            'BPMeds': [person.BPMeds for person in self.persons],
            'prevalentStroke': [person.prevalentStroke for person in self.persons],
            'prevalentHyp': [person.prevalentHyp for person in self.persons],
            'diabetes': [person.diabetes for person in self.persons],
            'totChol': [person.totChol for person in self.persons],
            'sysBP': [person.sysBP for person in self.persons],
            'diaBP': [person.diaBP for person in self.persons],
            'BMI': [person.BMI for person in self.persons],
            'heartRate': [person.heartRate for person in self.persons],
            'glucose': [person.glucose for person in self.persons],
            'TenYearCHD': [person.TenYearCHD for person in self.persons],
        }
        corr = pd.DataFrame(data).corr()
        return {
            'mean': { key: mean(val) for key, val in data.items() },
            'min': { key: min(val) for key, val in data.items() },
            'max': { key: max(val) for key, val in data.items() },
            'median': { key: median(val) for key, val in data.items() },
            'sd': { key: stdev(val) for key, val in data.items() },
            'Q1': { key: pd.DataFrame(val).quantile(0.25)[0] for key, val in data.items() },
            'Q3': { key: pd.DataFrame(val).quantile(0.75)[0] for key, val in data.items() },
            'corr': { key: corr['TenYearCHD'][key] for key in data.keys() }
        }
    
    #boites à moustaches des variables non nominales
    def stats_plot(self):
        # Création de la figure et des axes
        fig, ax = plt.subplots(figsize=(10, 7))

        # Création du graphique en boîtes à moustaches
        tab = self.tab
        my_tab = [tab['age'], tab['education'], tab['cigsPerDay'], tab['BPMeds'], tab['totChol'], tab['sysBP'], tab['diaBP'], tab['BMI'], tab['heartRate'], tab['glucose'], tab['TenYearCHD']]
        bp = ax.boxplot(my_tab)

        # Ajout de l'axe des abscisses et des ordonnées
        ax.set_xlabel('Axe des abscisses')
        ax.set_ylabel('Axe des ordonnées')

        labels =  [ "age", "education", "cigsPerDay", "BPMeds", "totChol", "sysBP", "diaBP", "BMI", "heartRate", "glucose", "TenYearCHD"]
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
    
    #histogramme du taux de cholesterole en fonction de l'age on peut en faire plusieur sortes c'est juste un exemple
    def plot_cholesterol_age_histogram(self):
        ages = self.tab['age']
        cholesterol = self.tab['totChol']
        plt.figure(figsize=(10, 7))
        plt.hist2d(ages, cholesterol, bins=10, range=[[0, 100], [0, 500]], cmap='YlOrRd')
        plt.colorbar(label='Nombre de personnes')
        plt.title("Taux de cholestérol en fonction de l'âge")
        plt.xlabel("Âge")
        plt.ylabel("Taux de cholestérol")
        plt.show()
        return 0



    #diagrammes à barres cigarettes par jour
    def cig_malade_histogram(self):
        malades = self.tab['TenYearCHD']
        cigarettes = self.tab['cigsPerDay']

        malades_0 = [self.tab['cigsPerDay'][int(i)] for i, malade in enumerate(self.tab['TenYearCHD']) if malade == 0]
        malades_1 = [self.tab['cigsPerDay'][int(i)] for i, malade in enumerate(self.tab['TenYearCHD']) if malade == 1]

        avg_cigarette_0 = np.mean(malades_0)  # Moyenne cigarettes fumées pour les non-malades
        avg_cigarette_1 = np.mean(malades_1)  # Moyenne cigarettes  fumées  pour les malades

        cig_all = pd.Series(cigarettes)
        avg_cigarette = cig_all.mean()


        plt.figure(figsize=(10, 7))
        plt.bar([0, 1, 2], [avg_cigarette_0, avg_cigarette_1, avg_cigarette], color=['b', 'r', 'y'])
        plt.xticks([0, 1, 2], ['Non-malades', 'Malades', 'everybody'])
        plt.title("Moyenne de cigarettes fumées par jour selon la catégorie malade ou non")
        plt.xlabel("10 year risk of coronary heart disease")
        plt.ylabel("Moyenne de cigarettes fumées par jour")
        plt.show()
        return 0
      

    #diagramme à barre moyenne taux cholesterol en fonct malades, non
    def totchol_malade_histogram(self):
        malades = self.tab['TenYearCHD']
        cholesterol = self.tab['totChol']

        malades_0 = [self.tab['totChol'][int(i)] for i, malade in enumerate(self.tab['TenYearCHD']) if malade == 0]

        malades_1 = [self.tab['totChol'][int(i)] for i, malade in enumerate(self.tab['TenYearCHD']) if malade == 1]

        avg_cholesterol_0 = np.mean(malades_0)  # Moyenne du taux de cholestérol pour les non-malades
        avg_cholesterol_1 = np.mean(malades_1)  # Moyenne du taux de cholestérol pour les malades

        
        cholesterol_all = pd.Series(cholesterol)
        avg_cholesterol = cholesterol_all.mean()

        plt.figure(figsize=(10, 7))
        plt.bar([0, 1, 2], [avg_cholesterol_0, avg_cholesterol_1, avg_cholesterol], color=['b', 'r', 'y'])
        plt.xticks([0, 1, 2], ['Non-malades', 'Malades', 'everybody'])
        plt.title("Moyenne du taux de cholestérol selon la catégorie malade ou non")
        plt.xlabel("10 year risk of coronary heart disease")
        plt.ylabel("Moyenne du taux de cholestérol")
        plt.show()
        return 0


    #diagramme à barre moyenne age en fonct malades, non
    def age_malade_histogram(self):
        malades = self.tab['TenYearCHD']
        age = self.tab['age']

        malades_0 = [self.tab['age'][int(i)] for i, malade in enumerate(self.tab['TenYearCHD']) if malade == 0]

        malades_1 = [self.tab['age'][int(i)] for i, malade in enumerate(self.tab['TenYearCHD']) if malade == 1]

        avg_age_0 = np.mean(malades_0)  # Moyenne du taux de cholestérol pour les non-malades
        avg_age_1 = np.mean(malades_1)  # Moyenne du taux de cholestérol pour les malades

        
        age_all = pd.Series(age)
        avg_age = age_all.mean()

        plt.figure(figsize=(10, 7))
        plt.bar([0, 1, 2], [avg_age_0, avg_age_1, avg_age], color=['b', 'r', 'y'])
        plt.xticks([0, 1, 2], ['Non-malades', 'Malades', 'everybody'])
        plt.title("Moyenne des ages l selon la catégorie malade ou non")
        plt.xlabel("10 year risk of coronary heart disease")
        plt.ylabel("Moyenne des ages")
        plt.show()
        return 0
    

    #diagramme à barre moyenne taux glucose en fonct malades, non
    def glucose_malade_histogram(self):
        malades = self.tab['TenYearCHD']
        glucose = self.tab['glucose']

        malades_0 = [self.tab['glucose'][int(i)] for i, malade in enumerate(self.tab['TenYearCHD']) if malade == 0]

        malades_1 = [self.tab['glucose'][int(i)] for i, malade in enumerate(self.tab['TenYearCHD']) if malade == 1]

        avg_glucose_0 = np.mean(malades_0)  # Moyenne du taux de cholestérol pour les non-malades
        avg_glucose_1 = np.mean(malades_1)  # Moyenne du taux de cholestérol pour les malades

        
        glucose_all = pd.Series(glucose)
        avg_glucose = glucose_all.mean()

        plt.figure(figsize=(10, 7))
        plt.bar([0, 1, 2], [avg_glucose_0, avg_glucose_1, avg_glucose], color=['b', 'r', 'y'])
        plt.xticks([0, 1, 2], ['Non-malades', 'Malades', 'everybody'])
        plt.title("Moyenne du taux de glucose selon la catégorie malade ou non")
        plt.xlabel("10 year risk of coronary heart disease")
        plt.ylabel("Moyenne du taux de glucose")
        plt.show()
        return 0
    
    #diagramme à barre moyenne bmi en fonct malades, non
    def bmi_malade_histogram(self):
        malades = self.tab['TenYearCHD']
        bmi = self.tab['BMI']

        malades_0 = [self.tab['BMI'][int(i)] for i, malade in enumerate(self.tab['TenYearCHD']) if malade == 0]

        malades_1 = [self.tab['BMI'][int(i)] for i, malade in enumerate(self.tab['TenYearCHD']) if malade == 1]

        avg_bmi_0 = np.mean(malades_0)  # Moyenne du taux de cholestérol pour les non-malades
        avg_bmi_1 = np.mean(malades_1)  # Moyenne du taux de cholestérol pour les malades

        
        bmi_all = pd.Series(bmi)
        avg_bmi= bmi_all.mean()

        plt.figure(figsize=(10, 7))
        plt.bar([0, 1, 2], [avg_bmi_0, avg_bmi_1, avg_bmi], color=['b', 'r', 'y'])
        plt.xticks([0, 1, 2], ['Non-malades', 'Malades', 'everybody'])
        plt.title("Moyenne du taux de bmi selon la catégorie malade ou non")
        plt.xlabel("10 year risk of coronary heart disease")
        plt.ylabel("Moyenne du taux de bmi")
        plt.show()
        return 0

    #diagramme à barre moyenne heartRate en fonct malades, non
    def heartRate_malade_histogram(self):
        malades = self.tab['TenYearCHD']
        heartRate = self.tab['heartRate']

        malades_0 = [self.tab['heartRate'][int(i)] for i, malade in enumerate(self.tab['TenYearCHD']) if malade == 0]

        malades_1 = [self.tab['heartRate'][int(i)] for i, malade in enumerate(self.tab['TenYearCHD']) if malade == 1]

        avg_heartRate_0 = np.mean(malades_0)  # Moyenne du taux de cholestérol pour les non-malades
        avg_heartRate_1 = np.mean(malades_1)  # Moyenne du taux de cholestérol pour les malades

        
        heartRate_all = pd.Series(heartRate)
        avg_heartRate = heartRate_all.mean()

        plt.figure(figsize=(10, 7))
        plt.bar([0, 1, 2], [avg_heartRate_0, avg_heartRate_1, avg_heartRate], color=['b', 'r', 'y'])
        plt.xticks([0, 1, 2], ['Non-malades', 'Malades', 'everybody'])
        plt.title("Moyenne du taux de heartRate selon la catégorie malade ou non")
        plt.xlabel("10 year risk of coronary heart disease")
        plt.ylabel("Moyenne du taux de heartRate")
        plt.show()
        return 0



    #histogramme avec toutes les colonnes
    def stats_hist(self):

        tab = self.tab
        my_tab = [tab['age'], tab['education'], tab['cigsPerDay'], tab['BPMeds'], tab['totChol'], tab['sysBP'], tab['diaBP'], tab['BMI'], tab['heartRate'], tab['glucose']]
        
        plt.figure(figsize=(12, 10))

        colonnes = ["age", "education", "cigsPerDay", "totChol", "sysBP", "diaBP", "BMI", "heartRate", "glucose"] # Liste de noms correspondant à chaque histogramme

        for i, data in enumerate(my_tab):
            color_map = cm.get_cmap('tab10')  # Crée une nouvelle carte de couleurs pour chaque histogramme
            color = color_map(i % 10)  # Utilise un index différent pour chaque histogramme
            plt.hist(data, bins=10, range=(0, 500), align="mid", rwidth=0.9, color=color, edgecolor="black", label=f'Boîte {i+1}')

        plt.title("Histogramme des stats")
        plt.xlabel("variables")
        plt.ylabel("Fréquence")
        plt.legend(colonnes)
        plt.show()

        return 0


    
    @classmethod
    def from_csv(cls, csvPath: str):
        '''
        Return complete list, sick people list, and healthy people list
        '''
        csv = pd.read_csv(csvPath)
        # Remove any rows with NaN values
        csv = csv.dropna()
        complete = [Person( 
                            row['male'],
                            row['age'],
                            row['education'],
                            row['currentSmoker'],
                            row['cigsPerDay'],
                            row['BPMeds'],
                            row['prevalentStroke'],
                            row['prevalentHyp'],
                            row['diabetes'],
                            row['totChol'],
                            row['sysBP'],
                            row['diaBP'],
                            row['BMI'],
                            row['heartRate'],
                            row['glucose'],
                            row['TenYearCHD'],
                        ) 
                        for _, row in csv.iterrows()]
        sick = [person for person in complete if person.TenYearCHD == 1]
        healthy = [person for person in complete if person.TenYearCHD == 0]
        return cls(complete), cls(sick), cls(healthy)
        
