# -*- coding: utf-8 -*-
{
    'name': "worqbox_multi_company",

    'summary': """Multi-company related addons""",

    'description': """
        1 - Install the related OCA multicompany addons
        2 - Action-server for updating the existing records
        3 - Per company CRM stages
    """,

    'author': "GIE",
    'website': "https://gie.ma",

    'category': 'Worqbox',
    'version': '15.0.0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'base_multi_company',
        'product_multi_company',
        'partner_multi_company',
        'worqbox_crm_stage_multi_company',
    ],

    # always loaded
    'data': [
        'data/action_data.xml',
        'views/product_template_views.xml',
    ],
    "post_init_hook": "post_init_hook",
}
