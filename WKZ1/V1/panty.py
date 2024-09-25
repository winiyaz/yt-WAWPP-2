from rich.traceback import install
from src.ban import banner
from src.p2 import func2

install(show_locals=True)


def main():
    banner("Running Func1")
    func2()


if __name__ == "__main__":
    main()
