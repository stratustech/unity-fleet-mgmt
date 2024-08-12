import subprocess
import ansible_runner

def loginsingle():
  subprocess.run(['python3', 'loginsingle.py'])

def loginmultiple():
  subprocess.run(['python3', 'loginmultiple.py'])

def main():

    print("\n\tWelcome to Stratus ztC Edge")
    print("\n\n 1. SINGLE CLUSTER MANAGEMENT\n\n 2. MULTIPLE CLUSTERS MANAGEMENT \n\n")
    print("\n\t Enter q to EXIT \n\n")

    ch = input("Choose your options: ")
    if ch == '1':
      loginsingle()
    elif ch == '2':
      loginmultiple()
    elif ch == 'q':
      exit
    else:
      print("\nINVALID INPUT\n")
main()

