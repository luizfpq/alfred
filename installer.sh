#!/bin/bash

# Verifica se o python3-full está instalado
if ! dpkg -s python3-full >/dev/null 2>&1; then
    echo "Instalando python3-full..."
    sudo apt-get install -y python3-full
fi

# Verifica se o pipx está instalado
if ! command -v pipx >/dev/null 2>&1; then
    echo "Instalando pipx..."
    python3 -m pip install --user pipx
    python3 -m userpath append ~/.local/bin
fi

# Solicita o nome do pacote a ser instalado
read -p "Digite o nome do pacote Python a ser instalado: " package_name

# Tenta instalar o pacote como um pacote Debian
if apt-cache show python3-$package_name >/dev/null 2>&1; then
    echo "Instalando pacote Debian python3-$package_name..."
    sudo apt-get install -y python3-$package_name
else
    echo "O pacote $package_name não é um pacote Debian. Instalando com pipx..."
    pipx install $package_name
fi