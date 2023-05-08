from statistics import mean, stdev, median
from typing import Dict, List
import pandas as pd
from json import dumps

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
            self.stats = dumps(self.compute_stats(), indent=4)
        else:
            self.stats = {}

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
        