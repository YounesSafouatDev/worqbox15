# -*- coding: utf-8 -*-
{
    'name': "worqbox_website_sale_custom",

    'summary': """
        Customized E-Commerce for Worqbox
    """,

    'description': """
        Customized E-Commerce for Worqbox
        Require Alan Theme
    """,

    'author': "GIE",
    'website': "https://gie.ma",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '15.0.0.0.4',

    # any module necessary for this one to work correctly
    'depends': [
        'theme_alan',
        'worqbox_sale_default_uom',
        'worqbox_product_attr',
        'website_sale_categ_videos',
    ],

    # always loaded
    'data': [
        # DATAS
        'data/author_blog_template.xml',
        'data/mail_template_data.xml',
        'data/sale_data.xml',
        'data/add_to_cart.xml',

        # Views
        'views/product_banner.xml',
        'views/website_sale_product.xml',
        'views/website_sale_products.xml',
        'views/quick_view.xml',
        'views/cart_view.xml',
        'views/blog_view.xml',
        'views/res_company_views.xml',
        'views/res_config_settings_views.xml',
        'views/sidebar_blog_follow_us.xml',
        'views/website_wishlist_product.xml',

        # Shop views
        'views/shop/quick_view.xml',

        'views/website_sale_templates.xml',
    ],

    'assets': {
        'web.assets_frontend': [
            'worqbox_website_sale_custom/static/src/scss/style.scss',
            'worqbox_website_sale_custom/static/src/scss/shop.scss',
            'worqbox_website_sale_custom/static/src/css/share_btn.css',

            'worqbox_website_sale_custom/static/src/js/website_sale.js',
            'worqbox_website_sale_custom/static/src/js/website_categ_menu.js',
        ],
    },
}
