# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime

logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


class Customer(Base):
    """description: Table representing pet shop customers."""
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    phone = Column(String)
    address = Column(String)
    balance = Column(Integer)


class Pet(Base):
    """description: Table representing pets managed by the pet shop."""
    __tablename__ = 'pet'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    species = Column(String, nullable=False)
    breed = Column(String)
    price = Column(Integer)
    owner_id = Column(Integer, ForeignKey('customer.id'))


class Order(Base):
    """description: Table representing pet purchase orders."""
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date_ordered = Column(DateTime, default=datetime.utcnow)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    amount_total = Column(Integer)


class OrderItem(Base):
    """description: Table representing items within an order."""
    __tablename__ = 'order_item'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    pet_id = Column(Integer, ForeignKey('pet.id'))
    quantity = Column(Integer, nullable=False)
    amount = Column(Integer)


class Supplier(Base):
    """description: Table representing suppliers of pets."""
    __tablename__ = 'supplier'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    contact_email = Column(String)
    phone = Column(String)


class Stock(Base):
    """description: Table representing stock details of pets in the shop."""
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True, autoincrement=True)
    pet_id = Column(Integer, ForeignKey('pet.id'))
    supplier_id = Column(Integer, ForeignKey('supplier.id'))
    quantity = Column(Integer)
    last_restocked = Column(Date)


class Attendance(Base):
    """description: Table representing attendance of customers for events."""
    __tablename__ = 'attendance'

    id = Column(Integer, primary_key=True, autoincrement=True)
    event_id = Column(Integer, ForeignKey('event.id'))
    customer_id = Column(Integer, ForeignKey('customer.id'))


class Event(Base):
    """description: Table representing events hosted by the pet shop."""
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    date = Column(Date)
    location = Column(String)


class Staff(Base):
    """description: Table representing staff members of the pet shop."""
    __tablename__ = 'staff'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    role = Column(String)
    hire_date = Column(Date)
    salary = Column(Integer)


class Schedule(Base):
    """description: Table representing work schedules for staff members."""
    __tablename__ = 'schedule'

    id = Column(Integer, primary_key=True, autoincrement=True)
    staff_id = Column(Integer, ForeignKey('staff.id'))
    shift_date = Column(Date)
    start_time = Column(DateTime)
    end_time = Column(DateTime)


class Appointment(Base):
    """description: Table representing appointments for pet grooming or veterinary visits."""
    __tablename__ = 'appointment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    pet_id = Column(Integer, ForeignKey('pet.id'))
    appointment_date = Column(Date)
    service_type = Column(String)


class Feedback(Base):
    """description: Table representing feedback from customers regarding services."""
    __tablename__ = 'feedback'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    staff_id = Column(Integer, ForeignKey('staff.id'))
    date_submitted = Column(Date)
    comments = Column(String)


# ALS/GenAI: Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ALS/GenAI: Prepare for sample data

# Test Data for Customer
customer1 = Customer(name='Alice Smith', email='alice@example.com', phone='555-0101', address='123 Elm St', balance=0)
customer2 = Customer(name='Bob Jones', email='bob@example.com', phone='555-0102', address='456 Oak St', balance=0)
customer3 = Customer(name='Eve Taylor', email='eve@example.com', phone='555-0103', address='789 Pine St', balance=0)
customer4 = Customer(name='Charlie Brown', email='charlie@example.com', phone='555-0104', address='101 Birch St', balance=0)

# Test Data for Pet
pet1 = Pet(name='Bella', species='Dog', breed='Beagle', price=250, owner_id=customer1.id)
pet2 = Pet(name='Max', species='Cat', breed='Siamese', price=150, owner_id=customer2.id)
pet3 = Pet(name='Charlie', species='Bird', breed='Parrot', price=300, owner_id=None)
pet4 = Pet(name='Molly', species='Fish', breed='Goldfish', price=20, owner_id=None)

# Test Data for Order
order1 = Order(date_ordered=date(2023, 1, 10), customer_id=customer1.id, amount_total=300)
order2 = Order(date_ordered=date(2023, 2, 15), customer_id=customer2.id, amount_total=150)
order3 = Order(date_ordered=date(2023, 3, 20), customer_id=customer3.id, amount_total=0)
order4 = Order(date_ordered=date(2023, 4, 25), customer_id=customer4.id, amount_total=20)

# Test Data for OrderItem
order_item1 = OrderItem(order_id=order1.id, pet_id=pet1.id, quantity=1, amount=250)
order_item2 = OrderItem(order_id=order2.id, pet_id=pet2.id, quantity=1, amount=150)
order_item3 = OrderItem(order_id=order3.id, pet_id=pet3.id, quantity=0, amount=0)
order_item4 = OrderItem(order_id=order4.id, pet_id=pet4.id, quantity=1, amount=20)

# Test Data for Supplier
supplier1 = Supplier(name='Happy Pets', contact_email='info@happypets.com', phone='555-0201')
supplier2 = Supplier(name='Animal House', contact_email='info@animalhouse.com', phone='555-0202')
supplier3 = Supplier(name='Pet World', contact_email='info@petworld.com', phone='555-0203')
supplier4 = Supplier(name='Tropical Fish Inc', contact_email='info@tropicalfish.com', phone='555-0204')

# Test Data for Stock
stock1 = Stock(pet_id=pet1.id, supplier_id=supplier1.id, quantity=10, last_restocked=date(2023, 1, 1))
stock2 = Stock(pet_id=pet2.id, supplier_id=supplier2.id, quantity=5, last_restocked=date(2023, 2, 1))
stock3 = Stock(pet_id=pet3.id, supplier_id=supplier3.id, quantity=8, last_restocked=date(2023, 3, 1))
stock4 = Stock(pet_id=pet4.id, supplier_id=supplier4.id, quantity=15, last_restocked=date(2023, 4, 1))

# Test Data for Attendance
attendance1 = Attendance(event_id=None, customer_id=customer1.id)
attendance2 = Attendance(event_id=None, customer_id=customer2.id)
attendance3 = Attendance(event_id=None, customer_id=customer3.id)
attendance4 = Attendance(event_id=None, customer_id=customer4.id)

# Test Data for Event
event1 = Event(name='Adoption Day', date=date(2023, 5, 20), location='Community Hall')
event2 = Event(name='Pet Parade', date=date(2023, 6, 25), location='Downtown Square')
event3 = Event(name='Vet Check-up', date=date(2023, 7, 10), location='Pet Shop Clinic')
event4 = Event(name='Grooming Workshop', date=date(2023, 8, 15), location='Main Store')

# Test Data for Staff
staff1 = Staff(name='John Doe', role='Manager', hire_date=date(2021, 1, 10), salary=40000)
staff2 = Staff(name='Jane Smith', role='Groomer', hire_date=date(2022, 5, 15), salary=30000)
staff3 = Staff(name='Emily Davis', role='Veterinarian', hire_date=date(2023, 2, 20), salary=50000)
staff4 = Staff(name='Tom Brown', role='Cashier', hire_date=date(2023, 6, 25), salary=25000)

# Test Data for Schedule
schedule1 = Schedule(staff_id=staff1.id, shift_date=date(2023, 9, 20), start_time=datetime(2023, 9, 20, 9, 0), end_time=datetime(2023, 9, 20, 17, 0))
schedule2 = Schedule(staff_id=staff2.id, shift_date=date(2023, 9, 21), start_time=datetime(2023, 9, 21, 9, 0), end_time=datetime(2023, 9, 21, 17, 0))
schedule3 = Schedule(staff_id=staff3.id, shift_date=date(2023, 9, 22), start_time=datetime(2023, 9, 22, 9, 0), end_time=datetime(2023, 9, 22, 17, 0))
schedule4 = Schedule(staff_id=staff4.id, shift_date=date(2023, 9, 23), start_time=datetime(2023, 9, 23, 9, 0), end_time=datetime(2023, 9, 23, 17, 0))

# Test Data for Appointment
appointment1 = Appointment(customer_id=customer1.id, pet_id=pet1.id, appointment_date=date(2023, 10, 5), service_type='Grooming')
apppointment2 = Appointment(customer_id=customer2.id, pet_id=pet2.id, appointment_date=date(2023, 10, 6), service_type='Vet Check-up')
appointment3 = Appointment(customer_id=customer3.id, pet_id=pet3.id, appointment_date=date(2023, 10, 7), service_type='Adoption')
appointment4 = Appointment(customer_id=customer4.id, pet_id=None, appointment_date=date(2023, 10, 8), service_type='Consultation')

# Test Data for Feedback
feedback1 = Feedback(customer_id=customer1.id, staff_id=staff1.id, date_submitted=date(2023, 11, 5), comments='Great service, thank you!')
feedback2 = Feedback(customer_id=customer2.id, staff_id=staff2.id, date_submitted=date(2023, 11, 6), comments='Excellent grooming!')
feedback3 = Feedback(customer_id=customer3.id, staff_id=staff3.id, date_submitted=date(2023, 11, 7), comments='Very knowledgeable vet.')
feedback4 = Feedback(customer_id=customer4.id, staff_id=staff4.id, date_submitted=date(2023, 11, 8), comments='Fast checkout.')


session.add_all([customer1, customer2, customer3, customer4, pet1, pet2, pet3, pet4, order1, order2, order3, order4, order_item1, order_item2, order_item3, order_item4, supplier1, supplier2, supplier3, supplier4, stock1, stock2, stock3, stock4, attendance1, attendance2, attendance3, attendance4, event1, event2, event3, event4, staff1, staff2, staff3, staff4, schedule1, schedule2, schedule3, schedule4, appointment1, apppointment2, appointment3, appointment4, feedback1, feedback2, feedback3, feedback4])
session.commit()
