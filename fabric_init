yum install gcc* python-devel wget mysql mysql-devel mysql-server

wget http://python.org/ftp/python/2.7.3/Python-2.7.3.tar.bz2
tar xf Python-2.7.3.tar.bz2
cd Python-2.7.3
./configure --prefix=/usr/local/python && echo ok
make && make install && echo ok

vi /usr/bin/yum
修改第一行为/usr/bin/python2.6
ln -s /usr/local/python/bin/python /usr/bin/python
echo "$PATH=$PATH:/usr/local/python/bin/" >> /etc/profile

wget https://bootstrap.pypa.io/get-pip.py --no-check-certificate
python get-pip.py

pip install fabric
pip install requests
