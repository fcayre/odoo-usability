# -*- encoding: utf-8 -*-
##############################################################################
#
#    Product Manager Group Stock module for OpenERP
#    Copyright (C) 2014 Akretion (http://www.akretion.com)
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


{
    'name': 'Product Manager Group Stock',
    'version': '0.1',
    'category': 'Hidden',
    'license': 'AGPL-3',
    'summary': 'Extend the group Product Manager to Stock',
    'description': """
Product Manager Group Stock
===========================

Extends the group Product Manager to Stock Management.

Please contact Alexis de Lattre from Akretion <alexis.delattre@akretion.com> for any help or question about this module.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['product_manager_group', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        ],
    'active': False,
    'installable': False,
}
