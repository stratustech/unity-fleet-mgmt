
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
  summary = 'summary.yaml'
  logout = 'logout.yaml'


  file_path = 'ip_address.txt'
  with open(file_path, 'r') as file:
    ip_address = file.readlines()

  ip_address = [ip.strip() for ip in ip_address]


  for idx, ip in enumerate(ip_address, start = 1):
    print(f"IP Address {idx}: {ip}")
    usrname = input("Enter the Username:\n")
    pswrd = getpass.getpass("Enter the Password:\n")
    vars = {
      'ip' : ip,
      'usrname' : usrname,
      'pswrd' : pswrd
    }
    run_playbook(login, vars)
    run_playbook(summary, vars)
    run_playbook(vm,vars)
    run_playbook(logout,vars)

main()

