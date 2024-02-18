set -o errexit

pip install -r requirements.txt
# 静的ファイルの収集
python manage.py collectstatic --noinput
# DBの再構築
python manage.py migrate
# スーパーユーザーの作成
python manage.py superuser