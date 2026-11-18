from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app import models
from app.database import Base, engine, get_db

app = FastAPI()

Base.metadata.create_all(engine)

@app.get("/")
async def get_value(db: Session = Depends(get_db)):
    result = db.query(models.Counter.value).first()
    if not result:
        new_counter = models.Counter(value=1)
        db.add(new_counter)
        db.commit()
        db.refresh(new_counter)
        return {"number": new_counter.value}
    return {"number": result.value}

@app.post("/add")
async def add_one(db: Session = Depends(get_db)):
    current_number = db.query(models.Counter).first()
    if not current_number:
        new_counter = models.Counter(value=1)
        db.add(new_counter)
        db.commit()
        return
    current_number.value += 1
    db.add(current_number)
    db.commit()
    return

