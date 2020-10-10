from .utils_colors import bcolors


def failPrint(string):
    print(
        f'{bcolors.FAIL}'
        f'{string}'
        f'{bcolors.ENDC}'
    )


def warningPrint(string):
    print(
        f'{bcolors.WARNING}'
        f'{string}'
        f'{bcolors.ENDC}'
    )


def successPrint(string):
    print(
        f'{bcolors.OKGREEN}'
        f'{string}'
        f'{bcolors.ENDC}'
    )


def boldPrint(string):
    print(
        f'{bcolors.BOLD}'
        f'{string}'
        f'{bcolors.ENDC}'
    )


def bluePrint(string):
    print(
        f'{bcolors.OKBLUE}'
        f'{string}'
        f'{bcolors.ENDC}'
    )
