# Ajedrez por Juan Martin Valverde Blasco

# Mantenibilidad
(<a href="https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-Juan-Martin-Valverde-Blasco/maintainability"><img src="https://api.codeclimate.com/v1/badges/b2506b61c30f1f5bafd1/maintainability" /></a>)

# Covertura del codigo
(<a href="https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-Juan-Martin-Valverde-Blasco/test_coverage"><img src="https://api.codeclimate.com/v1/badges/b2506b61c30f1f5bafd1/test_coverage" /></a>)

# Estado en CircleCI
(<a href="https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-Juan-Martin-Valverde-Blasco/tree/main"><img src="https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-Juan-Martin-Valverde-Blasco/tree/main.svg?style=svg"></a>)

# Descripcion

Esto es un ajedrez hecho en python y corrido en docker mediante terminal de linux, su forma de jugar es igual a la tradicional 

# Como ejecutar este juego

- Lo primero que debes hacer es instalar pip con el siguiente comando:

```
sudo apt-get install git 
```
- Una vez que tenes git es hora de clonar el repo:
```
git clone https://github.com/um-computacion-tm/ajedrez-2024-Juan-Martin-Valverde-Blasco.git
```
- Bien ahora metete al archivo abriendolo con visualstudio code o el interprete que tengas

- Adentro de este repo hay un archvio dockerfile el cual hace que funcione todo bien, asegurate de tener docker instalado:
```
docker build -t [nombre de la imagen] . 
```
- Una vez tiene la imagen hecha toca correrla:
```
docker run -it [nombre de la imagen] 
```

# Como correr los test sin correr el juego completo

- Si usas coverje es:
```
coverage run -m unittest && coverage report -m
```
- en caso de que sea por codeclimate ejecutar:
```
. test.sh
```

#MUCHAS GRACIAS

