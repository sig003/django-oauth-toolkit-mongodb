
import os, json
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured

def getMongoDBConnectHostFile():
    BASE_DIR = Path(__file__).resolve().parent.parent

    secret_file = os.path.join(BASE_DIR, 'secrets.json')
    with open(secret_file) as f:
        secrets = json.loads(f.read())

    def get_secret(setting):
        try:
            return secrets[setting]
        except KeyError:
            error_msg = "Set the {} environment variable".format(setting)
            raise ImproperlyConfigured(error_msg)

    MONGODB_HOST_FILE = get_secret("MONGODB_HOST")

    return MONGODB_HOST_FILE