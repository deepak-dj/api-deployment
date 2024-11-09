# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
DATABASE_URL = "redshift+psycopg2://awsuser:9411337680Dj@default-workgroup.423623868179.ap-southeast-2.redshift-serverless.amazonaws.com:5439/dev?sslmode=require&options=-c search_path=public"

# DATABASE_URL = "postgresql+psycopg2://awsuser:Admin1234@redshift-cluster-1.cuhbht0y6yvu.eu-north-1.redshift.amazonaws.com:5439/dev"
engine = create_engine(DATABASE_URL)
# cnn = engine.connect()
# try:
#     cnn.execute(
#         '''
#                 CREATE TABLE authors (
#                     id INTEGER IDENTITY(1, 1) PRIMARY KEY,
#                     first_name VARCHAR,
#                     last_name VARCHAR,
#                     email VARCHAR UNIQUE
#                 )
#             '''
#     )
# except Exception as e:
#     raise
Base = declarative_base()
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
