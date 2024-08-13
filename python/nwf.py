
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
  pm = 'physicalmachines.yaml'
  workon = 'workon.yaml'
  workoff = 'workoff.yaml'
  nodeshutdown = 'nodeshutdown.yaml'
  systemshutdown = 'systemshutdown.yaml'
  logout = 'logout.yaml'
  print(" \n PHYSICAL MACHINE MANAGEMENT \n")
  print("\n1. NODE WORK ON\nUsage: workon [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...[NODE NAME]...\n\n2. NODE WORK OFF\nUsage: workoff [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...[NODE NAME]...\n\n3. NODE Shutdown\nUsage: nodeshutdowm [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...[NODE NAME]...\n\n4. SYSTEM SHUTDOWN\nUsage:  [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...\n\n")
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
  run_playbook(pm, vars)


  if ch=='1':
    node=input(" Enter the node Name: ")
    vars['node'] = node
    run_playbook(workon, vars)
  elif ch=='2':
    node=input(" Enter the node Name: ")
    vars['node'] = node
    run_playbook(workoff,vars)
  elif ch=='3':
    node=input(" Enter the node Name: ")
    vars['node'] = node
    run_playbook(nodeshutdown,vars)
  elif ch=='4':
    run_playbook(systemshutdown,vars)
  else:
    print("\n\n...INVALID CHOICE...\n\n")

  run_playbook(logout,vars)
main()
