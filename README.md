## API REST DJango Rest Framework

#### Crear proyecto

```sh
$ mkdir rest-devcode
$ cd rest-devcode
$ virtualenv . -p python3
$ git clone 'https://github.com/DevcodeInc/API-REST-DJango-Rest-Framework.git src'
$ git checkout 0.5
```

#### Aplicar requerimientos
```sh
$ source bin/activate
$ (rest-devcode) pip install -r requirements.txt
```

#### Configurar base de datos
```sh
DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'comprame_db',
            'USER': 'ever',
            'PASSWORD': 'secreto',
            'HOST': 'localhost',
            'PORT': '5432',
        }
}
```


#### Aplicar migraciones

```sh
$ (rest-devcode) cd src/
$ (rest-devcode) python manage.py makemigrations
$ (rest-devcode) python manage.py migrate
```

#### llenado de data
copiar sql y aplicar en la base de datos en el siguiente orden
```sh
1. compras_client.sql
2. compras_product.sql
3. compras_purchase.sql
4. compras_purchaseitem.sql
```

#### Sincronizar base de datos
Genera el código sql para sincronizar la base de datos
```sh
$ (rest-devcode) $ python manage.py sqlsequencereset compras 
```

#### Iniciar
```sh
$ (rest-devcode) python manage.py runserver
```