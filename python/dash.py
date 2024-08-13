import ansible_runner
import getpass

def run_playbook(playbook_path, vars):
  runner = ansible_runner.run(
    private_data_dir='.',
    playbook=playbook_path,
    extravars=vars,
  )

def main():
  login = 'login.yaml'
  summary = 'summary.yaml'
  dash = 'dashboard.yaml'
  logout = 'logout.yaml'
  print(" \n DASHBOARD \n")
  print("Usage: dashboard [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...\n\n")
  ip = input("Enter the System IP:\n")
  usrname = input("Enter the Username:\n")
  pswrd = getpass.getpass("Enter the Password:\n")
  vars = {
    'ip' : ip,
    'usrname' : usrname,
    'pswrd' : pswrd
  }
  run_playbook(login, vars)
  run_playbook(summary, vars)
  run_playbook(dash, vars)
  run_playbook(logout,vars)
main()
