from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship

from config.DataBase import Base

class Store(Base):
    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), unique=True ,nullable=False)
    description = Column(String(500), nullable=False)
    address = Column(String(500), nullable=False)
    rating = Column(Integer, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"))
    products = relationship("Product")

    def __init__(self, name, description, address, rating, user_id):
        Base()
        self.name = name
        self.description = description
        self.address = address
        self.rating = rating
        self.user_id = user_id

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'address': self.address,
            'rating': self.rating,
            'user_id': self.user_id
        }
