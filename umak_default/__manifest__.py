# -----------------------------------------------------------------------------------
#
#    Copyright (C) 2022 jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
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
# -----------------------------------------------------------------------------------
{
    "name": "umak",
    "version": "17.0.1.0.0",
    "license": "Other OSI approved licence",
    "category": "Tools",
    "summary": "Customización umak",
    "author": "jeo Software",
    "depends": [
    ],
    "data": [],
    "test": [],
    "installable": True,
    "application": True,

    # Here begins odoo-env manifest configuration
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # manifest version, if omitted it is backward compatible
    "env-ver": "2",
    # if Enterprise it installs in a different directory than community
    "odoo-license": "EE",
    # port where odoo starts serving pages
    "port": "8069",
    # settins for config files
    "config": [],
    "config_local": [],
    # list of url repos to install in the form 'repo-url directory'
    "git-repos": [
        "https://github.com/jobiols/cl-umak.git -b 17.0",
        # ingadhoc
        # Para el caso de la 17 y 18 adhoc tiene modificaciones que todavia no se pudieron mezclar en oca
        "https://github.com/ingadhoc/account-financial-tools.git sub_l10n-ar/account-financial-tools"
        "https://github.com/ingadhoc/account-payment.git sub_l10n-ar/account-payment"
        "https://github.com/ingadhoc/odoo-argentina.git sub_l10n-ar/odoo-argentina"
        "https://github.com/ingadhoc/argentina-sale.git sub_l10n-ar/argentina-sale"
        "https://github.com/ingadhoc/account-invoicing.git sub_l10n-ar/account-invoicing"
        "https://github.com/ingadhoc/odoo-argentina-ee.git sub_l10n-ar/odoo-argentina-ee"
        "https://github.com/ingadhoc/stock.git sub_l10n-ar/stock"
        "https://github.com/ingadhoc/aeroo_reports.git sub_l10n-ar/aeroo_reports"

        "https://github.com/adhoc-cicd/oca-server-tools sub_l10n-ar/oca-server-tools"
        "https://github.com/adhoc-cicd/oca-stock-logistics-workflow.git sub_l10n-ar/oca-stock-logistics-workflow"
        "https://github.com/adhoc-cicd/oca-web.git sub_l10n-ar/oca-web"

    ],
    # list of images to use in the form 'name image-url'
    "docker-images": [
        "odoo jobiols/odoo-ent:17.0e",
        "postgres postgres:14.15-alpine",
    ],
}
