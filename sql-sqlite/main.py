from db_setup import Base, engine, SessionLocal
from models import User, Order

# Create tables
Base.metadata.create_all(bind=engine)

# Insert some test data
db = SessionLocal()
user1 = User(name="Alice", email="alice@example.com")
user2 = User(name="Bob", email="bob@example.com")

db.add_all([user1, user2])
db.commit()

order1 = Order(product="Laptop", user_id=user1.id)
order2 = Order(product="Phone", user_id=user1.id)
db.add_all([order1, order2])
db.commit()

# Query
users = db.query(User).all()
for u in users:
    print(u.name, [o.product for o in u.orders])

db.close()
