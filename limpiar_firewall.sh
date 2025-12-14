#!/bin/bash
echo "🧹 Limpiando todas las reglas de firewall..."
sudo iptables -F
sudo iptables -X
sudo iptables -t nat -F
sudo iptables -t mangle -F
sudo iptables -P INPUT ACCEPT
sudo iptables -P FORWARD ACCEPT
sudo iptables -P OUTPUT ACCEPT
echo "✅ Firewall limpio y permisivo."