from database import Base, engine
import user, worksheet, interact, document, item

print('Creating database tables....')
Base.metadata.create_all(bind=engine)
