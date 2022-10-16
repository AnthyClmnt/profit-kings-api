from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_booky_by_id(db: Session, booky_id: int):
    return db.query(models.BookMaker).filter(models.BookMaker.id == booky_id).first()


def create_booky(db: Session, booky: schemas.BookMakerBase):
    db_booky = models.BookMaker(name=booky.name,
                                book_type=booky.book_type,
                                website=booky.website,
                                location=booky.location)
    db.add(db_booky)
    db.commit()
    db.refresh(db_booky)
    return db_booky
