import os
from dotenv import load_dotenv


# load env
load_dotenv('local_test/utils/configs/.env')

# secrets
secret = os.getenv('secret')
