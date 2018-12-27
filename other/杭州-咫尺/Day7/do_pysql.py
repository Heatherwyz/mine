# -*- coding:utf-8 -*-

import pymysql
import random

__author__ = 'Heather'

if __name__ == "__main__":
    print ("PyMySQL基本示例")

    # 创建一个连接实例
    conn = pymysql.connect (
        host="10.68.3.88",  # mysql服务ip地址，若服务在本机则用localhost
        port=3306,  # mysql服务端口
        user="liyiming",  # 访问mysql的用户名
        password="liyiming",  # 访问mysql的密码
        db="zzb_pro",  # 默认连接到的数据库
        charset="utf8"  # 连接字符集
    )

    try:
        # 创建用于交互的cursor对象
        cursor = conn.cursor ()

        # 先插入10条测试数据

        # 构建插入数据的sql
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"

        # 生成10条测试数据
        sql_data = []
        for index in range (0, 10):
            email = "%.10f@126.com" % random.random ()
            password = random.random ()
            sql_data.append ((email, password))

            # 执行sql,进行批量插入数据
        cursor.executemany (sql, sql_data)

        # 提交至数据库
        conn.commit ()

        # 查询5条数据
        sql = "SELECT * FROM `users` LIMIT 5"

        # 执行sql
        cursor.execute (sql)

        # 取查询到的所有数据
        all_data = cursor.fetchall ()

        # 遍历打印出来
        print ("取所有查询到的数据")
        for data in all_data:
            print ("id: %d email: %s password: %s" %
                   (data[0], data[1], data[2]))

            # 取1条数据
        # cursor.execute(sql)
        one_data = cursor.fetchone ()
        print ("\n取1条数据")
        print ("id: %d email: %s password: %s" %
               (one_data[0], one_data[1], one_data[2]))

    finally:
        # 最后把数据库连接关闭
        conn.close ()