from jwt import encode, decode

class Utils:
    """ Utils docs """
    def __init__(self):
        super(Utils, self).__init__()

    def create_token(self, data: dict) -> str:
        return encode(payload=data, key="my_secret_key", algorithm="HS256")

    def validate_token(self, token: str) -> dict:
        return decode(token, key="my_secret_key", algorithms=['HS256'])