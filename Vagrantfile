Vagrant.configure('2') do |config|
   config.vm.define :control do |control|
     control.vm.box = "ubuntu/xenial64"
     control.vm.hostname = "mesin1"
     control.vm.network :public_network
     control.vm.network :private_network, ip: "192.168.123.10"
     control.vm.provider :kvm do |kvm, override|
        kvm.memory_size     = '1024m'
     end
   end
   

   config.vm.provision "shell", inline: <<-SHELL
       apt-get update -y
       apt-get install -y avahi-daemon libnss-mdns
       apt-get install -y python3  python3-pip python3-venv
       pip3 install --upgrade pip
       cd /home/vagrant
       git clone https://github.com/rm77/phonebook-service.git
       cd phonebook-service
       git checkout on-docker-1
	
       python3 -m venv venv
       source venv/bin/activate
       pip3 install --upgrade pip
       pip3 install -r requirements.txt
       python3 Phonebook_Service.py
   SHELL
end
