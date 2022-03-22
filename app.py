from flask import Flask,render_template#返回网页内容
import sqlite3
app = Flask(__name__)


@app.route('/index')
def index():
    infos = [] #数列
    con = sqlite3.connect("BOOKNN.db")
    cur = con.cursor()
    sql = "select 类目,图书,评分 from book2021 where 排名=1 limit 0,5"
    data = cur.execute(sql)
    for item in data:
        infos.append(item) #增加每一个item到info

    score = []
    num = []
    con = sqlite3.connect("BOOKNN.db")

    cur = con.cursor()
    sql = "SELECT 类目,count(类目) 占比 FROM book2021 WHERE 类目 in('历史文化','社科纪实','科学新知','艺术设计','影视戏剧') and 评分>9 group by 类目"
    data1 = cur.execute(sql)
    for item in data1:
        score.append(item[0])
        num.append(item[1])
        #project.append([item[1],item[0]])  0是查询结果的第1列 #1是查询结果的第2列

    cur.close()  #关掉查询
    con.close()  #关掉数据库
    return render_template("index.html", infos=infos,score=score,num=num)

if __name__ == '__main__':
    app.run()
