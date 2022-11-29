from typing import Optional

import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import HTTPException

from schemas import (
    load_db,
    CarInput,
    save_db,
    CarOutput,
    TripInput,
    TripOutput
)

app = FastAPI(title="Car Sharing")
db = load_db()


@app.get('/api/cars')
def get_cars(size: Optional[str] = None, doors: Optional[int] = None) -> list:
    result = db
    if size:
        result = [car for car in result if car.size == size]
    if doors:
        result = [car for car in result if car.doors == doors]
    return result


@app.get("/api/cars/{id}")
def car_by_id(id: int) -> dict:
    for car in db:
        if car.id == id:
            return car
    raise HTTPException(status_code=404, detail=f"No car found wth id = {id}")


@app.post("/api/cars", response_model=CarOutput)
def add_car(car: CarInput) -> CarOutput:
    new_car = CarOutput(size=car.size,
                        doors=car.doors,
                        fuel=car.fuel,
                        transmission=car.transmission,
                        id=len(db)+1)
    db.append(new_car)
    save_db(db)
    return new_car


@app.put("/api/cars/{id}", response_model=CarOutput)
def change_car(id: int, new_data: CarInput) -> CarOutput:
    matches = [car for car in db if car.id == id]
    if matches:
        car = matches[0]
        car.fuel = new_data.fuel
        car.transmission = new_data.transmission
        car.size = new_data.size
        car.doors = new_data.doors
        save_db(db)
        return car
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")


@app.delete("/api/cars/{id}", status_code=204)
def remove_car(id: int) -> None:
    matches = [car for car in db if car.id == id]
    if matches:
        car = matches[0]
        db.remove(car)
        save_db(db)
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")


@app.post("/api/cars/{car_id}/trips", response_model=TripOutput)
def add_trip(car_id: int, trip: TripInput) -> TripOutput:
    matches = [car for car in db if car.id == car_id]
    if matches:
        car = matches[0]
        new_trip = TripOutput(id=len(car.trips)+1,
                              start=trip.start, end=trip.end,
                              description=trip.description)
        car.trips.append(new_trip)
        save_db(db)
        return new_trip
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")


if __name__ == "__main__":
    uvicorn.run('carsharing:app', reload=True)
