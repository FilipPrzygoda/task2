from project import db, app


# Customer model
class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    city = db.Column(db.String(64))
    age = db.Column(db.Integer)
    pesel = db.Column(db.String(64))
    street = db.Column(db.String(128))
    appNo = db.Column(db.String(10))

    def __init__(self, name, city, age, pesel, street, appNo):
        self.name = name
        self.city = city
        self.age = age
        self.pesel = pesel
        self.street = street
        self.appNo = appNo
        print("Getting: " + str(self),flush=True)

    def __repr__(self):
        name = "*****" if self.name else "Empty or Invalid"
        city = "*****" if self.city else "Empty or Invalid"
        pesel = "*****" if self.pesel and len(str(self.pesel)) == 11 and str(self.pesel).isdigit() else "Empty or Invalid"
        street = "*****" if self.street else "Empty or Invalid"
        appNo = "*****" if self.appNo else "Empty or Invalid"
        return f"Customer(ID: {self.id}, Name: {name}, City: {city}, Age: {self.age}, Pesel: {pesel}, Street: {street}, AppNo: {appNo})"


with app.app_context():
    db.create_all()
