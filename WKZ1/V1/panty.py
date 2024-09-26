from rich.traceback import install
from src.utils.ban import banner
from src.exp.p24 import func24


install(show_locals=True)


def main():
    banner("Running Func22")
    func24()


if __name__ == "__main__":
    main()
