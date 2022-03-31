import numpy as np
import pandas as pd

# Step 1. Step 1: Filter the pandas dataframe based on provided values
def filter_dataframe(PARAM_BODYPARTS, PARAM_EQUIPMENT, PARAM_TARGETMUSCLES):
    new_fitness = (
        fitness_dataset.loc[
            (fitness_dataset["bodyPart"].isin(PARAM_BODYPARTS))
            & (fitness_dataset["equipment"].isin(PARAM_EQUIPMENT))
            & (fitness_dataset["target"].isin(PARAM_TARGETMUSCLES))
        ]
        .sort_values(by=["target", "equipment"])
        .copy(deep=True)
        .reset_index()
    )


new_fitness.drop(columns=["index"], inplace=True)

# Step 2: Now we need to get a random sampling
# Here we're checking out the distribution of exercises
# We want to prvoide something a bit more even spread (i.e. we don't want all abs)
new_fitness.groupby("target").size()
