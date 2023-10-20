# Configurações relativas ao ambiente Django

## Instalar dependências para funcionamento Django

```text
pip install django whitenoise gunicorn django-bootstrap4 PyMySQL django-stdimage
```

**WhiteNoise**: WhiteNoise é uma biblioteca que permite servir arquivos estáticos diretamente do aplicativo WSGI em produção. Ele foi projetado para trabalhar com servidores WSGI como Gunicorn e serve os arquivos estáticos do Django eficientemente, reduzindo a carga no servidor web.

**Gunicorn**: Gunicorn, ou "Green Unicorn", é um servidor WSGI HTTP para Python. Ele é usado para executar aplicativos web Python em produção. Ele é um dos servidores WSGI mais populares para aplicativos Django, pois é simples de configurar e oferece excelente desempenho.

**PyMySQL**: PyMySQL é um cliente MySQL para o Python. Ele permite que você se conecte a um banco de dados MySQL a partir de um script Python, execute consultas SQL e manipule dados no banco de dados.

**django-stdimage**: django-stdimage é uma biblioteca para o Django que fornece um campo ImageField personalizado. Ele adiciona várias opções úteis para lidar com imagens, como redimensionar imagens, recortar imagens e converter imagens para diferentes formatos. Ele é uma extensão do campo ImageField padrão do Django e é muito útil para gerenciar imagens em aplicativos Django.

## Criar Projeto django

```text
django-admin startproject nome_projeto .
```

## Criar apps para projeto django

```text
django-admin startapp <nome-do-app>
```

## Configurar o arquivo settings.py

```text
ALLOWED_HOSTS = ['*']

...

INSTALLED_APPS = [
    '.....',
    'core',
    'bootstrap4',
    'stdimage',
]

...

# O 'whitenoise.middleware.WhiteNoiseMiddleware' tem que ser em baixo do 'django.middleware.security.SecurityMiddleware' e será usado somente em produção
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    '........',
]

TEMPLATES = [
    {
        '.....'
        'DIRS': ['templates'],
        '.....',
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django2', # BASE_DIR / 'mydb',
        'USER':'user',
        'PASSWORD':'password',
        'HOST':'localhost',   # Ou um endereço de ip que seu db está hospedado
        'PORT':'3306',        # Porta do banco de dados (padrão 3306)
    }
}

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

```

## Criar no MySql Workbench o db (mydb)

## Comandos no Django

```text
python manage.py makemigrations
```

```text
python manage.py migrate
```

```text
python manage.py createsuperuser
```

```text
python manage.py runserver
```
