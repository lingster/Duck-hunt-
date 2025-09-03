import datetime
from sqlalchemy import create_engine, Column, String, Float, DateTime, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./properties.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class PropertyDB(Base):
    __tablename__ = "properties"

    url = Column(String, primary_key=True, index=True)
    location = Column(String, index=True)
    price = Column(Float, nullable=True)
    rooms = Column(Float, nullable=True)
    livable_area = Column(Float, nullable=True)
    total_area = Column(Float, nullable=True)
    first_seen = Column(DateTime, default=datetime.datetime.utcnow)
    last_seen = Column(DateTime, default=datetime.datetime.utcnow)
    car_parking = Column(Boolean, nullable=True)
    garage = Column(Boolean, nullable=True)
    swimming_pool = Column(Boolean, nullable=True)
    description = Column(String, nullable=True)
    html_path = Column(String, nullable=True)
    markdown_path = Column(String, nullable=True)


def create_db_and_tables():
    """Creates the database and tables if they don't exist."""
    Base.metadata.create_all(bind=engine)

def get_db():
    """Generator function to get a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
