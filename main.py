from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import crud
from datetime import date

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/surveys")
def create_survey(data: dict, db: Session = Depends(get_db)):
    survey = models.StudentSurvey(**data)
    return crud.create_survey(db, survey)

@app.get("/api/surveys")
def read_surveys(db: Session = Depends(get_db)):
    return crud.get_all_surveys(db)

@app.get("/api/surveys/{survey_id}")
def read_survey(survey_id: int, db: Session = Depends(get_db)):
    survey = crud.get_survey(db, survey_id)
    if not survey:
        raise HTTPException(status_code=404, detail="Survey not found")
    return survey

@app.delete("/api/surveys/{survey_id}")
def delete_survey(survey_id: int, db: Session = Depends(get_db)):
    crud.delete_survey(db, survey_id)
    return {"message": "Deleted"}

@app.put("/api/surveys/{survey_id}")
def update_survey(survey_id: int, data: dict, db: Session = Depends(get_db)):
    existing = crud.get_survey(db, survey_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Survey not found")

    for key, value in data.items():
        setattr(existing, key, value)
    
    db.commit()
    db.refresh(existing)
    return existing