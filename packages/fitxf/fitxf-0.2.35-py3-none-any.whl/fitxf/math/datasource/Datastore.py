import logging
import re
import os
from fitxf.math.datasource.DatastoreInterface import DbParams
from fitxf.math.datasource.Csv import Csv
from fitxf.math.utils.Env import Env
from fitxf.math.utils.Logging import Logging


class Datastore:

    def __init__(
            self,
            db_params: DbParams,
            logger = None,
    ):
        self.db_params = db_params
        assert type(self.db_params) is DbParams, 'Wrong type for db_params "' + str(type(self.db_params)) + '"'
        self.logger = logger if logger is not None else logging.getLogger()
        return

    def get_data_store(
            self,
    ):
        if self.db_params.db_type == 'csv':
            assert not re.match(pattern="/", string=self.db_params.db_table), \
                'Must not contain full path in table name or index "' + str(self.db_params.db_table) + '"'
            return Csv(
                db_params = self.db_params,
                logger = self.logger,
            )
        else:
            raise Exception('Not supported data store type "' + str(self.db_params.db_type) + '"')


if __name__ == '__main__':
    Env.set_env_vars_from_file(env_filepath=os.environ["REPO_DIR"] + '/.env.nwae.math')
    dbp = DbParams(
        identifier = 'test set',
        db_type   = os.environ["DB_TYPE"],
        db_host   = os.environ["DB_HOST"],
        db_port   = os.environ["DB_PORT"],
        db_scheme = os.environ["DB_SCHEME"],
        db_username = os.environ["DB_USERNAME"],
        db_password = os.environ["DB_PASSWORD"],
        db_verify_certs = os.environ["VERIFY_CERTS"],
        params_other ={'ignore_warnings': True},
        logger = Logging.get_default_logger(log_level=logging.INFO, propagate=False),
    )
    db = Datastore(db_params=dbp)
    db.get_data_store()
    exit(0)
