import json
import os

from gaas.config import (GAAS_CREDENTIAL_LOCATION, GAAS_CREDENTIAL_REPOSITORY,
                         GIRHUB_TOKEN_ENV_ID, KAGGLE_KEY_ENV_ID,
                         KAGGLE_USERNAME_ENV_ID)
from gaas.utils.kaggle import KaggleCredential

from github.MainClass import Github


def get_kaggle_credential() -> KaggleCredential:
    if KAGGLE_USERNAME_ENV_ID in os.environ and KAGGLE_KEY_ENV_ID in os.environ:
        return KaggleCredential(os.environ[KAGGLE_USERNAME_ENV_ID],
                                os.environ[KAGGLE_KEY_ENV_ID])
    elif GIRHUB_TOKEN_ENV_ID in os.environ:
        return get_kaggle_credential_from_secret_repository(
            GAAS_CREDENTIAL_REPOSITORY, GAAS_CREDENTIAL_LOCATION,
            os.environ[GIRHUB_TOKEN_ENV_ID])
    else:
        raise RuntimeError('{GIRHUB_TOKEN_ENV_ID} not found.'.format(
            GIRHUB_TOKEN_ENV_ID=GIRHUB_TOKEN_ENV_ID))


def get_kaggle_credential_from_secret_repository(
        repository: str, location: str, gh_token: str) -> KaggleCredential:
    gh = Github(gh_token)
    cred_repo = gh.get_repo(repository)
    kaggle_cred_res = cred_repo.get_contents(location)
    kaggle_cred = json.loads(kaggle_cred_res.decoded_content)
    if 'key' not in kaggle_cred or 'username' not in kaggle_cred:
        raise RuntimeError('Cannot find username or key in kaggle.json file.')
    kaggle_username = kaggle_cred['username']
    kaggle_key = kaggle_cred['key']
    ret_cred = KaggleCredential(kaggle_username, kaggle_key)
    return ret_cred
