import subprocess
import ansible_runner
import getpass

def run_playbook(playbook_path, vars):
  runner = ansible_runner.run(
    private_data_dir='.',
    playbook=playbook_path,
    extravars=vars,
  )

def fetch_credentials(file_path):
  credentials = []

  with open(file_path, 'r') as file:
    for line in file:
      ip,username,password = line.strip().split(':')
      credentials.append((ip, username, password))

  return credentials

file_path = input("Enter Credentials file: ")
credentials = fetch_credentials(file_path)

for ip, username, password in credentials:
  print(f"\n\n\tIP Address: {ip}, Username: {username}, Password: {password}\n")
  login = 'login.yaml'
  vars = {
    'ip' : ip,
    'usrname' : username,
    'pswrd' : password
  }
  run_playbook(login, vars)


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

while True:
    print("\n\tWelcome to Stratus ztC Edge")
    print("\n\n 1. DASHBOARD \n\n 2. SYSTEM \n\n 3. PREFERENCES \n\n 4. ALERTS & LOGS \n\n 5. VIRTUAL MACHINES MANAGEMENT \n\n 6. PHYSICAL MACHINES MANAGEMENT \n\n 7. LIBRARY ")
    print("\n\t Enter q to EXIT \n\n")

    ch = input("Choose your options: ")

    if ch == '1':
      for ip, username, password in credentials:
        print(f"\n\n\tIP Address: {ip}, Username: {username}, Password: {password}\n")
        vars = {
          'ip' : ip,
          'usrname' : username,
          'pswrd' : password
        }
        subprocess.run(['python3', 'dash.py', ip, username, password])

    if ch == '2':
      for ip, username, password in credentials:
        print(f"\n\n\tIP Address: {ip}, Username: {username}, Password: {password}\n")
        vars = {
          'ip' : ip,
          'usrname' : username,
          'pswrd' : password
        }
        subprocess.run(['python3', 'system.py', ip, username, password])

    if ch == '3':
      for ip, username, password in credentials:
        print(f"\n\n\tIP Address: {ip}, Username: {username}, Password: {password}\n")
        vars = {
          'ip' : ip,
          'usrname' : username,
          'pswrd' : password
        }
        subprocess.run(['python3', 'pref.py', ip, username, password])

    if ch == '4':
      for ip, username, password in credentials:
        print(f"\n\n\tIP Address: {ip}, Username: {username}, Password: {password}\n")
        vars = {
          'ip' : ip,
          'usrname' : username,
          'pswrd' : password
        }
        subprocess.run(['python3', 'logs.py', ip, username, password])

    if ch == '5':
      for ip, username, password in credentials:
        print(f"\n\n\tIP Address: {ip}, Username: {username}, Password: {password}\n")
        vars = {
          'ip' : ip,
          'usrname' : username,
          'pswrd' : password
        }
        subprocess.run(['python3', 'vmwf.py', ip, username, password])

    if ch == '6':
      for ip, username, password in credentials:
        print(f"\n\n\tIP Address: {ip}, Username: {username}, Password: {password}\n")
        vars = {
          'ip' : ip,
          'usrname' : username,
          'pswrd' : password
        }
        subprocess.run(['python3', 'nwf.py', ip, username, password])


    if ch == '7':
      for ip, username, password in credentials:
        print(f"\n\n\tIP Address: {ip}, Username: {username}, Password: {password}\n")
        vars = {
          'ip' : ip,
          'usrname' : username,
          'pswrd' : password
        }
        subprocess.run(['python3', 'up.py', ip, username, password])

    if ch == 'q':
      for ip, username, password in credentials:
        print(f"\n\n\tIP Address: {ip}, Username: {username}, Password: {password}\n")
        logout = 'logout.yaml'
        vars = {
          'ip' : ip,
          'usrname' : username,
          'pswrd' : password
        }
        run_playbook(logout, vars)
      break
