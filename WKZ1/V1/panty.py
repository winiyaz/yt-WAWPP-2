from rich.traceback import install
from src.utils.ban import banner
from src.exp.p22 import func22
from src.p2 import func2

install(show_locals=True)


def main():
    banner("Running Func22")
    func22()


if __name__ == "__main__":
    main()
