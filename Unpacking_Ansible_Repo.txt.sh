


sudo apt-get install python3-packaging python3-resolvelib
sudo apt-get install python3-packaging

cd ansible
tar -xvf repo.tar ./
cd repo
dpkg -i pool/main/a/ansible/ansible_8.7.0-1ppa~jammy_all.deb pool/main/a/ansible-core/ansible-core_2.15.9-1ppa~jammy_all.deb

ansible --version