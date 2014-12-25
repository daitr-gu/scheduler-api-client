"""
Scheduler Partner interface (v2 extension).
"""
from novaclient import base
# from novaclient.openstack.common.gettextutils import _
from novaclient.i18n import _
from novaclient import utils

class SchedulerPartner(base.Resource):
    def __repr__(self):
        return self.scheduler_partner


class SchedulerPartnerManager(base.Manager):
	resource_class = SchedulerPartner

	def create(self, ourId, body):
		return self._create("/os-scheduler-partner/%s/provision" % ourId, body, 'scheduler_partner', True)

	def estimate(self, ourId, body):
		return self._create("/os-scheduler-partner/%s/estimate" % ourId, body, 'scheduler_partner', True)