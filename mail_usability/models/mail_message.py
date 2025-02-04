# Copyright 2019 Akretion France (http://www.akretion.com)
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class MailMessage(models.Model):
    _inherit = 'mail.message'

    @property
    def record_id(self):
        # we do not use a reference field here as mail message
        # are used everywhere and many model are not yet loaded
        # so odoo raise exception
        if self:
            self.ensure_one()
            return self.env[self.model].browse(self.res_id)
        return None
