import argparse

from utils import say_hello


def main():
    parser = argparse.ArgumentParser(description="Example Ruff Project CLI")
    parser.add_argument("--name", type=str, help="Your name", default="World")
    args = parser.parse_args()

    print(say_hello(args.name))


if __name__ == "__main__":
    main()
