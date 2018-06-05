import pandas as pd
import numpy as np

df = pd.read_csv("/Users/macbookpro/Desktop/Coxi 4. Semester/Scientific programming in Python/Programming/ScientificProgramming-egiacomazzi/pandas_exercises/Pokemon.csv")

def first_gen(df):
    '''find the names of all Pokemon from generation 1'''
    return df["Name"][df["Generation"]==1]

def highest_hp(df):
    '''find the name(s) of the Pokemon with the highest HP'''
    return df[["Name"]][df['HP'] == df["HP"].max()]

def mean_attack_by_type(df):
    '''find the mean attack power of each type (just use Type 1), result will contain just type and attack columns'''
    return df.groupby(['Type 1'], as_index=False)['Attack'].mean()

def high_defense(df):
    '''find just the Name and Defense rating of Pokemon that have an above average (>) Defense.'''
    return df[["Name","Defense"]][df["Defense"]>df["Defense"].mean()]

def deduplicated(df):
    withoutdup = df.drop_duplicates('#', keep = 'first')
    return withoutdup["Name"]


def main():
    print("Pokemon of the 1st Gen \n {} \n ---".format(first_gen(df)))
    print("Pokemon with highest HP \n {} \n ---".format(highest_hp(df)))
    print("Pokemon Type with mean of attack \n {} \n ---".format(mean_attack_by_type(df)))
    print("Pokemon with highest defense \n {} \n ---".format(high_defense(df)))
    #print('Cleaned list \n {} ---'.format(deduplicated(df)))
    print("Names of Pokemon without doubled ones \n {} ---".format(deduplicated(df)))

if __name__ == '__main__':
    main()
