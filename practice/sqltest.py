from sqlalchemy import create_engine, text

db = {
    'user': 'user',
    'password':'password',
    'host':'localhost',
    'port':'port',
    'database':'miniter'
}

db_url = f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}?charset=utf8"

# Create_engine을 사용하여 데이터베이스에 연결하고 text를 사용하여 실행할 sql 를 만든다. 
# Create_engine은 Engine 객체를 리턴한다. 연결된 데이터베이스와 SQL 실행을 Engine 객체를 사용해서 할 수 있다. 
# 여기서는 Engine 객체를 db 변수에 저장했따. 

db = create_engine(db_url, encoding = 'utf-8', max_overflow = 0)
params = {'name':"test"}
rows = db.execute(text("SELECT *FROM users WHERE name = :name"), params).fetchall()

for row in rows :
    print(f"name:{row['name']}")
    print(f"email:{row['email']}")