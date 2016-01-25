# -*- coding: utf-8 -*-
##############################################################################
#
#    Account Bank Statement Import Usability module for Odoo
#    Copyright (C) 2015 Akretion (http://www.akretion.com)
#    @author Alexis de Lattre <alexis.delattre@akretion.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, api


class AccountBankStatementImport(models.TransientModel):
    """Extend model account.bank.statement."""
    _inherit = 'account.bank.statement.import'

    @api.model
    def _find_bank_account_id(self, account_number):
        """Compared to the code in the module account_bank_statement_import,
        this code:
        - works when the account_number is not a complete IBAN,
          but just an account number (most statement files only have the
          account number)
        - works if you have 2 bank accounts with the same number
          (I have seen that at Crédit du Nord: the company had 1 account in USD
          and 1 account in EUR with the same number !)
          -> for that, I filter on the journal if the journal_id field is set
          """
        bank_account_id = None
        if account_number and len(account_number) > 4:
            if self.journal_id:
                self._cr.execute("""
                    SELECT id FROM res_partner_bank
                    WHERE replace(replace(acc_number,' ',''),'-','') like %s
                    AND journal_id=%s
                    ORDER BY id
                    """, ('%' + account_number + '%', self.journal_id.id))
            else:
                self._cr.execute("""
                    SELECT id FROM res_partner_bank
                    WHERE replace(replace(acc_number,' ',''),'-','') like %s
                    AND journal_id is not null
                    ORDER BY id
                    """, ('%' + account_number + '%', ))
            bank_account_ids = [id[0] for id in self._cr.fetchall()]
            if bank_account_ids:
                bank_account_id = bank_account_ids[0]
        return bank_account_id
