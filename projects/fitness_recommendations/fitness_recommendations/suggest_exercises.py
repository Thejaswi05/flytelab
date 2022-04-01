import numpy as np
import pandas as pd

# Step 1. Step 1: Filter the pandas dataframe based on provided values

def filter_dataset(fitness_dataset, PARAM_BODYPARTS, PARAM_EQUIPMENT, PARAM_TARGETMUSCLES):
    new_fitness = (fitness_dataset.loc[ \
            (fitness_dataset["bodyPart"].isin(PARAM_BODYPARTS)) \ 
            & (fitness_dataset["equipment"].isin(PARAM_EQUIPMENT)) \
            & (fitness_dataset["target"].isin(PARAM_TARGETMUSCLES)) \
        ].sort_values(by=["target", "equipment"]) \
        .copy(deep=True) \
        .reset_index())

    new_fitness.drop(columns=["index"], inplace=True)

    return new_fitness



# Step 2: Now we need to get a random sampling
# Here we're checking out the distribution of exercises
# We want to prvoide something a bit more even spread (i.e. we don't want all abs)
def randomize_selection(new_fitness, PARAM_EXERCISES):
    # Here we will grab the sampling number by trget muscle group
    sampling_num = int(round((PARAM_EXERCISES/len(new_fitness.target.unique()))))

    # we also want to make sure we get the remainder so we don't short-change
    remainder = PARAM_EXERCISES % sampling_num

    # We sample by group
    # new_fitness.groupby("target").sample(n=sampling_num,random_state=42)
    # We sample the rows for the remainder number
    #new_fitness.sample(n=remainder,random_state=42)
    # Then we combine into a final table

    suggested_exercises = pd.concat(new_fitness.groupby("target").sample(n=sampling_num,random_state=42), new_fitness.sample(n=remainder,random_state=42))
    
    return suggested_exercises

