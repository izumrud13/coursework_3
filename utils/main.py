from utils.functions import open_file, sort_operation, sort_files


def main():
    files = open_file("operations.json")
    new_files = sort_operation(files)
    sort_file = sort_files(new_files)
    return sort_file

if __name__ == '__main__':
    main()


