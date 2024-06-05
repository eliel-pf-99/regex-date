import re
import pyfiglet
import sys, os
import colorama

def intro():
   print(colorama.Fore.BLUE, pyfiglet.figlet_format("Conversor de Datas!"))

####### Core #######

def check_date(date):
    day = "(3[01]|[12][0-9]|0?[1-9])"
    month = "(1[0-2]|0?[1-9])"
    year = "(([0-9]{2})?[0-9]{2})"
    break_date = r"(\/|-|.)"
    pattern = '^' + month + break_date + day + break_date + year + '$'
    return len(re.findall(pattern, date)) > 0

def format_date(date):
    return re.sub(r'(\.|-|\|/)', r'/', date)

def change_date(date):
   return re.sub(r'(\d{1,2})\/(\d{1,2})\/(\d{2,4})', '\\2/\\1/\\3', date)

####### Command-line #######

def main_for_line(date=None):
    if date is None:
        date = inside_date()
    print(change_date(date))

def inside_date():
    date = input("Por favor entre com a data (mm/dd/yyyy): ") 
    if check_date(date):
        return date
    else:
        error(date)
        return inside_date()
    
####### Text-file #######

def check_file(file):
    return os.path.isfile(file)

def read_from_file(file):
    content = ""
    with open(file) as f:
        content = f.read()
    return content

def convert_file(content):
    contents = content.split(' ')
    for x in range(len(contents)):
        contents[x] = check_date(contents[x]) if format_date(contents[x]) else contents[x]
    return change_date(content)

def save_in_the_file(content, file):
    with open(file, 'w') as f:
        f.write(content)
    return 

def main_for_file(file):
    content = read_from_file(file)
    processed = convert_file(content)
    save_in_the_file(processed, file)
    print(colorama.Fore.GREEN, "arquivo pronto!")

####### Main and error #######

def main(date):
    if check_date(date):
        main_for_line(format_date(date))
    elif check_file(date):
        main_for_file(date)
    else:
        error(date)

def error(date):
    print(colorama.Fore.RED, f"O nome do arquivo ou a data são inválidas. {date}")

if __name__ == "__main__":
    intro()
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main_for_line()
    
