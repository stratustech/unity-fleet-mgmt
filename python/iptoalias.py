input_file = 'ip_address.txt'
output_file = 'alias_address.txt'

with open(input_file, 'r') as file:
  ip_address = file.readlines()

ip_adress = [ip.strip() for ip in ip_address]

ip_alias = []

for idx, ip in enumerate(ip_address, start=1):
  alias = input(f"Enter alias for IP Adress {ip}: ")
  ip_alias.append((alias, ip))

with open(output_file, 'w') as file:
  for alias, ip in ip_alias:
    file.write(f"{alias} : {ip}")

print(f"IP addresses with alias is saved in {output_file}")
