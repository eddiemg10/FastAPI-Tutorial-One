from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DB_URL = "sqlite:///./blog.db"
engine = create_engine(SQLALCHEMY_DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


"""
When using FastAPI's dependency injection system, a new instance of the dependency is created for each request. This means that a new database connection will be created and opened for each request, and then closed when the request is complete.

However, it's possible to reuse the same connection across multiple requests by using a connection pool. A connection pool is a cache of database connections that can be used and reused by multiple requests.

For example, if you're using SQLAlchemy as your ORM, you can use its built-in connection pooling system to manage your database connections. You can configure a connection pool with a certain maximum size, and then whenever a new connection is needed, SQLAlchemy will either reuse an existing connection from the pool or create a new one (up to the maximum size of the pool).

Here's an example of how you might use SQLAlchemy's connection pool with FastAPI:

--------------------------------------------------------------------------
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, pool_size=5, max_overflow=0)

def get_db():
    try:
        db = Session(autocommit=False, autoflush=False, bind=engine)
        yield db
    finally:
        db.close()
--------------------------------------------------------------------------

In this example, create_engine() is used to create a new SQLAlchemy engine object with a connection pool of size 5. The get_db() dependency then uses this engine to create a new database session for each request. When the session is no longer needed, it's closed and returned to the connection pool, where it can be reused by another request.

Note that the pool_size argument sets the maximum number of connections that can be in use at any given time. If all connections are in use and a new one is requested, the max_overflow argument determines whether a new connection can be created (if max_overflow is greater than 0) or whether the request should be blocked until a connection becomes available (if max_overflow is 0).

Using a connection pool can help improve the performance of your FastAPI application, as it reduces the overhead of opening and closing database connections for each request. However, it's important to choose an appropriate pool size based on the expected traffic to your application and the capacity of your database server.
"""
