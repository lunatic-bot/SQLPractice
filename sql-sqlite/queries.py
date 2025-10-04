from db_setup import SessionLocal
from models import User, Order

db = SessionLocal()

# 1. Get all users who ordered "Laptop"
laptop_users = db.query(User).join(Order).filter(Order.product=="Laptop").all()
print([u.name for u in laptop_users])

# 2. Count orders per user
order_counts = db.query(User.name, func.count(Order.id)).join(Order).group_by(User.id).all()
print(order_counts)

db.close()
