from rich.traceback import install
from src.utils.ban import banner
from src.tut.p2 import func2


install(show_locals=True)


def main():
    banner("Running Func22")
    func2()


if __name__ == "__main__":
    main()
