from utils.Person import *
import pandas as pd
import matplotlib.pyplot as plt


def diag(path):

    tab = pd.read_csv(path, header=None).values.tolist()
    tab1 = tab[0]

    complete, _, _ = PersonList.from_csv("../data/framingham_heart_disease_raw.csv")
    non_encrypt_tab = [value for value in complete.stats['mean'].values()]

    my_final_list = [elem for pair in zip(tab1, non_encrypt_tab) for elem in pair]

    print(len(my_final_list)) 

    colors = ['b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r',
               'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r']
    plt.bar(range(len(my_final_list)), my_final_list, color=colors[:len(my_final_list)])
    plt.xticks(range(len(my_final_list)), ['male', 'male_c', 'age', 'age_c', 'education', 'education_c', 'currentSmoker', 'currentSmoker_c',
                                           'cigsPerDay', 'cigsPerDay_c', 'BPMeds', 'BPMeds_c', 'prevalentStroke', 'prevalentStroke_c', 'prevalentHyp', 'prevalentHyp_c',
                                           'diabetes', 'diabetes_c', 'totChol', 'totChol_c', 'sysBP', 'sysBP_c', 'diaBP', 'diaBP_c',
                                           'BMI', 'BMI_c', 'heartRate', 'heartRate_c', 'glucose', 'glucose_c', 'TenYearCHD', 'TenYearCHD_c'])
    
                                                                             
    #plt.xlim([-4.5, 4.5])
    plt.xlabel("Comparaison entre les moyennes chiffrées et non-chiffrées")
    plt.ylabel("Moyenne")
    plt.show()



def diag2(path):

    tab = pd.read_csv(path, header=None).values.tolist()
    tab1 = tab[0]

    complete, _, _ = PersonList.from_csv("../data/framingham_heart_disease_raw.csv")
    to_keep = ['age', 'cigsPerDay', 'totChol', 'sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose']
    non_encrypt_tab = [val for key, val in complete.stats['mean'].items() if key in to_keep]

    tab_dict = dict(zip(complete.stats['mean'].keys(), tab1))
    tab1 = [val for key, val in tab_dict.items() if key in to_keep]
    tab_dict = {k + "_c": v for k, v in tab_dict.items()}

    my_final_list = [elem for pair in zip(tab1, non_encrypt_tab) for elem in pair]

    [print(f"{k[0]:<16}: {round(k[1],13):>20},{round(v[1],13):>20} | diff={max(k[1], v[1]) - min(k[1], v[1])}\n") for k, v in zip(complete.stats['mean'].items(), tab_dict.items())]

    colors = ['b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r']
    plt.bar(range(len(my_final_list)), my_final_list, color=colors[:len(my_final_list)])
    plt.xticks(range(len(my_final_list)), ['age', 'age_c', 'cigsPerDay', 'cigsPerDay_c', 'totChol', 'totChol_c', 'sysBP', 'sysBP_c', 'diaBP', 'diaBP_c', 
                                           'BMI', 'BMI_c', 'heartRate', 'heartRate_c', 'glucose', 'glucose_c'])
                                                                             
    plt.xlabel("Comparaison entre les moyennes chiffrées et non-chiffrées")
    plt.ylabel("Moyenne")
    plt.show()

diag2("decrypted_results.csv")