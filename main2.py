import sys


def hello(name: str) -> None:
    'For test with param'
    print(f'Hello Jenkins!\nNice to see you {name}!')


if __name__ == '__main__':
   hello(sys.argv[1])
