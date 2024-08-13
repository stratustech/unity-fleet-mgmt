
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

  limit = int(input("Enter the number of clusters:\n"))

  for i in range(limit):
    ip = input(f"Enter the System IP of CLUSTER {i+1}:\n")
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
