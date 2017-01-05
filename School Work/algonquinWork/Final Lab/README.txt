Before attempting to run this application, be sure to change the address location
on the following tags:

1. <form action="http://192.168.1.107/8279/main.py" name="gradeProfile" method="get">

2. <a href="http://192.168.1.107/8279/display.py">Display Results</a>

At the moment, the Pi does not have a static IP and is not port forwarded (I have not received a go-ahead from the company to fiddle with the router), so this only works within a local network.

It does not matter where the laptop side files go but it is important that the raspberry side files go into a directory that can be accessed by apache. I used the following permissions and directories for my 000-default.conf file:

<Directory /var/www/html>
	Options ExecCGI Indexes FollowSymLinks MultiViews
	AllowOverride None
	Order allow,deny
	allow from all
	AddHandler cgi-script .py
	DirectoryIndex index.py
</Directory>

