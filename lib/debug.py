from models.__init__ import CONN, CURSOR
import ipdb


ipdb.set_trace()

from models import Session, User

session = Session()

new_user = User(username="mariam", email="mariam@example.com")
session.add(new_user)
session.commit()

print("User created:", new_user)
