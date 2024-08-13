
import ansible_runner
import getpass

def read_ipfile(filename):
  ip_aliases = {}
  with open(filename, 'r') as file:
    for line in file:
      alias, ip = line.strip().split(' : ')
      ip_aliases[alias] = ip
  return ip_aliases

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

  ip_file = "alias_address.txt"
  ip_aliases = read_ipfile(ip_file)

  limit = int(input("Enter the number of clusters:\n"))

  for i in range(limit):
    alias_input = input(f"Enter the Alias of System IP of CLUSTER {i+1}:\n")
    if alias_input in ip_aliases:
      print(f"System IP = {ip_aliases[alias_input]}")
    usrname = input("Enter the Username:\n")
    pswrd = getpass.getpass("Enter the Password:\n")
    vars = {
      'ip' : ip_aliases[alias_input],
      'usrname' : usrname,
      'pswrd' : pswrd
    }
    run_playbook(login, vars)
    run_playbook(summary, vars)
    run_playbook(vm,vars)
    run_playbook(logout,vars)

main()
