from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    refresh_token: str

class BookMakerBase(BaseModel):
    name: str
    book_type: str
    website: str = None
    location: str = None

    class Config:
        orm_mode = True


class Bookmaker(BookMakerBase):
    id: int


class BookyBalance(BaseModel):
    user_id: int
    booky_id: int
    balance: float = 0


class BetBase(BaseModel):
    back_booky_id = int
    lay_booky_id = int


class CreateBet(BetBase):
    user_id = int


class Bet(BetBase):
    id = int


class BetDetailBase(BaseModel):
    back_odds = float
    lay_odds = float
    event_type: str = None
    event: str = None
    event_date: str
    settled: bool
    comments: str = None
    money_gain = float


class BetDetail(BetDetailBase):
    id: int
