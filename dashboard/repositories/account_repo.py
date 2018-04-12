from dashboard.models import *
from .repo import Repo


class AccountRepo(Repo):
    def __init__(self):
        super().__init__(Account)

    def get_educator_accounts(self, educator):
        accounts = self._model.objects.raw('''
        SELECT `dashboard_account`.`id`, `dashboard_account`.`name`, `dashboard_account`.`logo`, 
        `dashboard_educatoraccount`.`url`
        FROM `dashboard_account` 
        LEFT OUTER JOIN `dashboard_educatoraccount` ON 
        (`dashboard_account`.`id` = `dashboard_educatoraccount`.`account_id` and
        `dashboard_educatoraccount`.`educator_id` = %s) 
        ''', [educator])

        return accounts
