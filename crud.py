#test
from sqlalchemy.orm import Session
from models import StudentSurvey

def get_all_surveys(db: Session):
    return db.query(StudentSurvey).all()

def get_survey(db: Session, survey_id: int):
    return db.query(StudentSurvey).filter(StudentSurvey.id == survey_id).first()

def create_survey(db: Session, survey: StudentSurvey):
    db.add(survey)
    db.commit()
    db.refresh(survey)
    return survey

def delete_survey(db: Session, survey_id: int):
    survey = get_survey(db, survey_id)
    if survey:
        db.delete(survey)
        db.commit()

def update_survey(db: Session, survey_id: int, updated_data: dict):
    survey = get_survey(db, survey_id)
    if not survey:
        return None

    for key, value in updated_data.items():
        setattr(survey, key, value)

    db.commit()
    db.refresh(survey)
    return survey
