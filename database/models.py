# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  November 12, 2024 20:13:53
# Database: sqlite:////tmp/tmp.F2FDrQzUVR-01JCH03SBPSAP5CAS4X33JY4BG/Pet_Shop_Management_System/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Customer(SAFRSBaseX, Base):
    """
    description: Table representing pet shop customers.
    """
    __tablename__ = 'customer'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    phone = Column(String)
    address = Column(String)
    balance = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)
    AttendanceList : Mapped[List["Attendance"]] = relationship(back_populates="customer")
    FeedbackList : Mapped[List["Feedback"]] = relationship(back_populates="customer")
    OrderList : Mapped[List["Order"]] = relationship(back_populates="customer")
    PetList : Mapped[List["Pet"]] = relationship(back_populates="owner")
    AppointmentList : Mapped[List["Appointment"]] = relationship(back_populates="customer")



class Event(SAFRSBaseX, Base):
    """
    description: Table representing events hosted by the pet shop.
    """
    __tablename__ = 'event'
    _s_collection_name = 'Event'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(Date)
    location = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    AttendanceList : Mapped[List["Attendance"]] = relationship(back_populates="event")



class Staff(SAFRSBaseX, Base):
    """
    description: Table representing staff members of the pet shop.
    """
    __tablename__ = 'staff'
    _s_collection_name = 'Staff'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    role = Column(String)
    hire_date = Column(Date)
    salary = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)
    FeedbackList : Mapped[List["Feedback"]] = relationship(back_populates="staff")
    ScheduleList : Mapped[List["Schedule"]] = relationship(back_populates="staff")



class Supplier(SAFRSBaseX, Base):
    """
    description: Table representing suppliers of pets.
    """
    __tablename__ = 'supplier'
    _s_collection_name = 'Supplier'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_email = Column(String)
    phone = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    StockList : Mapped[List["Stock"]] = relationship(back_populates="supplier")



class Attendance(SAFRSBaseX, Base):
    """
    description: Table representing attendance of customers for events.
    """
    __tablename__ = 'attendance'
    _s_collection_name = 'Attendance'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    event_id = Column(ForeignKey('event.id'))
    customer_id = Column(ForeignKey('customer.id'))

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("AttendanceList"))
    event : Mapped["Event"] = relationship(back_populates=("AttendanceList"))

    # child relationships (access children)



class Feedback(SAFRSBaseX, Base):
    """
    description: Table representing feedback from customers regarding services.
    """
    __tablename__ = 'feedback'
    _s_collection_name = 'Feedback'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customer.id'))
    staff_id = Column(ForeignKey('staff.id'))
    date_submitted = Column(Date)
    comments = Column(String)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("FeedbackList"))
    staff : Mapped["Staff"] = relationship(back_populates=("FeedbackList"))

    # child relationships (access children)



class Order(SAFRSBaseX, Base):
    """
    description: Table representing pet purchase orders.
    """
    __tablename__ = 'order'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    date_ordered = Column(DateTime)
    customer_id = Column(ForeignKey('customer.id'))
    amount_total = Column(Integer)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)
    OrderItemList : Mapped[List["OrderItem"]] = relationship(back_populates="order")



class Pet(SAFRSBaseX, Base):
    """
    description: Table representing pets managed by the pet shop.
    """
    __tablename__ = 'pet'
    _s_collection_name = 'Pet'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    species = Column(String, nullable=False)
    breed = Column(String)
    price = Column(Integer)
    owner_id = Column(ForeignKey('customer.id'))

    # parent relationships (access parent)
    owner : Mapped["Customer"] = relationship(back_populates=("PetList"))

    # child relationships (access children)
    AppointmentList : Mapped[List["Appointment"]] = relationship(back_populates="pet")
    OrderItemList : Mapped[List["OrderItem"]] = relationship(back_populates="pet")
    StockList : Mapped[List["Stock"]] = relationship(back_populates="pet")



class Schedule(SAFRSBaseX, Base):
    """
    description: Table representing work schedules for staff members.
    """
    __tablename__ = 'schedule'
    _s_collection_name = 'Schedule'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    staff_id = Column(ForeignKey('staff.id'))
    shift_date = Column(Date)
    start_time = Column(DateTime)
    end_time = Column(DateTime)

    # parent relationships (access parent)
    staff : Mapped["Staff"] = relationship(back_populates=("ScheduleList"))

    # child relationships (access children)



class Appointment(SAFRSBaseX, Base):
    """
    description: Table representing appointments for pet grooming or veterinary visits.
    """
    __tablename__ = 'appointment'
    _s_collection_name = 'Appointment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customer.id'))
    pet_id = Column(ForeignKey('pet.id'))
    appointment_date = Column(Date)
    service_type = Column(String)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("AppointmentList"))
    pet : Mapped["Pet"] = relationship(back_populates=("AppointmentList"))

    # child relationships (access children)



class OrderItem(SAFRSBaseX, Base):
    """
    description: Table representing items within an order.
    """
    __tablename__ = 'order_item'
    _s_collection_name = 'OrderItem'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('order.id'))
    pet_id = Column(ForeignKey('pet.id'))
    quantity = Column(Integer, nullable=False)
    amount = Column(Integer)

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(back_populates=("OrderItemList"))
    pet : Mapped["Pet"] = relationship(back_populates=("OrderItemList"))

    # child relationships (access children)



class Stock(SAFRSBaseX, Base):
    """
    description: Table representing stock details of pets in the shop.
    """
    __tablename__ = 'stock'
    _s_collection_name = 'Stock'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    pet_id = Column(ForeignKey('pet.id'))
    supplier_id = Column(ForeignKey('supplier.id'))
    quantity = Column(Integer)
    last_restocked = Column(Date)

    # parent relationships (access parent)
    pet : Mapped["Pet"] = relationship(back_populates=("StockList"))
    supplier : Mapped["Supplier"] = relationship(back_populates=("StockList"))

    # child relationships (access children)
