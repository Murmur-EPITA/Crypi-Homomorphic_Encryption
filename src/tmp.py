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
#complete.plot_cholesterol_age_histogram()
complete.stats_hist()


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
"""