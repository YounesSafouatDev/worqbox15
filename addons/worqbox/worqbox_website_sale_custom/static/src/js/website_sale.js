odoo.define('worqbox_website_sale_custom.hauteur_range_option', function (require) {
    'use strict';
    
    const publicWidget = require('web.public.widget');
    
    publicWidget.registry.multirangeHauteurSelector = publicWidget.Widget.extend({
        selector: '#o_wsale_range_hauteur',
        events: {
            'newRangeValue input[type="range"]': '_onHauteurRangeSelected',
        },
    
        //----------------------------------------------------------------------
        // Handlers
        //----------------------------------------------------------------------
    
        /**
         * @private
         * @param {Event} ev
         */
         _onHauteurRangeSelected(ev) {
            const range = ev.currentTarget;
            const search = $.deparam(window.location.search.substring(1));
            delete search.min_hauteur;
            delete search.max_hauteur;
            if (parseFloat(range.min) !== range.valueLow) {
                search['min_hauteur'] = range.valueLow;
            }
            if (parseFloat(range.max) !== range.valueHigh) {
                search['max_hauteur'] = range.valueHigh;
            }
            window.location.search = $.param(search);
        },
    });
});
odoo.define('worqbox_website_sale_custom.profondeur_range_option', function (require) {
    'use strict';
    
    const publicWidget = require('web.public.widget');
    
    publicWidget.registry.multirangeProfondeurSelector = publicWidget.Widget.extend({
        selector: '#o_wsale_range_profondeur',
        events: {
            'newRangeValue input[type="range"]': '_onProfondeurRangeSelected',
        },
    
        //----------------------------------------------------------------------
        // Handlers
        //----------------------------------------------------------------------
    
        /**
         * @private
         * @param {Event} ev
         */
         _onProfondeurRangeSelected(ev) {
            const range = ev.currentTarget;
            const search = $.deparam(window.location.search.substring(1));
            delete search.min_profondeur;
            delete search.max_profondeur;
            if (parseFloat(range.min) !== range.valueLow) {
                search['min_profondeur'] = range.valueLow;
            }
            if (parseFloat(range.max) !== range.valueHigh) {
                search['max_profondeur'] = range.valueHigh;
            }
            window.location.search = $.param(search);
        },
    });
});
odoo.define('worqbox_website_sale_custom.longueur_range_option', function (require) {
    'use strict';
    
    const publicWidget = require('web.public.widget');
    
    publicWidget.registry.multirangeLongueurSelector = publicWidget.Widget.extend({
        selector: '#o_wsale_range_longueur',
        events: {
            'newRangeValue input[type="range"]': '_onLongueurRangeSelected',
        },
    
        //----------------------------------------------------------------------
        // Handlers
        //----------------------------------------------------------------------
    
        /**
         * @private
         * @param {Event} ev
         */
         _onLongueurRangeSelected(ev) {
            const range = ev.currentTarget;
            const search = $.deparam(window.location.search.substring(1));
            delete search.min_longueur;
            delete search.max_longueur;
            if (parseFloat(range.min) !== range.valueLow) {
                search['min_longueur'] = range.valueLow;
            }
            if (parseFloat(range.max) !== range.valueHigh) {
                search['max_longueur'] = range.valueHigh;
            }
            window.location.search = $.param(search);
        },
    });
});

// CHECKBOX FLEXIBLE
odoo.define('worqbox_website_sale_custom.flexible_checkbox', function (require) {
    'use strict';
    
    const publicWidget = require('web.public.widget');
    
    publicWidget.registry.FlexibleSelector = publicWidget.Widget.extend({
        selector: '#products_version',
        events: {
            'change select': '_onChangeSelect',
        },
    
        //----------------------------------------------------------------------
        // Handlers
        //----------------------------------------------------------------------
    
        /**
         * @private
         * @param {Event} ev
         */
         _onChangeSelect(ev) {
            const value = ev.currentTarget.value;
            const search = $.deparam(window.location.search.substring(1));
            delete search.flexible;
            search['flexible'] = value;
            window.location.search = $.param(search);
        },
    });
});
document.body.innerHTML = document.body.innerHTML.replace('commande', ' Devis');
document.body.innerHTML = document.body.innerHTML.replace('Quantité', ' Unité');