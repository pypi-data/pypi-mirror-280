from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher():
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password):
        return pwd_context.hash(password)
    

# Assuming Hasher is a class and get_password_hash is a static method
if __name__ == "__main__":
    hashed_password = Hasher.get_password_hash("APIUser2024&")
    print(hashed_password)