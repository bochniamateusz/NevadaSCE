from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app import models, schemas
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Strefy API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/check", response_model=schemas.CarResponse)
def check_car(input: str, db: Session = Depends(get_db)):
    input = input.strip().lower()

    car = db.query(models.Car).filter(
        (models.Car.car_id.ilike(input)) |
        (models.Car.number == input if input.isdigit() else False)
    ).first()

    if not car:
        raise HTTPException(status_code=404, detail="Nie znaleziono samochodu")
    return car
