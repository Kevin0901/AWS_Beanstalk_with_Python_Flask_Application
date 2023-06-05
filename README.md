# AWS_Beanstalk_with_Python_Flask_Application
使用 AWS Beanstalk 搭建 python flask application 之範例程式碼

網站原始碼由以下 GitHub 專案改編成連接 MySQL：[專案連結](
https://github.com/PrettyPrinted/youtube_video_code/tree/master/2020/02/10/Creating%20a%20Login%20Page%20in%20Flask%20Using%20Sessions "Creating a Login Page in Flask Using Sessions")


### AWS 環境設定注意事項
- **平台選擇 Python 3.9**

![平台](https://media.discordapp.net/attachments/1115095502007050323/1115095517685370890/image.png "平台")

- **執行個體選 t3.medium 與 t3.large**

![執行個體](https://media.discordapp.net/attachments/1115095502007050323/1115097186070446171/image.png "執行個體")



### Python 程式碼設定區域
```Python
# 資料庫參數設定
db_settings = {
    "host": "在此填入 AWS RDS 連線端點",
    "port": 3306,
    "user": "資料庫帳號",
    "password": "資料庫密碼",
    "db": "資料庫名稱",
    "charset": "utf8"
}

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
```
