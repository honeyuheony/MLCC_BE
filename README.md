# ๐ปMLCC_BE

2021-03 ~ ing

### MLCC ์ ์ธต ์ผ๋ผ์ธ๋จผํธ ์์คํ

์ผ์ฑ๊ธฐ์ ์ ๋ฐ๋์ฒด ํ์ง๊ฒ์ฌ ๊ณต์ ์์ ์ฌ์ฉํ  ๋ชฉ์ ์ผ๋ก ๋ง๋  ๋ชจ๋ธ ์๋น | ๋ชจ๋ํฐ๋ง ์๋น์ค์๋๋ค.
๋ฐ๋์ฒด์ ํ์ง(๋ง์ง๋ฅ )์ ๋น๋กฏํ ํ๊ฐ ๋ฐ์ดํฐ ๋ชจ๋ธ ์ฐ์ถ๋ฌผ์ ๊ณต์  ๋ด ์ ๋ฌธ๊ฐ๋ค์ด ์ฝ๊ฒ ํ์ธํด 
ํ์ง ๋ถ์ ๋ฐ ๋ชจ๋ธ ์ฑ๋ฅ ํฅ์์ ๊ธฐ์ฌํ  ์ ์๋๋ก ์น ํํ๋ก ์ ์ํ์ต๋๋ค.

- Celery ๊ธฐ๋ฐ ๋ชจ๋ธ ์๋น
- ๋ถ์ ๋ฐ์ดํฐ ๋ชจ๋ํฐ๋ง์ ์ํ API ๊ตฌํ


### Install

#### Git Clone
```
    $ git clone https://github.com/Woo-Yeol/MLCC_BE.git
```

#### Create Venv
```
    $ python -m venv venv
```

#### Activate Venv
```
    Mac
    $ source venv/bin/activate
    
    Window
    $ source venv/Scripts/activate
```

#### Requirements Install
```
    $ pip install -r requirements.txt 
```

#### Settings.py -> secrets.json ์์ฑ
```
    {
    "SECRET_KEY": "*******************"
    }
```

#### Migration
```
    $ sh migrate.sh
```

#### Run Server
```
    $ python manage.py runserver
```

### After Pull

#### Reset Migration
- Error ๋ฐ์์
```
    $ rm ./db.sqlite3
    $ sh reset_migration.sh
    $ sh migrate.sh
```

#### ์ข์์ฑ ์๋ฐ์ดํธ
```
    $ pip install -r requirements.txt
```
