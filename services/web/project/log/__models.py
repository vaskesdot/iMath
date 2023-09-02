# import datetime

# from sqlalchemy.orm import relationship

# from project.__init__ import db


# class Brand(db.Model):
#     __tablename__ = "brands"

#     id = db.Column(db.Integer, primary_key=True, index=True)

#     brand = db.Column(db.String(128), unique=True, nullable=False)

#     sku = relationship("Sku", back_populates="brand")

#     def __init__(self, brand):
#         self.brand = brand

# class Sku(db.Model):
#     __tablename__ = "sku"

#     id = db.Column(db.Integer, primary_key=True, index=True)

#     name = db.Column(db.String(128), unique=True, nullable=False)

#     brand = relationship("Brand", back_populates="sku")
#     brand_id = db.Column(db.Integer, db.ForeignKey("brands.id"))
#     cards = relationship("Card", back_populates="sku")

#     def __init__(self, name):
#         self.name = name


# class Pharmacy(db.Model):
#     __tablename__ = "pharmacies"

#     id = db.Column(db.Integer, primary_key=True, index=True)

#     name = db.Column(db.String(128), unique=True, nullable=False)

#     cards = relationship("Card", back_populates="pharmacy")
#     sites_data = relationship("PharmacySitesData", back_populates="pharmacy")

#     def __init__(self, name):
#         self.name = name

# class PharmacySitesData(db.Model):
#     __tablename__ = "pharmacies_sites_data"

#     id = db.Column(db.Integer, primary_key=True, index=True)

#     comment = db.Column(db.String(5000), unique=False, nullable=True)
#     cookies = db.Column(db.JSON, unique=False, nullable=True)
#     is_cookies_expired_by_401_error = db.Column(db.Boolean, nullable=False)

#     pharmacy_id = db.Column(db.Integer, db.ForeignKey("pharmacies.id"))
#     pharmacy = relationship("Pharmacy", back_populates="sites_data")


#     def __init__(self, comment, cookies=None, is_cookies_expired_by_401_error=None):
#         self.comment = comment
#         self.cookies = cookies
#         self.is_cookies_expired_by_401_error = is_cookies_expired_by_401_error


# class City(db.Model):
#     __tablename__ = "cities"

#     id = db.Column(db.Integer, primary_key=True, index=True)

#     name = db.Column(db.String(128), unique=True, nullable=False)

#     cards = relationship("Card", back_populates="city")

#     def __init__(self, name):
#         self.name = name


# class Card(db.Model):
#     __tablename__ = "cards"

#     id = db.Column(db.Integer, primary_key=True, index=True)

#     url = db.Column(db.String(128), unique=True, nullable=False)
#     could_be_opened_last_status = db.Column(db.Boolean, nullable=True)
#     could_be_opened_last_date = db.Column(db.DateTime, nullable=True)
#     could_be_parsed_last_status = db.Column(db.Boolean, nullable=True)
#     could_be_parsed_last_date = db.Column(db.DateTime, nullable=True)
#     last_price = db.Column(db.Integer, nullable=True)

#     pharmacy_id = db.Column(db.Integer, db.ForeignKey("pharmacies.id"))
#     pharmacy = relationship("Pharmacy", back_populates="cards")
#     sku_id = db.Column(db.Integer, db.ForeignKey("sku.id"))
#     sku = relationship("Sku", back_populates="cards")
#     city_id = db.Column(db.Integer, db.ForeignKey("cities.id"))
#     city = relationship("City", back_populates="cards")
#     snapshots = relationship("Snapshot", back_populates="card")

#     def __init__(self, url):
#         self.url = url

# class Snapshot(db.Model):
#     __tablename__ = "snapshots"

#     id = db.Column(db.Integer, primary_key=True, index=True)
#     price = db.Column(db.Integer, nullable=True)
#     date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
#     was_successful = db.Column(db.Boolean, nullable=True)

#     card_id = db.Column(db.Integer, db.ForeignKey("cards.id"))
#     card = relationship("Card", back_populates="snapshots")

#     def __init__(self, price, date, card_id):
#         self.price = price
#         self.date = date
#         self.card_id = card_id

