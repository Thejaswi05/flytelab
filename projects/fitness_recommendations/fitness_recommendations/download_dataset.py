import os.path
from kaggle.api.kaggle_api_extended import KaggleApi


def get_dataset():
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_file('edoardoba/fitness-exercises-with-animations', file_name='fitness_exercises.csv')
    if os.path.isfile('fitness_exercises.csv'):
        print("Downloaded fitness exercise dataset successfully!")
    else:
        print("Fitness exercise dataset doesn't exist. Please check!")


get_dataset();
