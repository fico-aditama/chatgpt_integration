odoo.define('custom_po.PosButtonRestruct', function (require) {
    'use strict';

    const PosGlobalState = require('point_of_sale.models').PosGlobalState;
    const Registries = require('point_of_sale.Registries');

    const PosButtonRestruct = (PosGlobalState) => {
        return class extends PosGlobalState {
            async _processData(loadedData) {
                await super._processData(...arguments);
                this.visible_backspace_btn = loadedData.visible_backspace_btn;
            }
        };
    };

    Registries.Model.extend(PosGlobalState, PosButtonRestruct);

    return PosButtonRestruct;
});
