from rich.traceback import install
from src.ban import banner
from src.p1 import func1

install(show_locals=True)


def main():
    banner("Running Func1")
    func1()


if __name__ == "__main__":
    main()
