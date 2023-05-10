from utils.Person import *
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

complete, malades, nonmalades = PersonList.from_csv("../data/framingham_heart_disease_raw.csv")
#print(len(complete.persons), "=", len(nonmalades.persons), "+", len(malades.persons))

""""
print("complete_cho", complete.stats['mean']['totChol'])
print("malades", malades.stats['mean']['totChol'])
print("non-malades", nonmalades.stats['mean']['totChol'])

print("complete_cig", complete.stats['mean']['cigsPerDay'])
print("malades", malades.stats['mean']['cigsPerDay'])
print("non-malades", nonmalades.stats['mean']['cigsPerDay'])
"""
print("complete_age", complete.stats['mean']['heartRate'])
print("malades", malades.stats['mean']['heartRate'])
print("non-malades", nonmalades.stats['mean']['heartRate'])

#complete.stats_plot()
#malades.stats_plot()
#nonmalades.stats_plot()

#complete.plot_cholesterol_age_histogram()
#complete.stats_hist()
#complete.totchol_malade_histogram()
#complete.cig_malade_histogram()

#complete.age_malade_histogram()
#complete.glucose_malade_histogram()
#complete.bmi_malade_histogram()
complete.heartRate_malade_histogram()