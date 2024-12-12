
# Django-Event


## コマンド

一個ずつ確実に実行してね❤

# ステップ1
```bash
poetry shell
```

```bash
cd myproject
```
とりあえずDjangoとMySQLを使えるように必須項目を入れよう。
```bash
pip install django mysqlclient
```

# ステップ2
> 既にeventのデータベースがあるとエラーが出るかも；；
```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```

# トラブルシューティング
### データーベースがない・存在するけど正しく機能しない
```bash
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
```

### `manage.py`とかが無いってエラーが出るって？？
```bash
cd myproject
```