# Documento de iformações sobre o projeto

## Projeto Django - django2

### Descrição do projeto

O objetivo desse projeto é didático e mostrará as funcionalidades do Django com o MySql e o bootstrap.

## Apps do projeto

### core

Contem a plicação principal e deverá ser criado as pastas:

- templates - Que contém os arquivos html
  - contato.html
  - index.html
  - produto.html
- statics  - Que contém todas as pastas de estilos, scripts e imagens utilizadas no site
  - css
  - images
  - js
- urls.py   - Define as rotas chamados no views.py

## Configurações

Antes de mais nada, verificar se o servidor MySql está devidamente instalado na máquina local ou se for o caso de um DB externo, verificar se as configurações externas estão ok.

Para rodar esse projeto localmente você precisará ter instalado na máquina:

Se estiver no Ubuntu:

```text
sudo apt-get install libmysqlclient-dev python3-dev
```

Se estiver no Mac:

No SO instale:

```text
brew install pkg-config
brew install mysql
pip install mysqlclient
```

Depois no ambiente virtual:

```text
pip install mysqlclient
```

Talvez seja necessário:

```text
brew tap homebrew/core
brew install mysql-connector-c
```

Se estiver no Windows, e tem o servidor MySql instalado, as bibliotecas já devem estar instaladas
