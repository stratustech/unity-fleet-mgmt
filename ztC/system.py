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
  ns = 'nodestats.yaml'
  cs = 'clusterstats.yaml'
  print(" \n SYSTEM STATS \n")
  print("\n1. NODE STATS\nUsage: nodestats [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...\n\n2. CLUSTER STATS\nUsage: clusterstats [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...\n")

  ch=input(" Enter the choice: ")
  vars = {
    'ip' : ip,
    'usrname' : username,
    'pswrd' : password
  }

  if ch=='1':
    run_playbook(ns, vars)
  elif ch=='2':
    run_playbook(cs, vars)
  else:
    print("\n\n...INVALID CHOICE...\n\n")

main()
