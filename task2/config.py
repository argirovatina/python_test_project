import random
import yaml
import logger_module

USER_CREDS = {
    'login': 'bot1@qa.qa',
    'pass': 'q1w2e3r4t5'
}
test_data = yaml.load(open("test_data.yaml", 'r'))
uid = 0  # complex hash function