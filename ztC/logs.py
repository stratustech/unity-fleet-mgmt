import ansible_runner
import sys

ip = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]

def run_playbook(playbook_path, vars):
  runner = ansible_runner.run(
    private_data_dir='.',
    playbook=playbook_path,
    extravars=vars,
  )

def main():
  login = 'login.yaml'
  alerts = 'alerts.yaml'
  supportlogs = 'supportlogs.yaml'
  auditlogs = 'auditlogs.yaml'
  logout = 'logout.yaml'
  print(" \n ALERTS & LOGS \n")
  print("\n1. ALERT HISTORY\nUsage: alerts [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...\n\n2. SUPPORT LOGS\nUsage: supportlogs [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...\n\n3. AUDIT LOGS \nUsage: auditlogs [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...\n\n")
  ch=input(" Enter the choice: ")
  vars = {
    'ip' : ip,
    'usrname' : username,
    'pswrd' : password
  }

  if ch=='1':
    run_playbook(alerts, vars)
  elif ch=='2':
    run_playbook(supportlogs,vars)
  elif ch=='3':
    run_playbook(auditlogs,vars)
  else:
    print("\n\n...INVALID CHOICE...\n\n")

main()
