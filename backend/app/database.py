from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import oracledb

# تهيئة عميل Oracle
oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient_11_2")

# إعدادات الاتصال
DATABASE_URL = "oracle+oracledb://sbcm:SbcMRkdjdvASAB@HASSAN:1521/?service_name=reef"

# إنشاء المحرك
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# اختبار الاتصال
try:
    # اختبار اتصال raw (اختياري)
    with oracledb.connect(
        user="sbcm",
        password="SbcMRkdjdvASAB",
        dsn="HASSAN:1521/reef"
    ) as conn:
        print("Raw connection success! Oracle version:", conn.version)

    # اختبار اتصال SQLAlchemy
    with engine.connect() as conn:
        print("SQLAlchemy connection successful!")
        
except Exception as e:
    print("Connection failed:", e)