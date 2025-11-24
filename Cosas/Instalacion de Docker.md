---

---
# Preparacion del Entorno

En primer lugar se debe correr el siguiente comando para evitar posibles conflictos de archivos o paquetes previamenete instalados

```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 
podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

# Metodos de Instalacion

Hay diversas maneras de instalar docker, se puede instalar el motor de docker junto con su aplicacion cliente de escritorio o unicamente el motor y manejarse con comandos por terminal o algun otro cliente/extension del IDE.

En este caso vamos a instalar unicamente el motor y se muestra una extension de Visual Studio Code hacia el final.

## Instalando el Motor usando el Repositorio APT

Antes de instalar docker en la computadora se debe dejar preparado el repositorio apt

1. Preparando  el repositorio apt

```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o 
/etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] 
  https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") 
  stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

2. Instalar los paquetes de docker

```bash
sudo apt-get install docker-ce docker-ce-cli 
containerd.io docker-buildx-plugin docker-compose-plugin
```

## POST-INSTALL

Este procedimiento posterior a la instalacion describe como configurar la maquina host de Linux para trabajar mejor con Docker

## Manejar Docker como un usuario no-root

Para crear el grupo de docker y agregar nuestro usuario:

3. Crear el grupo `docker` .
```bash
sudo groupadd docker
```
4. Agregar nuestro usuario al grupo `docker` .
```bash
sudo usermod -aG docker $USER
```

3, Cerrar sesion y loguearse nuevamente para que nuestro usuario sea re-evaluado en el grupo.

5. Verificar que se pueden correr comandos de `docker`  sin utilizar `sudo`

### Configurar Docker para que Inicie al booteo

Para activar el inicio de Docker en el booteo de la maquina

```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

Para desactivarlo:

```bash
sudo systemctl disable docker.service
sudo systemctl disable containerd.service
```

# Extension de Visual Studio Code (opcional)

Se pueden manejar (ademas que desde la terminal) los contenedores e imagenes de Docker mediante una extension de Visual Studio Code.

La cual es la extension oficial de “Docker” la cual viene con “Container Tools”

<!-- Column 1 -->
![[image 20.png]]

<!-- Column 2 -->
![[image 21.png]]
