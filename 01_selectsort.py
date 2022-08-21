import sys

def print_help():
    print("This is a help message")
    print("Use program with just one argument: filename to sort")
    print("Example:")
    print("01_selectsort.py sort_this_file.txt > out.txt")
    print("It will sort content of file sort_this_file.txt and place result in the out.txt")
    print("So... Good Luck!")

def arguments_validation():
    if len(sys.argv) != 2:
        return False
    else:
        return True
        
def check_file(filename_to_check):
    try:
        f = open(filename_to_check, "r")
        f.close()
        return True
    except:
        return False
        
def read_file_into_list(filename):
    try:
        f = open(filename, "r")
        result = [str for str in f]
        return result
    except Exception:
        print("Fatal error with code 0001")
        exit()
    

if __name__ == "__main__":
    print("01_selectsort")
    if not arguments_validation():
        print_help()
        exit()
    if not check_file(sys.argv[1]):
        print_help()
        exit()
    
    lst = read_file_into_list(sys.argv[1])
    print(lst)