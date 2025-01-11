                cursor.execute('insert into reviews(title,review,rating,itemid,username) values(%s,%s,%s,uuid_to_bin(%s),%s)',[title,reviewtext,rating,itemid,session.get('user')])
