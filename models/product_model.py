from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Corrected: Use declarative_base() from sqlalchemy.orm
Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float)

# Database connection
DATABASE_URL = "sqlite:///data/database.sqlite"
engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
    """ Create database tables """
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()