from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date
import models, schemas, crud
from database import SessionLocal, engine
from weather_service import get_weather
from export import export_to_csv

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE
@app.post("/weather/")
def create_weather(data: schemas.WeatherCreate, db: Session = Depends(get_db)):
    if data.start_date > data.end_date:
        raise HTTPException(status_code=400, detail="Invalid date range")

    weather_data = get_weather(data.location)

    return crud.create_weather(db, data, weather_data)

# READ
@app.get("/weather/")
def read_weather(db: Session = Depends(get_db)):
    return crud.get_all(db)

# UPDATE
@app.put("/weather/{id}")
def update_weather(id: int, temp: float, db: Session = Depends(get_db)):
    return crud.update_weather(db, id, temp)

# DELETE
@app.delete("/weather/{id}")
def delete_weather(id: int, db: Session = Depends(get_db)):
    crud.delete_weather(db, id)
    return {"message": "Deleted"}

# EXPORT
@app.get("/export/csv")
def export_data(db: Session = Depends(get_db)):
    data = crud.get_all(db)
    export_to_csv(data)
    return {"message": "Exported to CSV"}