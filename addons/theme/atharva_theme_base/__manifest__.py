# -*- coding: utf-8 -*-
{
    'name': 'Worqbox Atharva Theme Base',
    'category': 'Base',
    'summary': 'Base module for Atharva E-commerce themes',
    'version': '2.0.2.1',
    'license': 'OPL-1',
    'author': 'Atharva System',
	'support': 'support@atharvasystem.com',
    'website' : 'https://www.atharvasystem.com',
	'description': """
        Base module for Atharva E-commerce themes
        
        <h3>Modified version</h3>
        <ul>
            <li>Removed Product brand views</li>
            <li>Removed Product extra info views</li>
            <li>Moved E-Commerce product attribs in a new tab</li>
        </ul>
    """,
    'depends': [
        'website_sale',
        'website_sale_wishlist',
        'website_sale_comparison',
        'website_blog',
        'stock'
    ],
    'data': [
        'security/ir.model.access.csv',
        # VIEWS
        'views/admin/product_ecom_views.xml',
        'views/admin/product_tags.xml',
        'views/admin/product_label.xml',
        'views/admin/product_tab.xml',
        'views/admin/document_tab.xml',
        'views/admin/faqs_views.xml',
        # 'views/admin/product_brand.xml',
        'views/admin/menu_tag.xml',
        'views/admin/pwa.xml',
        # 'views/admin/product_info.xml',
        'views/admin/countdown_view.xml',
        'views/megamenus/templates.xml',
        'views/shop/product_page.xml',
        'views/shop/shop_page.xml',
        'views/shop/shop_filter.xml',
        'views/shop/quick_view.xml',
        'views/pwa/template.xml',
        'views/header_footer/footer.xml',
        'views/header_footer/header.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'atharva_theme_base/static/src/lib/swiper-bundle.min.css',
            'atharva_theme_base/static/src/lib/swiper-bundle.min.js',
            'atharva_theme_base/static/src/lib/jquery.magnific-popup.min.js',
            'atharva_theme_base/static/src/lib/magnific-popup.css',
            'atharva_theme_base/static/src/js/lazy_load.js',
            'atharva_theme_base/static/src/js/pwa_config.js',
        ],
    },
    'price': 4.00,
    'currency': 'EUR',
    'images': ['static/description/as-theme-base.png'],
    'installable': True,
    'application': True
}
