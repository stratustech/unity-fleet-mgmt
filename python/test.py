
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
  vmcreate = 'vmcreate.yaml'
  vmpoweron = 'vmpoweron.yaml'
  vmpoweroff = 'vmpoweroff.yaml'
  vmshutdown = 'vmshutdown.yaml'
  vmcopy = 'vmcopy.yaml'
  logout = 'logout.yaml'
  print(" \n VM MANAGEMENT \n")
  print("\n1. VM Create\nUsage: vmcreate [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...[VM NAME]...[DECRIPTION]...[BOOT TYPE]...[NO OF VCPU]...[MEMORY SIZE]...[AVAILABILITY LEVEL]...[PREFEERED NODE]...[NO OF VOLUMES]...[REMOTE TYPE]...[REMOTE ISO PATH]...[NETWORK]...\n\n2. VM Power ON\nUsage: vmpoweron [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...[VM NAME]...\n\n3. VM Power OFF\nUsage: vmpoweron [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...[VM NAME]...\n\n4. VM Shutdown\nUsage: vmpoweron [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...[VM NAME]...\n\n5. VM Copy\nUsage: vmpoweron [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...[VM NAME]...\n\n")
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
  run_playbook(vm, vars)


  if ch=='1':
    vmname=input(" Enter the VM Name: ")
    vars['vmname'] = vmname
    description=input(" Enter the VM Description: ")
    vars['description'] = description
    bootType=input(" Enter the VM Boot Type: ")
    vars['bootType'] = bootType
    virtualCpus=input(" Enter the No of VPUs: ")
    vars['virtualCpus'] = virtualCpus
    memory=input(" Enter the Memory Size: ")
    vars['memory'] = memory
    availabilityLevel=input(" Enter the availability level: ")
    vars['availabilityLevel'] = availabilityLevel
    prefferednode=input(" Enter the Preffered node: ")
    vars['prefferednode'] = prefferednode
    volumes=input(" Enter the No of Volumes: ")
    vars['volumes'] = [volumes]
    remotetype=input(" Enter the remote type: ")
    vars['remotetype'] = remotetype
    remoteisopath=input(" Enter the remote ISO path: ")
    vars['remoteisopath'] = remoteisopath
    network=input(" Enter the network: ")
    vars['network'] = [network]
    run_playbook(vmcreate,vars)
  elif ch=='2':
    vmname=input(" Enter the VM Name: ")
    vars['vm'] = vmname
    run_playbook(vmpoweron,vars)
  elif ch=='3':
    vmname=input(" Enter the VM Name: ")
    vars['vm'] = vmname
    run_playbook(vmpoweroff,vars)
  elif ch=='4':
    vmname=input(" Enter the VM Name: ")
    vars['vm'] = vmname
    run_playbook(vmshutdown,vars)
  elif ch=='5':
    vmname=input(" Enter the VM Name: ")
    vars['vm'] = vmname
    run_playbook(vmcopy,vars)
  else:
    print("\n\n...INVALID CHOICE...\n\n")

  run_playbook(logout,vars)
main()
