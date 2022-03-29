from flytekit import task, workflow
from download_dataset import download_fitness_dataset


@task
def download_kaggle_fitness_dataset():
    download_fitness_dataset()


@workflow
def main():
    download_kaggle_fitness_dataset()


if __name__ == "__main__":
    print(f"trained model: {main()}")
