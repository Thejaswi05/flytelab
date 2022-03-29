import os.path
from kaggle.api.kaggle_api_extended import KaggleApi


# Downloads the kaggle dataset. To run this function, please set ENV variables
# export KAGGLE_USERNAME='' and export KAGGLE_KEY='' .
# If the values are not set kaggle API would throw a message to set those details.


def download_fitness_dataset():
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_file('edoardoba/fitness-exercises-with-animations', file_name='fitness_exercises.csv')
    if os.path.isfile('fitness_exercises.csv'):
        print("Downloaded fitness exercise dataset successfully!")
    else:
        print("Fitness exercise dataset doesn't exist. Please check!")
