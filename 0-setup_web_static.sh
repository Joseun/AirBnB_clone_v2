#!/usr/bin/env bash
#Bash script to prepare web servers for deployment of web_static

if [ ! -x "$(command -v nginx)" ]; then
	sudo apt-get -y update
	sudo apt-get -y install nginx
	sudo ufw --force enable
	sudo ufw allow 'Nginx HTTP'
	sudo ufw allow 22
fi
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
if [[ -L "/data/web_static/current/test" ]]; then
	sudo unlink /data/web_static/current/
else
	sudo ln -s /data/web_static/releases/test/ /data/web_static/current
	unlink /data/web_static/current/test
fi
sudo chown -R ubuntu:ubuntu /data/
sudo chmod 777 /etc/nginx/sites-available/default
sudo sed -i "0,/location \/ {/s/location \/ {/location \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;/" /etc/nginx/sites-available/default
sudo service nginx restart
