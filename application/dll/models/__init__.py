from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, DATE, Text, Date, Float, CHAR
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship
from application.dll.db.db import Base


class Storage(Base):
    __tablename__ = "Storage"

    idstorage = Column(Integer, primary_key=True, autoincrement=True)
    adress = Column(String(45), nullable=False, unique=True)
    zipcode = Column(String(45), nullable=False)
    city = Column(String(45), nullable=False)
    state = Column(String(45), nullable=False)
    country = Column(String(45), nullable=False)

    office = relationship("Office", back_populates="storage")
    product_stored = relationship('ProductStored', back_populates='storage')

    def __repr__(self):
        return f"{self.country}, {self.state}, {self.city}, {self.zipcode}, {self.adress}"


class Office(Base):
    __tablename__ = 'offices'

    idoffices = Column(Integer, primary_key=True, autoincrement=True)
    office_name = Column(String(45), nullable=False, unique=True)
    city = Column(String(100), nullable=False)
    phone_number = Column(String(45), nullable=False)
    adress = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)
    zipcode = Column(Integer, nullable=False)
    Storage_idOffice_storage = Column(ForeignKey('Storage.idstorage'), nullable=False)

    storage = relationship("Storage", back_populates='office')
    employees = relationship("Employee", back_populates="office")

    def __repr__(self):
        return f'{self.office_name} {self.city} {self.phone_number}, {self.adress}, {self.state}, {self.country}, {self.zipcode}'


class Employee(Base):
    __tablename__ = 'Employees'

    idEmployees = Column(Integer, primary_key=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(45), nullable=False)
    Jobtitle = Column(String(45))
    offices_idoffices = Column(Integer, ForeignKey('offices.idoffices'), nullable=False)

    office = relationship("Office", back_populates="employees")
    customers = relationship('Customer', back_populates='employees')

    def __repr__(self):
        return f'{self.first_name} {self.last_name}, {self.email}, {self.phone}, {self.Jobtitle}'


class CarInfo(Base):
    __tablename__ = 'Carinfo'

    idCarinfo = Column(Integer, primary_key=True)
    reg_number = Column(String(15), nullable=False)
    manufacture_name = Column(String(45), nullable=False)
    model = Column(String(45), nullable=False)
    year_model = Column(DateTime, nullable=False)
    color = Column(String(45), nullable=False)
    Customers_idCustomers = Column(Integer, ForeignKey('Customers.idCustomers'))

    customers = relationship('Customer', back_populates='car_info')

    def __repr__(self):
        return f'{self.reg_number}, {self.manufacture_name}, {self.model}, {self.year_model}, {self.color}'


class Company(Base):
    __tablename__ = 'Company'

    idContactPersons = Column(Integer, primary_key=True)
    company_name = Column(String(45), nullable=False)
    phone_number = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False)

    company_contact_employees = relationship('CompanyContactEmployee', back_populates='companies')
    customers = relationship('Customer', back_populates='companies')

    def __repr__(self):
        return f'{self.company_name}, {self.phone_number}, {self.email}'


class CompanyContactEmployee(Base):
    __tablename__ = 'company_contact_employees'

    idcompany_contact_employees = Column(Integer, primary_key=True, autoincrement=True)
    Company_idContactPersons = Column(Integer, ForeignKey('Company.idContactPersons'))
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    phone = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False)

    companies = relationship('Company', back_populates='company_contact_employees')

    def __repr__(self):
        return f'{self.first_name}, {self.last_name}, {self.phone}, {self.email}'


class CarModel(Base):
    __tablename__ = 'component_model'

    idcomponent_model = Column(Integer, primary_key=True)
    car_brand = Column(String(45), nullable=False)
    car_model = Column(String(45), nullable=False)
    car_model_year = Column(DateTime, nullable=True)

    product = relationship('Product', back_populates='component_model')

    def __repr__(self):
        return f'{self.car_brand}, {self.car_model}, {self.car_model_year}'


class PrivatePerson(Base):
    __tablename__ = 'private_person'

    idprivate_person = Column(Integer, primary_key=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    phone = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False)

    customers = relationship('Customer', back_populates='private_persons')

    def __repr__(self):
        return f'{self.idprivate_person}, {self.first_name}, {self.last_name}, {self.phone}, {self.email}'


class Customer(Base):
    __tablename__ = 'Customers'

    idCustomers = Column(Integer, primary_key=True)
    created = Column(DATE, nullable=False)
    private_person_or_company = Column(TINYINT, nullable=False)
    Company_idContactPersons = Column(Integer, ForeignKey('Company.idContactPersons'))
    Employees_idEmployees = Column(Integer, ForeignKey('Employees.idEmployees'))
    private_person_idprivate_person = Column(Integer, ForeignKey('private_person.idprivate_person'))
    delivery_adress_iddelivery_adress = Column(Integer, ForeignKey('delivery_adress.iddelivery_adress'))

    delivery_addresses = relationship('DeliveryAdress', back_populates='customers')
    companies = relationship('Company', back_populates='customers')
    orders = relationship('Order', back_populates='customers')
    private_persons = relationship('PrivatePerson', back_populates='customers')
    car_info = relationship('CarInfo', back_populates='customers')
    employees = relationship('Employee', back_populates='customers')

    def __repr__(self):
        return f'{self.customer_id}, {self.created}'


class DeliveryAdress(Base):
    __tablename__ = 'delivery_adress'

    iddelivery_adress = Column(Integer, primary_key=True)
    country = Column(String(45), nullable=False)
    city = Column(String(45), nullable=False)
    state = Column(String(45), nullable=False)
    zipcode = Column(String(45), nullable=False)
    adress = Column(String(45), nullable=False)

    customers = relationship('Customer', back_populates='delivery_addresses')

    def __repr__(self):
        return f'{self.country} {self.city}, {self.state}, {self.zipcode}, {self.adress}'


class ManufactureContactPerson(Base):
    __tablename__ = 'Manufactures_contact_person'

    idManufactures_contact_person = Column(Integer, primary_key=True)
    phone_number = Column(String(45), nullable=False, unique=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    email = Column(String(100), nullable=False, unique=True)

    Manufactures_idManufactures = Column(Integer, ForeignKey('Manufactures.idManufactures'))
    manufactures = relationship('Manufacture', back_populates='contact_person')

    def __repr__(self):
        return f'{self.idManufactures_contact_person},{self.phone_number}, {self.first_name}, {self.last_name}, {self.email}'


class ManufactureOffice(Base):
    __tablename__ = 'Manufactures_offices'

    idManufactures_offices = Column(Integer, primary_key=True)
    phone = Column(String(45), nullable=False, unique=True)
    adress = Column(String(45), nullable=False)
    country = Column(String(45), nullable=False)
    zipcode = Column(String(45), nullable=False)
    state = Column(String(45), nullable=False)
    Manufactures_idManufactures = Column(Integer, ForeignKey('Manufactures.idManufactures'))

    manufactures = relationship('Manufacture', back_populates='office')

    def __repr__(self):
        return f'{self.idManufactures_offices},{self.phone}, {self.adress}, {self.country}, {self.zipcode}, {self.state}'


class Order(Base):
    __tablename__ = 'Orders'

    idOrders = Column(Integer, primary_key=True)
    Customers_idCustomers = Column(Integer, ForeignKey('Customers.idCustomers'), primary_key=True)
    purchase_date = Column(DateTime, nullable=False)
    requireddate = Column(Date)
    shippeddate = Column(Date)
    status = Column(String(45), nullable=False)
    comments = Column(Text)

    customers = relationship('Customer', back_populates='orders')
    orderdetails = relationship('Orderdetail', back_populates='orders')

    def __repr__(self):
        return f'{self.purchase_date} {self.requireddate}, {self.shippeddate}, {self.status}, {self.comments}'


class Orderdetail(Base):
    __tablename__ = 'Orderdetails'

    idOrderdetails = Column(Integer, primary_key=True)
    product_number = Column(String(45), nullable=False)
    quantityordered = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    Orders_idOrders = Column(Integer, ForeignKey('Orders.idOrders'), nullable=False)
    Orders_Customers_idCustomers = Column(Integer, ForeignKey('Orders.Customers.idCustomers'), nullable=False)

    orders = relationship('Order', back_populates='orderdetails')

    def __repr__(self):
        return f'{self.product_number} {self.quantityordered}, {self.price}'


class ProductHasManufacture(Base):
    __tablename__ = 'Products_has_Manufactures'

    Product_idProducts = Column(Integer, ForeignKey('Product.idProducts'), primary_key=True)
    Manufactures_idManufactures = Column(Integer, ForeignKey('Manufactures.idManufactures'), primary_key=True)
    purchase_price = Column(Float, nullable=False)
    quality_rating = Column(Integer, nullable=True)

    #manufactures = relationship('Manufacture', back_populates='product_has_manufacture')
    #product = relationship('Product', back_populates='product_has_manufacture')


class Product(Base):
    __tablename__ = 'Products'

    idProducts = Column(Integer, primary_key=True)
    product_name = Column(String(100), nullable=False)
    product_number = Column(CHAR(10), nullable=False, unique=True)
    description = Column(String(500), nullable=True)
    sell_price = Column(Float, nullable=False)
    product_stored_idproduct_stored = Column(Integer, ForeignKey('product_stored.idproduct_stored'))
    component_model_idcomponent_model = Column(Integer, ForeignKey('component_model.idcomponent_model'))

    product_stored = relationship('ProductStored', back_populates='product')
    component_model = relationship('CarModel', back_populates='product')
    suppliers = relationship('Supplier', back_populates='product')
    #product_has_manufacture = relationship('ProductHasManufacture', back_populates='product')

    def __repr__(self):
        return f'{self.idProducts},{self.product_name}, {self.product_number}, {self.description}, {self.sell_price}'


class Manufacture(Base):
    __tablename__ = 'Manufactures'

    idManufactures = Column(Integer, primary_key=True)
    company_name = Column(String(45), nullable=False, unique=True)
    number_head_office = Column(Integer, nullable=True)

    #product_has_manufacture = relationship('ProductHasManufacture', back_populates='manufactures')
    contact_person = relationship('ManufactureContactPerson', back_populates='manufactures')
    office = relationship('ManufactureOffice', back_populates='manufactures')

    def __repr__(self):
        return f'{self.idManufactures},{self.company_name}, {self.number_head_office}'


class ProductStored(Base):
    __tablename__ = "product_stored"

    idproduct_stored = Column(Integer, primary_key=True)
    product_stored = Column(Integer)
    product_min_limit = Column(Integer)
    products_max_limit = Column(Integer)
    storage_idstorage = Column(Integer, ForeignKey("Storage.idstorage"), nullable=False)

    storage = relationship("Storage", back_populates="product_stored")
    product = relationship("Product", back_populates="product_stored")

    def __repr__(self):
        return f"{self.product_stored}, limit {self.product_min_limit} {self.product_max_limit}"


class SupplierContactPerson(Base):
    __tablename__ = 'Supplier_contactperson'

    idSupplier_contactperson = Column(Integer, primary_key=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    phone = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False)

    Suppliers_idSuppliers = Column(Integer, ForeignKey('Suppliers.idSuppliers'))
    suppliers = relationship('Supplier', back_populates='supplier_contact_person')

    def __repr__(self):
        return f'{self.idSupplier_contactperson},{self.first_name}, {self.last_name}, {self.phone}, {self.email}'


class Supplier(Base):
    __tablename__ = 'Suppliers'

    idSuppliers = Column(Integer, primary_key=True)
    company_name = Column(String(45), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(45), nullable=False)
    country = Column(String(45), nullable=False)
    zipcode = Column(String(45), nullable=False)
    city = Column(String(45), nullable=False)
    adress = Column(String(100), nullable=False)

    Products_idProducts = Column(Integer, ForeignKey('Products.idProducts'))

    product = relationship('Product', back_populates='suppliers')
    supplier_contact_person = relationship('SupplierContactPerson', back_populates='suppliers')

    def __repr__(self):
        return f'{self.idSuppliers},{self.company_name}, {self.email}, {self.phone}, {self.country} {self.zipcode}, {self.adress}'

