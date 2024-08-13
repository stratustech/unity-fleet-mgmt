
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
  alerts = 'alerts.yaml'
  supportlogs = 'supportlogs.yaml'
  auditlogs = 'auditlogs.yaml'
  logout = 'logout.yaml'
  print(" \n ALERTS & LOGS \n")
  print("\n1. ALERT HISTORY\nUsage: alerts [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...\n\n2. SUPPORT LOGS\nUsage: supportlogs [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...\n\n3. AUDIT LOGS \nUsage: auditlogs [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...\n\n")
  ch=input(" Enter the choice: ")
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


  if ch=='1':
    run_playbook(alerts, vars)
  elif ch=='2':
    run_playbook(supportlogs,vars)
  elif ch=='3':
    run_playbook(auditlogs,vars)
  else:
    print("\n\n...INVALID CHOICE...\n\n")

  run_playbook(logout,vars)
main()

