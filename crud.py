from sqlalchemy.orm import Session
import models

def create_weather(db: Session, data, weather_data):
    record = models.Weather(
        location=data.location,
        start_date=data.start_date,
        end_date=data.end_date,
        temperature=weather_data["temp"],
        description=weather_data["desc"]
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

def get_all(db: Session):
    return db.query(models.Weather).all()

def update_weather(db: Session, id: int, new_temp: float):
    record = db.query(models.Weather).get(id)
    record.temperature = new_temp
    db.commit()
    return record

def delete_weather(db: Session, id: int):
    record = db.query(models.Weather).get(id)
    db.delete(record)
    db.commit()