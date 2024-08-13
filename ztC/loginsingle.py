import subprocess
import ansible_runner
import getpass

def run_playbook(playbook_path, vars):
  runner = ansible_runner.run(
    private_data_dir='.',
    playbook=playbook_path,
    extravars=vars,
  )


ip = input("Enter the System IP:\n")
username = input("Enter the Username:\n")
password = getpass.getpass("Enter the Password:\n")

print(f"\n\n\tIP Address: {ip}, Username: {username}, Password: {password}\n")
login = 'login.yaml'
vars = {
  'ip' : ip,
  'username' : username,
  'password' : password
}
run_playbook(login, vars)


def dashboard():
  subprocess.run(['python3', 'dash.py'])

def system():
  subprocess.run(['python3', 'system.py'])

def pref():
  subprocess.run(['python3', 'pref.py'])

def pref():
  subprocess.run(['python3', 'logs.py'])

def vmwf():
  subprocess.run(['python3', 'vmwf.py'])

def nwf():
  subprocess.run(['python3', 'nwf.py'])

def up():
  subprocess.run(['python3', 'up.py'])

while True:
    print("\n\tWelcome to Stratus ztC Edge")
    print("\n\n 1. DASHBOARD \n\n 2. SYSTEM \n\n 3. PREFERENCES \n\n 4. ALERTS & LOGS \n\n 5. VIRTUAL MACHINES MANAGEMENT \n\n 6. PHYSICAL MACHINES MANAGEMENT \n\n 7. LIBRARY ")
    print("\n\t Enter q to EXIT \n\n")

    ch = input("Choose your options: ")

    if ch == '1':
        subprocess.run(['python3', 'dash.py', ip, username, password])

    if ch == '2':
        subprocess.run(['python3', 'system.py', ip, username, password])

    if ch == '3':
        subprocess.run(['python3', 'pref.py', ip, username, password])

    if ch == '4':
        subprocess.run(['python3', 'logs.py', ip, username, password])

    if ch == '5':
        subprocess.run(['python3', 'vmwf.py', ip, username, password])

    if ch == '6':
        subprocess.run(['python3', 'nwf.py', ip, username, password])


    if ch == '7':
        subprocess.run(['python3', 'up.py', ip, username, password])

    if ch == 'q':
        logout = 'logout.yaml'
        run_playbook(logout, vars)
        break
