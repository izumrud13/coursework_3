from utils.functions import open_file, sort_files, form_list


def main():
    files = open_file("operations.json")
    sort_file = sort_files(files)
    format_ = form_list(sort_file)
    #print(sort_file)

if __name__ == '__main__':
    main()


