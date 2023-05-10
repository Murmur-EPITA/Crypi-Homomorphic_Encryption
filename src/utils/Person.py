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
        '''
            Attributes:
                persons: list of Person instances
                rawData: Dict of every Person attributes linked to a list of self.persons' values for this attribute
                stats: Dict of Dict regrouping statistics for self.rawData
        '''
        self.persons = persons
        if self.persons != []:
            self.rawData = self.create_rawData()
            self.stats = self.compute_stats()
        else:
            self.stats = {}
            self.rawData = {}

    def create_rawData(self):
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
        data = self.rawData
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
        rawData = self.rawData
        my_rawData = [rawData['age'], rawData['education'], rawData['cigsPerDay'], rawData['BPMeds'], rawData['totChol'], rawData['sysBP'], rawData['diaBP'], rawData['BMI'], rawData['heartRate'], rawData['glucose'], rawData['TenYearCHD']]
        bp = ax.boxplot(my_rawData)

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
        ages = self.rawData['age']
        cholesterol = self.rawData['totChol']
        plt.figure(figsize=(10, 7))
        plt.hist2d(ages, cholesterol, bins=10, range=[[0, 100], [0, 500]], cmap='YlOrRd')
        plt.colorbar(label='Nombre de personnes')
        plt.title("Taux de cholestérol en fonction de l'âge")
        plt.xlabel("Âge")
        plt.ylabel("Taux de cholestérol")
        plt.show()
        return 0


    def _histogram(self, attr_to_compare: str, plot_title: str, ylabel_title: str):
        malades = self.rawData['TenYearCHD']
        attr = self.rawData[attr_to_compare]

        malades_0 = [attr[int(i)] for i, malade in enumerate(malades) if malade == 0]
        malades_1 = [attr[int(i)] for i, malade in enumerate(malades) if malade == 1]

        avg_attr_0 = np.mean(malades_0)  # Moyenne cigarettes fumées pour les non-malades
        avg_attr_1 = np.mean(malades_1)  # Moyenne cigarettes  fumées  pour les malades

        attr_all = pd.Series(attr)
        avg_attr = attr_all.mean()

        plt.figure(figsize=(10, 7))
        plt.bar([0, 1, 2], [avg_attr_0, avg_attr_1, avg_attr], color=['b', 'r', 'y'])
        plt.xticks([0, 1, 2], ['Non-malades', 'Malades', 'everybody'])
        plt.title(plot_title)
        plt.xlabel("10 year risk of coronary heart disease")
        plt.ylabel(ylabel_title)
        plt.show()
        return 0


    #diagrammes à barres cigarettes par jour
    def cig_malade_histogram(self):
        self._histogram('cigsPerDay', 'Moyenne de cigarettes fumées par jour selon la catégorie malade ou non',
                       'Moyenne de cigarettes fumées par jour')

    #diagramme à barre moyenne taux cholesterol en fonct malades, non
    def totchol_malade_histogram(self):
        self._histogram('TenYearCHD', 'Moyenne du taux de cholestérol selon la catégorie malade ou non',
                       'Moyenne du taux de cholestérol')

    #diagramme à barre moyenne age en fonct malades, non
    def age_malade_histogram(self):
        self._histogram('age', 'Moyenne des ages l selon la catégorie malade ou non',
                       'Moyenne des ages')

    #diagramme à barre moyenne taux glucose en fonct malades, non
    def glucose_malade_histogram(self):
        self._histogram('glucose', 'Moyenne du taux de glucose selon la catégorie malade ou non',
                       'Moyenne du taux de glucose')
    
    #diagramme à barre moyenne bmi en fonct malades, non
    def bmi_malade_histogram(self):
        self._histogram('BMI', 'Moyenne du taux de bmi selon la catégorie malade ou non',
                       'Moyenne du taux de bmi')

    #diagramme à barre moyenne heartRate en fonct malades, non
    def heartRate_malade_histogram(self):
        self._histogram('heartRate', 'Moyenne du taux de heartRate selon la catégorie malade ou non',
                       'Moyenne du taux de heartRate')

    #histogramme avec toutes les colonnes
    def stats_hist(self):

        rawData = self.rawData
        my_rawData = [rawData['age'], rawData['education'], rawData['cigsPerDay'], rawData['BPMeds'], rawData['totChol'], rawData['sysBP'], rawData['diaBP'], rawData['BMI'], rawData['heartRate'], rawData['glucose']]
        
        plt.figure(figsize=(12, 10))

        colonnes = ["age", "education", "cigsPerDay", "totChol", "sysBP", "diaBP", "BMI", "heartRate", "glucose"] # Liste de noms correspondant à chaque histogramme

        for i, data in enumerate(my_rawData):
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
        
