from utils.functions import open_file, sort_files


def main():
    files = open_file("operations.json")
    sort_file = sort_files(files)
    print(sort_file)

if __name__ == '__main__':
    main()


