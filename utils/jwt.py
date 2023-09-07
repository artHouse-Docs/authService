import os
from datetime import *
import jwt
import dotenv

dotenv.load_dotenv()


def generate_token(user_id):
    payload = lambda data, exp: {
        'id': data,
        'exp': datetime.utcnow() + exp,
    }
    return [
        jwt.encode(payload(user_id, timedelta(seconds=120)), os.getenv('JWT_SECRET'), algorithm='HS256'),
        jwt.encode(payload(user_id, timedelta(days=10)), os.getenv('JWT_SECRET'), algorithm='HS256'),
    ]


def decode_token(token):
    try:
        return jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise "Token expired"
    except jwt.DecodeError:
        raise "Token invalid"
    except jwt.InvalidTokenError:
        raise "Token invalid"
