python -V
pip list
.\.venv\Scripts\activate.bat
rem python -m pip install --upgrade pip
pip install Django==4.2
pip list

python manage.py runserver

# 在舊 venv 裡執行
pip freeze > requirements.txt

# 然後在新環境中安裝
pip install -r requirements.txt

