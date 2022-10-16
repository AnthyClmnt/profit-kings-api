from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    first_name = Column(String)
    is_active = Column(Boolean, default=True)


class BookMaker(Base):
    __tablename__ = "book_maker"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    book_type = Column(String, nullable=False)
    website = Column(String)
    location = Column(String)


class BookyBalance(Base):
    __tablename__ = "booky_balance"

    user_id = Column(Integer, ForeignKey(User.id), primary_key=True)
    booky_id = Column(Integer, ForeignKey(BookMaker.id), nullable=False)
    balance = Column(Float, default=0)


class Bets(Base):
    __tablename__ = "bets"

    id = Column(Integer, primary_key=True, index=True)
    back_booky_id = Column(Integer, ForeignKey(BookMaker.id), nullable=False)
    lay_booky_id = Column(Integer, ForeignKey(BookMaker.id), nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)


class BetDetails(Base):
    __tablename__ = "bet_details"
    id = Column(Integer, ForeignKey(Bets.id), primary_key=True, index=True)
    back_odds = Column(Float, nullable=False)
    lay_odds = Column(Float, nullable=False)
    event_type = Column(String)
    event = Column(String)
    event_date = Column(DateTime, nullable=False)
    settled = Column(Boolean)
    comments = Column(String)
    money_gain = Column(Float, nullable=False)

    bet_id = relationship("Bets")
