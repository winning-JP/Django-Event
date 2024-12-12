
# Django-Event


## コマンド

一個ずつ確実に実行してね❤

# ステップ1
```bash
<<<<<<< HEAD
poetry shell
```

```bash
cd myproject
```
とりあえずDjangoとMySQLを使えるように必須項目を入れよう。
```bash
pip install django mysqlclient
=======
  poetry shell
```

```bash
  cd myproject
```
とりあえずDjangoとMySQLを使えるように必須項目を入れよう。
```bash
  pip install django mysqlclient
>>>>>>> 0ac60e3ba1ac44fd83f7fb2b0143593d338da2c8
```

# ステップ2
> 既にeventのデータベースがあるとエラーが出るかも；；
```bash
<<<<<<< HEAD
python manage.py makemigrations
```

```bash
python manage.py migrate
```

```bash
python manage.py runserver
=======
  python manage.py makemigrations
```

```bash
  python manage.py migrate
```

```bash
  python manage.py runserver
>>>>>>> 0ac60e3ba1ac44fd83f7fb2b0143593d338da2c8
```

# トラブルシューティング
### データーベースがない・存在するけど正しく機能しない
```bash
<<<<<<< HEAD
mysql -u root
```
↓とりあえずデーターベースDROPして作り直す
```mysql
DROP DATABASE events;
```

```mysql
CREATE DATABASE events;
```

```mysql
exit;
```

```bash
python manage.py runserver
=======
  mysql -u root
```
↓とりあえずデーターベースDROPして作り直す
```mysql
  DROP DATABASE events;
```

```mysql
  CREATE DATABASE events;
```

```mysql
  exit;
```

```bash
  python manage.py runserver
>>>>>>> 0ac60e3ba1ac44fd83f7fb2b0143593d338da2c8
```

### `manage.py`とかが無いってエラーが出るって？？
```bash
<<<<<<< HEAD
cd myproject
=======
  cd myproject
>>>>>>> 0ac60e3ba1ac44fd83f7fb2b0143593d338da2c8
```