
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
  vm = 'virtualmachines.yaml'
  vmpoweron = 'vmpoweron.yaml'
  vmpoweroff = 'vmpoweroff.yaml'
  vmshutdown = 'vmshutdown.yaml'
  vmcopy = 'vmcopy.yaml'
  logout = 'logout.yaml'
  print(" \n VM MANAGEMENT \n")
  print("\n1. VM Power ON\nUsage: vmpoweron [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...[VM NAME]...\n\n2. VM Power OFF\nUsage: vmpoweron [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...[VM NAME]...\n\n3. VM Shutdown\nUsage: vmpoweron [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...[VM NAME]...\n\n4. VM Copy\nUsage: vmpoweron [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...[VM NAME]...\n\n")
  ch=input(" Enter the choice: ")
  ip = input("Enter the System IP:\n")
  usrname = input("Enter the Username:\n")
  pswrd = getpass.getpass("Enter the Password:\n")
  vars = {
    'ip' : ip,
    'usrname' : username,
    'pswrd' : password
 }

  run_playbook(login, vars)
  run_playbook(vm, vars)


  if ch=='1':
    vmname=input(" Enter the VM Name: ")
    vars['vm'] = vmname
    run_playbook(vmpoweron,vars)
  elif ch=='2':
    vmname=input(" Enter the VM Name: ")
    vars['vm'] = vmname
    run_playbook(vmpoweroff,vars)
  elif ch=='3':
    vmname=input(" Enter the VM Name: ")
    vars['vm'] = vmname
    run_playbook(vmshutdown,vars)
  elif ch=='4':
    vmname=input(" Enter the VM Name: ")
    vars['vm'] = vmname
    run_playbook(vmcopy,vars)
  else:
    print("\n\n...INVALID CHOICE...\n\n")

  run_playbook(logout,vars)
main()
