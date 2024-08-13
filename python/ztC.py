import subprocess

def dashboard():
  subprocess.run(['python3', 'dash.py'])

def system():
  subprocess.run(['python3', 'system.py'])

def pref():
  subprocess.run(['python3', 'pref.py'])


def logs():
  subprocess.run(['python3', 'logs.py'])

def vmwf():
  subprocess.run(['python3', 'vmwf.py'])

def nwf():
  subprocess.run(['python3', 'nwf.py'])

def up():
  subprocess.run(['python3', 'up.py'])

def main():


  while True:
    print("\n\tWelcome to Stratus ztC Edge")
    print("\n\n 1. DASHBOARD \n\n 2. SYSTEM \n\n 3. PREFERENCES \n\n 4. ALERTS & LOGS \n\n 5. VIRTUAL MACHINES MANAGEMENT \n\n 6. PHYSICAL MACHINES MANAGEMENT \n\n 7. LIBRARY ")
    print("\n\t Enter CTRL+C to EXIT \n\n")

    ch = input("Choose your options: ")
    if ch == '1':
      dashboard()
    elif ch == '2':
      system()
    elif ch == '3':
      pref()
    elif ch == '4':
      logs()
    elif ch == '5':
      vmwf()
    elif ch == '6':
      nwf()
    elif ch == '7':
      up()
    else:
      print("\n\nINVALID CHOICE\n\n")
main()

