"""
Scheduler Partner interface (v2 extension).
"""
from novaclient import base
from novaclient.openstack.common.gettextutils import _
from novaclient import utils

class SchedulerPartner(base.Resource):
    def __repr__(self):
        return "<SchedulerPartner: %s>" % self.name


class SchedulerPartnerManager(base.Manager):
	resource_class = SchedulerPartner

	def create(self, body):
		return self._create('/os-scheduler-partner', body, 'scheduler_partner')