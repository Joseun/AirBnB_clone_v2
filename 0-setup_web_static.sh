#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

apt-get -y update 
apt-get -y install nginx
ufw allow 'Nginx HTTP'
ufw allow 'OpenSSH'
service nginx start
mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu /data/
chgrp -R ubuntu /data/
sed -i '/listen 80 default_server/a location /hbnb_static/ {\n\t\t alias /data/web_static/current;\n\tindex index.html index.htm;\n\t}' /etc/nginx/sites-available/default
service nginx restart
