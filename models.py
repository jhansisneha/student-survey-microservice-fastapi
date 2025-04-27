from sqlalchemy import Column, Integer, String, Date
from database import Base

class StudentSurvey(Base):
    __tablename__ = "student_survey"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    street_address = Column(String(255))
    city = Column(String(255))
    state = Column(String(255))
    zip = Column(String(20))
    telephone = Column(String(20))
    email = Column(String(255))
    date_of_survey = Column(Date)
    liked_most = Column(String(255))
    interest_source = Column(String(255))
    recommendation_likelihood = Column(String(255))
