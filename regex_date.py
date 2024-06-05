import re
import pyfiglet
import sys

def intro():
   print(pyfiglet.figlet_format("Conversor de Datas!"))

def inside_date():
    return input("Por favor entre com a data (mm/dd/yyyy): ") 

def change_date(date):
   return re.sub(r'(\d{1,2})\/(\d{1,2})\/(\d{4})', '\\2/\\1/\\3', date) 

def main_for_line(date=None):
    if date is None:
        date = inside_date()

    return change_date(date)

def main_for_file():
    pass

def check_date():
    pass


if __name__ == "__main__":
    intro()
    if len(sys.argv) == 1:
        main_for_line()
    else: 
        main_for_line(date=sys.argv[1])
