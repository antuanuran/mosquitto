# 1. План А
sudo sh -c 'echo "{\n "registry-mirrors": ["https://mirror.gcr.io", "https://daocloud.io", "https://c.163.com/", "https://registry.docker-cn.com"\]\n}" > /etc/docker/daemon.json'

sudo systemctl daemon-reload

sudo systemctl restart docker

# 2. План Б

sudo reboot

sudo rm -f /etc/docker/daemon.json

{
 "registry-mirrors": ["https://mirror.gcr.io", "https://daocloud.io", "https://c.163.com/", "https://registry.docker-cn.com"]
}

sudo systemctl daemon-reload

sudo systemctl restart docker


Mosquitto:
mosquitto_sub -t 'test_mqtt' -v
