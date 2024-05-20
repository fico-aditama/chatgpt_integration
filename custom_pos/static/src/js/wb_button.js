odoo.define('custom_po.WBSampleButton', function(require){

    "use strict";

    const PosComponent = require("point_of_sale.PosComponent");
    const ProductScreen = require("point_of_sale.ProductScreen");
    const Registries = require("point_of_sale.Registries");
    const { useListener } = require("@web/core/utils/hooks");

    class WBSampleButton extends PosComponent {

        setup(){
            super.setup();
            useListener("click", this.wb_button_click);
        }

        wb_button_click(){
            console.log('Helo Test');
        }
    }

    class WBSampleButton2 extends PosComponent {

        setup(){
            super.setup();
            useListener("click", this.wb_button_click);
        }

        wb_button_click(){
            console.log('Helo Test');
        }
    }


    WBSampleButton.template = "WBSampleButton";
    WBSampleButton2.template = "WBSampleButton2";


    ProductScreen.addControlButton({
        component: WBSampleButton,
        position: ["before", "OrderlineCustomerNoteButton"],

    });
    ProductScreen.addControlButton({
        component: WBSampleButton2,
        position: ["before", "NumpadWidget"],

    });

    Registries.Component.add(WBSampleButton);
    Registries.Component.add(WBSampleButton2);
    return WBSampleButton,WBSampleButton2;

});