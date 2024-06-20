from euphorie.client.model import Session as EuphorieSession
from oira.statistics.tools.update import UpdateStatisticsDatabases
from osha.oira.statistics.model import get_postgres_url
from Products.Five import BrowserView

import logging


logger = logging.getLogger(__name__)


class UpdateStatistics(BrowserView):
    def get_postgres_url(self):
        return get_postgres_url()

    def __call__(self):
        logger.info("Updating statistics databases")
        postgres_url = self.get_postgres_url()
        if postgres_url is None:
            return "Could not get postgres connection URL!"
        update_db = UpdateStatisticsDatabases(EuphorieSession, postgres_url)
        update_db()
        logger.info("Done")
        return "Done"
