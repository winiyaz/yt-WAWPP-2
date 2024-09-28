from rich.traceback import install
from src.utils.ban import banner
from src.tut.p3 import func3


install(show_locals=True)


def main():
    banner("Running Func22")
    func3()


if __name__ == "__main__":
    main()
