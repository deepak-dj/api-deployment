from sqlalchemy import Column, String, Integer, text, Sequence, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
# Base = declarative_base()
from sqlalchemy.orm import relationship

from .db import Base

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Indications(Base):
    __tablename__ = 'indications'

    id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String(255), nullable=False)  # Consider making this non-nullable

    # Relationships
    market_baskets = relationship("MarketBasket", back_populates="indication", cascade="all, delete-orphan")
    diagnosis_codes = relationship("DiagnosisCode", back_populates="indication", cascade="all, delete-orphan")
    surgery_codes = relationship("SurgeryCode", back_populates="indication", cascade="all, delete-orphan")


class MarketBasket(Base):
    __tablename__ = 'market_basket'

    id = Column(Integer, primary_key=True, autoincrement=False)  # Add primary key
    name = Column(String(255), nullable=False)  # Consider making this non-nullable
    indication_id = Column(Integer, ForeignKey('indications.id'), nullable=False)

    # Relationship
    indication = relationship("Indications", back_populates="market_baskets")


class DiagnosisCode(Base):
    __tablename__ = 'diagnosis_code'  # Corrected typo in the table name

    id = Column(Integer, primary_key=True, autoincrement=False)  # Add primary key
    name = Column(String(255), nullable=False)  # Consider making this non-nullable
    indication_id = Column(Integer, ForeignKey('indications.id'), nullable=False)

    # Relationship
    indication = relationship("Indications", back_populates="diagnosis_codes")


class SurgeryCode(Base):
    __tablename__ = 'surgery_code'

    id = Column(Integer, primary_key=True, autoincrement=False)  # Add primary key
    name = Column(String(255), nullable=False)  # Consider making this non-nullable
    indication_id = Column(Integer, ForeignKey('indications.id'), nullable=False)

    # Relationship
    indication = relationship("Indications", back_populates="surgery_codes")
