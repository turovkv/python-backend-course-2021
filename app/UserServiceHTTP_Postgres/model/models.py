from typing import List

from pydantic import BaseModel


class Answer(BaseModel):
    id: int
    title: str
    points: int

    class Config:
        orm_mode = True


class Question(BaseModel):
    id: int
    title: str
    answers: List[Answer]

    class Config:
        orm_mode = True


class Quiz(BaseModel):
    id: int
    title: str
    questions: List[Question]
    is_public: bool

    class Config:
        orm_mode = True


class User(BaseModel):
    id: int
    email: str
    password_hash: str

    class Config:
        orm_mode = True


class QuizSession(BaseModel):
    id: int
    quiz_id: int
    owner_id: int
    is_ended: bool

    class Config:
        orm_mode = True


class UserSession(BaseModel):
    id: int
    user_id: int
    quiz_session_id: int
    point_sum: int

    class Config:
        orm_mode = True
