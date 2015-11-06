# -*- mode: ruby -*-
# vi: set ft=ruby :

require "fileutils"

# the following is adapted from https://gist.github.com/juanje/3797297
def local_cache(basebox_name)
	cache_dir = Vagrant::Environment.new.home_path.join('cache', 'apt', basebox_name)
	partial_dir = cache_dir.join('partial')
	FileUtils.makedirs(partial_dir) unless partial_dir.exist?
	cache_dir
end

Vagrant.configure(2) do |config|
  config.vm.box = "debian/jessie64"
  config.vm.network "forwarded_port", guest: 80, host: 8080
  cache_dir = local_cache(config.vm.box)
  config.vm.synced_folder cache_dir, "/var/cache/apt/archives/"
  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install -y python-pelican screen nginx
    sed -i 's/\\/var\\/www\\/html/\\/vagrant\\/output/' /etc/nginx/sites-enabled/default
    systemctl restart nginx.service
    cd /vagrant
    make clean
    make html
  SHELL
end
