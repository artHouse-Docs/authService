import os

import dotenv
import redis

from auth import auth_pb2_grpc
from auth import auth_pb2

from utils.jwt import generate_token, decode_token

dotenv.load_dotenv()

r = redis.Redis(host='localhost', port=6379, decode_responses=True)


class AuthService(auth_pb2_grpc.AuthServiceServicer):
    def Login(self, request, context):
        access_token, refresh_token = generate_token(request.id)
        r.set(refresh_token, request.id)
        return auth_pb2.JWTToken(
            access_token=access_token,
            refresh_token=refresh_token
        )

    def Refresh(self, request, context):
        try:
            user_id = decode_token(request.refresh_token)['id']
        except:
            return auth_pb2.JWTToken(
                access_token=None,
                refresh_token=None
            )
        access_token, refresh_token = generate_token(user_id)
        r.set(refresh_token, user_id)
        return auth_pb2.JWTToken(
            access_token=access_token,
            refresh_token=refresh_token
        )

    def CheckToken(self, request, context):
        try:
            user_id = decode_token(request.access_token)['id']
        except:
            return auth_pb2.Payload(id=None)
        return auth_pb2.Payload(id=user_id)
