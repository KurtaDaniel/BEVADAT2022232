# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# %%
'''
FONTOS: Az első feladatáltal visszaadott DataFrame-et kell használni a további feladatokhoz. 
A függvényeken belül mindig készíts egy másolatot a bemenő df-ről, (new_df = df.copy() és ezzel dolgozz tovább.)
'''

# %%
'''
Készíts egy függvényt, ami egy string útvonalat vár paraméterként, és egy DataFrame ad visszatérési értékként.

Egy példa a bemenetre: 'test_data.csv'
Egy példa a kimenetre: df_data
return type: pandas.core.frame.DataFrame
függvény neve: csv_to_df
'''



# %%
def csv_to_df(input : str) -> pd.DataFrame:
    return pd.read_csv(input)


#df = csv_to_df("StudentsPerformance.csv")
#print(df)

# %%
'''
Készíts egy függvényt, ami egy DataFrame-et vár paraméterként, 
és átalakítja azoknak az oszlopoknak a nevét nagybetűsre amelyiknek neve nem tartalmaz 'e' betüt.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_capitalized
return type: pandas.core.frame.DataFrame
függvény neve: capitalize_columns
'''

# %%
def capitalize_columns(df_data : pd.DataFrame) -> pd.DataFrame:
    new_df = df_data.copy()
    upper = lambda x: x.upper() if 'e' not in x else x
    new_df.columns = (map(upper,new_df.columns))
    return new_df

#print(capitalize_columns(df))


# %%
'''
Készíts egy függvényt, ahol egy szám formájában vissza adjuk, hogy hány darab diáknak sikerült teljesíteni a matek vizsgát.
(legyen az átmenő ponthatár 50).

Egy példa a bemenetre: df_data
Egy példa a kimenetre: 5
return type: int
függvény neve: math_passed_count
'''

# %%
def math_passed_count(df_data : pd.DataFrame) -> int:
    new_df = df_data.copy()
    passed = new_df["math score"].where(lambda x : x >= 50).count()
    return passed

#print(math_passed_count(df))

# %%
'''
Készíts egy függvényt, ahol Dataframe ként vissza adjuk azoknak a diákoknak az adatait (sorokat), akik végeztek előzetes gyakorló kurzust.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_did_pre_course
return type: pandas.core.frame.DataFrame
függvény neve: did_pre_course
'''

# %%
def did_pre_course(df_data : pd.DataFrame) -> pd.DataFrame:
    new_df = df_data.copy()
    competedPreCourse = new_df.loc[np.where(new_df["test preparation course"] == "completed")]
    return competedPreCourse

#print(did_pre_course(df))

# %%
'''
Készíts egy függvényt, ahol a bemeneti Dataframet a diákok szülei végzettségi szintjei alapján csoportosításra kerül,
majd aggregációként vegyük, hogy átlagosan milyen pontszámot értek el a diákok a vizsgákon.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_average_scores
return type: pandas.core.frame.DataFrame
függvény neve: average_scores
'''

# %%
def average_scores(df_data : pd.DataFrame) -> pd.DataFrame: #nem tudom hogy pontosan ez volt e feladat de én igy értettem
    new_df = df_data.copy()
    avgscoreC = (new_df["math score"] + new_df["reading score"] + new_df["writing score"])/3
    new_df["avaragescore"] = avgscoreC
    return new_df.groupby(["parental level of education","race/ethnicity"])["avaragescore"].mean()
    
    

#print(average_scores(df))

# %%
'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'age' oszloppal, töltsük fel random 18-66 év közötti értékekkel.
A random.randint() függvényt használd, a random sorsolás legyen seedleve, ennek értéke legyen 42.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_age
return type: pandas.core.frame.DataFrame
függvény neve: add_age
'''

# %%
def add_age(df_data : pd.DataFrame) -> pd.DataFrame:
     new_df = df_data.copy()
     np.random.seed(42)
     new_df["age"] = np.random.randint(18,67,len(new_df.index))
     return new_df

#print(add_age(df))

# %%
'''
Készíts egy függvényt, ami vissza adja a legjobb teljesítményt elérő női diák pontszámait.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: (99,99,99) #math score, reading score, writing score
return type: tuple
függvény neve: female_top_score
'''

# %%
def female_top_score(df_data : pd.DataFrame) -> tuple:
    new_df = df_data.copy()
    g_df = new_df.loc[np.where(new_df["gender"] == "female")]
    avgscoreC = (g_df["math score"] + g_df["reading score"] + g_df["writing score"])/3
    g_df["avaragescore"] = avgscoreC
    g_df = g_df.sort_values("avaragescore")
    return (g_df.iloc[-1]["math score"], g_df.iloc[-1]["reading score"], g_df.iloc[-1]["writing score"])
    

#print(female_top_score(df))

# %%
'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'grade' oszloppal. 
Számoljuk ki hogy a diákok hány százalékot ((math+reading+writing)/300) értek el a vizsgán, és osztályozzuk őket az alábbi szempontok szerint:

90-100%: A
80-90%: B
70-80%: C
60-70%: D
<60%: F

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_grade
return type: pandas.core.frame.DataFrame
függvény neve: add_grade
'''

# %%
def add_grade(df_data : pd.DataFrame) -> pd.DataFrame:
    temp_df = df_data.copy()
    ret_df = df_data.copy()
    avgscoreC = (temp_df["math score"] + temp_df["reading score"] + temp_df["writing score"])/3
    temp_df["avgscoreC"] = avgscoreC
    ret_df["grade"] = pd.DataFrame(map(temp,temp_df["avgscoreC"]))
    return ret_df 
    
def temp(num : float) -> str:
    if num >= 90:
        return "A"
    elif num >= 80:
        return "B"
    elif num >= 70:
        return "C"
    elif num >= 60:
        return "D"
    else:
        return "F"
    
#print(add_grade(df))

# %%
'''
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan oszlop diagrammot,
ami vizualizálja a nemek által elért átlagos matek pontszámot.

Oszlopdiagram címe legyen: 'Average Math Score by Gender'
Az x tengely címe legyen: 'Gender'
Az y tengely címe legyen: 'Math Score'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: math_bar_plot
'''

# %%
def math_bar_plot(df_data : pd.DataFrame) -> plt.figure:
    new_df = df_data.copy()
    gender_scores = new_df.groupby('gender')['math score'].mean()

    fig, ax = plt.subplots()
    ax.bar(gender_scores.index, gender_scores.values)
    ax.set_title("Average Math Score by Gender")
    ax.set_xlabel("Gender")
    ax.set_ylabel("Math Score")
    return fig

#print(math_bar_plot(df))
#plt.show()


# %%
''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan histogramot,
ami vizualizálja az elért írásbeli pontszámokat.

A histogram címe legyen: 'Distribution of Writing Scores'
Az x tengely címe legyen: 'Writing Score'
Az y tengely címe legyen: 'Number of Students'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: writing_hist
'''

# %%
def writing_hist(df_data : pd.DataFrame) -> plt.figure:
    new_df = df_data.copy()

    fig, ax = plt.subplots()
    ax.hist(new_df["writing score"])
    ax.set_title("Distribution of Writing Scores")
    ax.set_xlabel("Writing Score")
    ax.set_ylabel("Number of Students")
    return fig

#writing_hist(df)
#plt.show()

# %%
''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan kördiagramot,
ami vizualizálja a diákok etnikum csoportok szerinti eloszlását százalékosan.

Érdemes megszámolni a diákok számát, etnikum csoportonként,majd a százalékos kirajzolást az autopct='%1.1f%%' paraméterrel megadható.
Mindegyik kör szelethez tartozzon egy címke, ami a csoport nevét tartalmazza.
A diagram címe legyen: 'Proportion of Students by Race/Ethnicity'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: ethnicity_pie_chart
'''

# %%
def ethnicity_pie_chart(df_data : pd.DataFrame) -> plt.figure:
    new_df = df_data.copy()
    a = new_df.groupby(["race/ethnicity"])["race/ethnicity"].count()
    fig, ax = plt.subplots()
    ax.pie(a.values,autopct='%1.1f%%',labels=a.keys())
    ax.set_title("Proportion of Students by Race/Ethnicity")
    return fig

#print(ethnicity_pie_chart(df))
#plt.show()


