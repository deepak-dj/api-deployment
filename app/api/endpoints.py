from typing import Optional, List
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.db import get_db, engine
from app.models import Indications, MarketBasket

import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

router = APIRouter()


class Author_P(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    email: str


# Register the custom dialect


class MarketBasketCreate(BaseModel):
    name: str
    indication_id: int


class MarketBasketOut(BaseModel):
    id: int
    name: str
    indication_id: int

    class Config:
        from_attributes = True


class IndicationCreate(BaseModel):
    name: str
    # indication_id: int


class IndicationOut(BaseModel):
    id: int
    name: str
    market_baskets: List[MarketBasketOut] = []
    diagonsis_codes: List[MarketBasketOut] = []
    surgery_codes: List[MarketBasketOut] = []

    # class Config:
    #     orm_mode = True
    class Config:
        from_attributes = True


def get_next_id(db: Session, table_name: str, id_column_name: str) -> int:
    # Get the maximum ID from the table
    result = db.execute(f"SELECT MAX({id_column_name}) FROM {table_name}").fetchone()
    max_id = result[0] if result[0] is not None else 0
    return max_id + 1


@router.post("/data")
async def create_data(data: IndicationCreate, db: Session = Depends(get_db)):
    try:
        next_id = get_next_id(db, 'indications', 'id')
        item = Indications(id=next_id, name=data.name)
        db.add(item)
        db.commit()
        db.refresh(item)  # Refresh to get the auto-generated ID
        return item
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@router.post("/market-basket")
async def create_market_data(data: MarketBasketCreate, db: Session = Depends(get_db)):
    try:
        next_id = get_next_id(db, 'market_basket', 'id')
        item = MarketBasket(id=next_id, name=data.name, indication_id=data.indication_id)
        db.add(item)
        db.commit()
        db.refresh(item)  # Refresh to get the auto-generated ID
        return item
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@router.get("/data")
async def get_data(indication: Optional[str] = None, db: Session = Depends(get_db)):
    try:
        # Query the database
        query = db.query(Indications)
        if indication:
            query = query.filter(Indications.name.ilike(f"%{indication}%"))
        items = query.all()
        response = [
            IndicationOut(
                id=indication.id,
                name=indication.name,
                market_baskets=[
                    MarketBasketOut(id=mb.id, name=mb.name, indication_id=mb.indication_id)
                    for mb in indication.market_baskets
                ]
            ) for indication in items
        ]

        return response
    except Exception as e:
        # Handle any errors that occur
        raise HTTPException(status_code=500, detail="An error occurred while retrieving data")


class UserModel(BaseModel):
    username: str
    password: str

#
# @router.get("/data/{id}", response_model=MyTableOut)
# async def get_data_by_id(id: int, db: Session = Depends(get_db)):
#     # Query the database for the record with the given ID
#     item = db.query(MyTable).filter(MyTable.id == id).first()
#     if item is None:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return item
#
#
# @router.delete("/data/{id}", response_model=None)
# async def delete_data_by_id(id: int, db: Session = Depends(get_db)):
#     # Query the database for the record with the given ID
#     item = db.query(MyTable).filter(MyTable.id == id).first()
#     if item is None:
#         raise HTTPException(status_code=404, detail="Item not found")
#
#     # Delete the record
#     db.delete(item)
#     db.commit()
#     return {"detail": "Item deleted successfully"}
