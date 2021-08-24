# PKT_mine_optimizer
This is a short program to optimize pkt mining pools for packetcrypt

#Installation

### Install build tools
```bash
sudo apt-get update
sudo apt-get install -y unzip xvfb libxi6 libgconf-2-4
sudo apt-get install build-essential -y
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
wget https://golang.org/dl/go1.17.linux-amd64.tar.gz
sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go1.17.linux-amd64.tar.gz
```

### Add go to path
```bash
sudo vi /etc/profile
```
paste the following line at the end of the file 
```bash
sudo echo "export PATH=$PATH:/usr/local/go/bin" >> /etc/profile
```

```bash
source /etc/profile
```

### Install Packetcrypt

```bash
git clone http://github.com/cjdelisle/packetcrypt_rs
cd packetcrypt_rs
~/.cargo/bin/cargo build --release
```

### Install chrome driver

```bash
sudo apt-get install unzip

wget -N http://chromedriver.storage.googleapis.com/2.26/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo chmod +x chromedriver

sudo mv -f chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
```

#Run the program

```bash
python3 pool_handle.py
```


#Shut the program down 
```bash
ps -ef | grep pool_handle.py
```

Find the pid and kill it

```bash
kill PID#
```

Next kill the miner

```bash 
ps -ef | grep packetcrypt
```

Find the pid and kill it

```bash 
kill PID#
```


