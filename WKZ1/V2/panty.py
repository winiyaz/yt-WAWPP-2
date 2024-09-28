from rich.traceback import install
from src.utils.ban import banner
from src.tut.p4 import func4


install(show_locals=True)


def main():
    banner("Running p4.py - func4")
    func4()


if __name__ == "__main__":
    main()
