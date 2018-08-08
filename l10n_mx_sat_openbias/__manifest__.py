# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "l10n_mx_sat_openbias",
    'summary': "Catálogo contable SAT", 
    'description': 
    """
        Catálogo contable conestructura SAT
    """,
    'author': "openBias",
    'website': "https://www.bias.com.mx",
    'category': 'Localization',
    'auto_install': True,
    'version': '0.2',
    'depends': [
        'account_accountant',
        'sales_team',
        'bias_base_report',
        'base_vat_mx',
        'contabilidad_electronica',
        'bias_coa_hierarchy',
        'account_tax_cash_basis_extended',
        'cfd_mx',
        'validar_facturas',
        'currency_rate_update',
    ],
    'data': [
        'data/data_account_type.xml',
        'data/l10n_mx_chart_data.xml',
        'data/account_tax_data.xml',
        'data/account_chart_template_data.yml',
    ],
}
