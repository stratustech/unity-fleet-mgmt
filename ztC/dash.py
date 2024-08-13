import sys
import ansible_runner

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
  dash = 'dashboard.yaml'
  print("Usage: dashboard [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...\n\n")
  vars = {
    'ip' : ip,
    'usrname' : username,
    'pswrd' : password
  }
  run_playbook(dash, vars)
main()
