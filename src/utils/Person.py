from statistics import mean, stdev, median
from typing import Dict
import pandas as pd

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

class PersonList:
    def __init__(self, persons=[]):
        self.persons = persons
        if self.persons != []:
            self.persons = self.compute_stats()
        else:
            self.stats = {}

    # Dict[nom_colonne, Dict[moyenne, ecart-type, mediane]]
    def compute_stats(self) -> Dict[str, Dict[float, float, float]]:
        maleList = [person.male for person in self.persons]
        ageList = [person.age for person in self.persons]
        educationList = [person.education for person in self.persons]
        currentSmokerList = [person.currentSmoker for person in self.persons]
        cigsPerDayList = [person.cigsPerDay for person in self.persons]
        BPMedsList = [person.BPMeds for person in self.persons]
        prevalentStrokeList = [person.prevalentStroke for person in self.persons]
        prevalentHypList = [person.prevalentHyp for person in self.persons]
        diabetesList = [person.diabetes for person in self.persons]
        totCholList = [person.totChol for person in self.persons]
        sysBPList = [person.sysBP for person in self.persons]
        diaBPList = [person.diaBP for person in self.persons]
        BMIList = [person.BMI for person in self.persons]
        heartRateList = [person.heartRate for person in self.persons]
        glucoseList = [person.glucose for person in self.persons]
        tenYearCHDList = [person.TenYearCHD for person in self.persons]
        return {
            'means': {
                'male': mean(maleList),
                'age': mean(ageList),
                'education': mean(educationList),
                'currentSmoker': mean(currentSmokerList),
                'cigsPerDay': mean(cigsPerDayList),
                'BPMeds': mean(BPMedsList),
                'prevalentStroke': mean(prevalentStrokeList),
                'prevalentHyp': mean(prevalentHypList),
                'diabetes': mean(diabetesList),
                'totChol': mean(totCholList),
                'sysBP': mean(sysBPList),
                'diaBP': mean(diaBPList),
                'BMI': mean(BMIList),
                'heartRate': mean(heartRateList),
                'glucose': mean(glucoseList),
                'TenYearCHD': mean(tenYearCHDList),
                },
            'sd': {
                'male': stdev(maleList),
                'age': stdev(ageList),
                'education': stdev(educationList),
                'currentSmoker': stdev(currentSmokerList),
                'cigsPerDay': stdev(cigsPerDayList),
                'BPMeds': stdev(BPMedsList),
                'prevalentStroke': stdev(prevalentStrokeList),
                'prevalentHyp': stdev(prevalentHypList),
                'diabetes': stdev(diabetesList),
                'totChol': stdev(totCholList),
                'sysBP': stdev(sysBPList),
                'diaBP': stdev(diaBPList),
                'BMI': stdev(BMIList),
                'heartRate': stdev(heartRateList),
                'glucose': stdev(glucoseList),
                'TenYearCHD': stdev(tenYearCHDList),
                },
            'median': {
                'male': median(maleList),
                'age': median(ageList),
                'education': median(educationList),
                'currentSmoker': median(currentSmokerList),
                'cigsPerDay': median(cigsPerDayList),
                'BPMeds': median(BPMedsList),
                'prevalentStroke': median(prevalentStrokeList),
                'prevalentHyp': median(prevalentHypList),
                'diabetes': median(diabetesList),
                'totChol': median(totCholList),
                'sysBP': median(sysBPList),
                'diaBP': median(diaBPList),
                'BMI': median(BMIList),
                'heartRate': median(heartRateList),
                'glucose': median(glucoseList),
                'TenYearCHD': median(tenYearCHDList),
                }
        }

    
    @classmethod
    def from_csv(cls, csvPath: str):
        csv = pd.read_csv(csvPath)
        persons = [Person( 
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
                        for index, row in csv.iterrows()]
        return cls(persons)
        