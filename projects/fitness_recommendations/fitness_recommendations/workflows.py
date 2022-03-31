from flytekit import task, workflow
# from download_dataset import download_fitness_dataset
#
#
# @task
# def download_kaggle_fitness_dataset():
#     download_fitness_dataset()
#
#

import os.path
from kaggle.api.kaggle_api_extended import KaggleApi


@task
def download_fitness_dataset():
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_file('edoardoba/fitness-exercises-with-animations', file_name='fitness_exercises.csv')
    if os.path.isfile('fitness_exercises.csv'):
        print("Downloaded fitness exercise dataset successfully!")
    else:
        print("Fitness exercise dataset doesn't exist. Please check!")


@workflow
def main():
    download_fitness_dataset()
    # download_kaggle_fitness_dataset()


if __name__ == "__main__":
    print(f"trained model: {main()}")
