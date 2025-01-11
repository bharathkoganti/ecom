from itsdangerous import URLSafeTimedSerializer
from key import salt
def encode(data):
    serializer=URLSafeTimedSerializer('bharath')
    return serializer.dumps(data,salt=salt)

def decode(data):
    serializer=URLSafeTimedSerializer('bharath')
    return serializer.loads(data,salt=salt)