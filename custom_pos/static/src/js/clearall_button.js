odoo.define('custom_po.WBClearAlLButton', function (require) {
  'use strict'
  const PosComponent = require('point_of_sale.PosComponent')
  const ProductScreen = require('point_of_sale.ProductScreen')
  const Registries = require('point_of_sale.Registries')
  const { useListener } = require('@web/core/utils/hooks')
  const core = require('web.core')
  var _t = core._t

  class WBClearAlLButton extends PosComponent {
    setup () {
      super.setup()
      useListener('click', this.wb_clear_all_lines)
    }

    async wb_clear_all_lines () {
      console.log('wb_clear_all_lines method called')

      //   method 1
        var current_order = this.env.pos.get_order()
        console.log(current_order)
        current_order.orderlines.filter(line=> line.get_product()).forEach(single_line=>current_order.remove_orderline(single_line));

      //   method 2
      //   // Ensure there is a current order before attempting to clear its lines
      //   if (current_order) {
      //     // Get all order lines
      //     const order_lines = current_order.get_orderlines()
      //     console.log('Order lines before clearing:', order_lines)

      //     // Remove each order line
      //     for (let line of order_lines) {current_order.remove_orderline(line)}
      //     console.log('Order lines after clearing:',current_order.get_orderlines())
      //   }

      // method 3
      // Get the current order and clear its lines
      //   const current_order = this.env.pos.get_order()
      //   if (current_order) {
      //     current_order
      //       .get_orderlines()
      //       .forEach(line => current_order.remove_orderline(line))
      //   }
    }
  }

  WBClearAlLButton.template = 'WBClearAlLButton'

  ProductScreen.addControlButton({
    component: WBClearAlLButton,
    position: ['after', 'OrderlineCustomerNoteButton']
  })

  Registries.Component.add(WBClearAlLButton)
  return WBClearAlLButton
})
