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
  pref = 'pref.yaml'
  oi = 'ownerinfo.yaml'
  pl = 'productlicense.yaml'
  sw = 'swupdate.yaml'
  ipconfig = 'ipconfiguration.yaml'
  qs = 'quorumservers.yaml'
  dt = 'dateandtime.yaml'
  ms = 'mailserver.yaml'
  at = 'admintools.yaml'
  sc = 'secureconnection.yaml'
  nt = 'notification.yaml'
  rs = 'remotesupport.yaml'
  logout = 'logout.yaml'
  print(" \n PREFERENCES \n")
  print("\n\nSYSTEM\n\n1. OWNER INFORMATION\nUsage: ownerinfo [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...\n\n2. PRODUCT LICENSE\nUsage: productlicense [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...\n\n3. SOFTWARE UPDATE\nUsage: swupdate [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...\n\n4. IP CONFIGURATION \nUsage: ipconfiguration [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...\n\n5. QUORUM SERVERS\nUsage: quorumservers [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...\n\n6. DATE AND TIME\nUsage: dateandtime [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...\n\n7. MAIL SERVER\nUsage: mailserver [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...\n\nADMINISTRATION TOOLS\n\n8. USERS AND GROUPS\nUsage: admintools [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...\n\n9. SECURE CONNECTION\nUsage: secureconnection [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...\n\nNOTIFICATION\n\n10. NOTIFY \nUsage: notify [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...\n\nREMOTE SUPPORT \n\n11. SUPPORT\nUsage: remotesupport [SYSTEM IP ADDRESS]...[LOGIN USERNAME]...[LOGIN PASSWORD]...\n\n")
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
  run_playbook(pref, vars)


  if ch=='1':
    run_playbook(oi, vars)
  elif ch=='2':
    run_playbook(pl, vars)
  elif ch=='3':
    run_playbook(sw, vars)
  elif ch=='4':
    run_playbook(ipconfig, vars)
  elif ch=='5':
    run_playbook(qs, vars)
  elif ch=='6':
    run_playbook(dt, vars)
  elif ch=='7':
    run_playbook(ms, vars)
  elif ch=='8':
    run_playbook(at, vars)
  elif ch=='9':
    run_playbook(sc, vars)
  elif ch=='10':
    run_playbook(nt, vars)
  elif ch=='11':
    run_playbook(rs, vars)



  else:
    print("\n\n...INVALID CHOICE...\n\n")

  run_playbook(logout,vars)
main()

