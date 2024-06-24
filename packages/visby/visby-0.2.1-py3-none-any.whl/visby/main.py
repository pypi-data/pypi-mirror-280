from datetime import timedelta
from typing import Any, List, Optional, Sequence

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session

import visby.crud as crud
from visby.activity_model import Activity, ActivityCreate, ActivityRead
from visby.database import create_db_and_tables, engine
from visby.measurement_model import Measurement, MeasurementCreate, MeasurementRead
from visby.user_model import User, UserCreate, UserRead

create_db_and_tables(engine)
app = FastAPI()


def get_db() -> Any:
    with Session(engine) as session:
        yield session


@app.post("/api/users/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)) -> User:
    db_user = crud.get_users(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already exists.")
    return crud.create_user(db=db, user=user)


@app.get("/api/users/", response_model=List[UserRead])
def read_users(
    name: Optional[str] = None,
    user_id: Optional[int] = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> Sequence[User]:
    return crud.get_users(db, skip=skip, limit=limit, name=name, user_id=user_id)


@app.delete("/api/users/{user_id}", response_model=UserRead)
def delete_user(user_id: int, db: Session = Depends(get_db)) -> Optional[User]:
    db_user = crud.delete_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/api/measurements/", response_model=MeasurementRead)
def create_measurement(
    measurement: MeasurementCreate, db: Session = Depends(get_db)
) -> Measurement:
    try:
        return crud.create_measurement(db=db, measurement=measurement)
    except IntegrityError:
        raise HTTPException(status_code=404, detail="User does not exist")


@app.get("/api/measurements/", response_model=List[MeasurementRead])
def read_measurements(
    measurement_id: Optional[int] = None,
    user_id: Optional[int] = None,
    type: Optional[str] = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> Sequence[Measurement]:
    return crud.get_measurements(
        db,
        skip=skip,
        limit=limit,
        measurement_id=measurement_id,
        user_id=user_id,
        type=type,
    )


@app.delete("/api/measurements/{measurement_id}", response_model=MeasurementRead)
def delete_measurement(
    measurement_id: int, db: Session = Depends(get_db)
) -> Optional[Measurement]:
    db_measurement = crud.delete_measurement(db, measurement_id=measurement_id)
    if db_measurement is None:
        raise HTTPException(status_code=404, detail="Measurement not found")
    return db_measurement


@app.post("/api/activities/", response_model=ActivityRead)
def create_activity(
    activity: ActivityCreate, db: Session = Depends(get_db)
) -> Activity:
    try:
        return crud.create_activity(db=db, activity=activity)
    except IntegrityError:
        raise HTTPException(status_code=404, detail="User does not exist")


@app.get("/api/activities/", response_model=List[ActivityRead])
def read_activities(
    activity_id: Optional[int] = None,
    user_id: Optional[int] = None,
    type: Optional[str] = None,
    duration: Optional[timedelta] = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> Sequence[Activity]:
    return crud.get_activities(
        db,
        skip=skip,
        limit=limit,
        activity_id=activity_id,
        user_id=user_id,
        type=type,
        duration=duration,
    )


@app.delete("/api/activities/{activity_id}", response_model=ActivityRead)
def delete_activity(
    activity_id: int, db: Session = Depends(get_db)
) -> Optional[Activity]:
    db_activity = crud.delete_activity(db, activity_id=activity_id)
    if db_activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    return db_activity
