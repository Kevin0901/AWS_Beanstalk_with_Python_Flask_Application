from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)

import pymysql

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []

# 資料庫參數設定
db_settings = {
    "host": "在此填入 AWS RDS 連線端點",
    "port": 3306,
    "user": "資料庫帳號",
    "password": "資料庫密碼",
    "db": "資料庫名稱",
    "charset": "utf8"
}

def get_Database():
    global users
    try:
        # 建立Connection物件
        conn = pymysql.connect(**db_settings)
        # 建立Cursor物件
        with conn.cursor() as cursor:
            # 查詢資料SQL語法
            command = "SELECT * FROM 資料表名稱"
            # 執行指令
            cursor.execute(command)
            # 取得所有資料
            result = cursor.fetchall()
            print(result)

            # 將所有資料填入到 users 陣列
            for i in result:
                users.append(User(id=i[0], username=i[1], password=i[2]))

    except Exception as ex:
        print(ex)


application = Flask(__name__)
application.secret_key = 'somesecretkeythatonlyishouldknow'

@application.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user
        

@application.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        global users
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        
        users = []
        get_Database()
        if users != []:
            user = [x for x in users if x.username == username][0]
            if user and user.password == password:
                session['user_id'] = user.id
                return redirect(url_for('profile'))
        else:
            print("users list is empty")
            
        return redirect(url_for('login'))

    return render_template('login.html')

@application.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('login'))

    return render_template('profile.html')

if __name__ == "__main__":
    application.run()