##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2023 Ricardo Pico Ochandategui
#    (<http://www.marlonfalcon.com>).
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
    'name': 'Module RPO',
    'version': '1.1',
    'author': 'Ricardo Pico Ochandategui',
    'maintainer': 'Ricardo Pico Ochandategui',
    'license': 'AGPL-3',
    'category': 'Extra Tools',
    'summary': 'Set Sale Report.',
    'depends': ['base', 'sale_management'],
    'data': [
        'reports/set_sale_report.xml',
    ],
    'images': ['static/description/banner.png'],
}
