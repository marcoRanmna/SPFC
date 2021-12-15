from application.view.mongo.base_document import Document, db


class Company(Document):
    collection = db.Company


class Customer(Document):
    collection = db.Customers


class Manufacture(Document):
    collection = db.Manufactures


class Order(Document):
    collection = db.Orders


class Product(Document):
    collection = db.Products


class Supplier(Document):
    collection = db.Suppliers


class Storage(Document):
    collection = db.Storage
