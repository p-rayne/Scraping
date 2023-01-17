import os
from scraper import get_array
from convert_to_xlsx import writer


def main():
    if not os.path.exists("./var_0/images/"):
        os.mkdir("./var_0/images/")
    writer(get_array)


if __name__ == "__main__":
    main()
