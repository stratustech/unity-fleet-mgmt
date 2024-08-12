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
  ns = 'nodestats.yaml'
  cs = 'clusterstats.yaml'
  logout = 'logout.yaml'
  print(" \n SYSTEM STATS \n")
  print("\n1. NODE STATS\nUsage: nodestats [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...\n\n2. CLUSTER STATS\nUsage: clusterstats [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...\n")
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
    run_playbook(ns, vars)
  elif ch=='2':
    run_playbook(cs, vars)
  else:
    print("\n\n...INVALID CHOICE...\n\n")

  run_playbook(logout,vars)
main()

