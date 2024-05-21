odoo.define('custom_po.WBSampleButton', function (require) {
  'use strict'
  const PosComponent = require('point_of_sale.PosComponent')
  const ProductScreen = require('point_of_sale.ProductScreen')
  const Registries = require('point_of_sale.Registries')
  const { useListener } = require('@web/core/utils/hooks')
  const core = require('web.core')
  var _t = core._t

  class WBSampleButton extends PosComponent {
    setup () {
      super.setup()
      useListener('click', this.wb_button_click)
    }

    async wb_button_click () {
      // Documentation:
      // This popup is used to display an error message to the user.
      // `title` specifies the title of the popup.
      // `body` contains the message to be displayed.
      // `confirmText` is the text on the confirmation button.
      // `cancelText` is the text on the cancel button.
      // `confirmed` will be true if the user clicks the confirm button, and false otherwise.
      // `selectedOption` will contain the selected option's data.
      // `keepBehind` specifies whether to keep the popup behind other elements.

      // Show an error message popup
      // this.showPopup("ErrorPopup", {
      //     title: "Error Message",
      //     body: "The simple error message screen",
      // });

      // Show a confirmation dialog popup and handle the response
      // const { confirmed } = await this.showPopup("ConfirmPopup", {
      //     title: "Confirm Popup",
      //     body: "Are you sure you want to continue?",
      //     confirmText: "Yes",
      //     cancelText: "No",
      // });

      // if (confirmed) {
      //     console.log('Clicked Yes Button', confirmed);
      // } else {
      //     console.log('Clicked No Button', confirmed);
      // }

      // Show an offline error message popup
      // this.showPopup("OfflineErrorPopup", {
      //     title: "Odoo Error",
      //     body: "Hey, this is a test popup screen, don't take it seriously",
      // });

      // Show a selection popup and handle the selected option
      // const { confirmed, payload: selectedOption } = await this.showPopup("SelectionPopup", {
      //     title: "Are you a good JS Developer?",
      //     list: [
      //         {'id':0, 'label':"Yes",'item':"You pressed Yes" },
      //         {'id':1, 'label':"Sure",'item':"You pressed Sure" },
      //         {'id':2, 'label':"Not Sure",'item':"You pressed Not Sure" },
      //     ]
      // });
      // console.log(confirmed);
      // console.log(selectedOption);

      // Show a close POS info popup
      // const info = await this.env.pos.getClosePosInfo();
      // this.showPopup("ClosePosPopup", {
      //     info: info,
      //     keepBehind: true
      // });

      // agar bisa translate
      // this.showPopup('ErrorPopup', {
      //   title: this.env._t('Error Message'),
      //   body: this.env._t('The Simple Error Message Screen')
      // })

      // hindari translate
      // this.showPopup("ErrorPopup", {
      //     title: "Error Message",
      //     body: "The Simple Error Message Screen",
      // });


      // RPC (Remote Procedure Call) Calls
      // var result = await this.rpc({
      //   "model":"res.lang",
      //   "method":"search_read",
      //   "args":[[],["id","name","code"]],
      // })

      // var result = await this.rpc({
      //   "route":"/pos/rpc/example",
      //   "params":{},
      // })

      // // console.log(result);
      // result.forEach(function(value){
      //   console.log("Record-->", value)
      // });

      // VIdeo 12
      var result = await this.rpc({
        "route":"/pos/rpc/example",
        "params":{},
      })
      
      var multi_lang_list = [];

      result.forEach(function(value){
        multi_lang_list.push({"id":value.id,
          "label": value.name,
          "item": value
        });
      });
      console.log(multi_lang_list);

      var {confirmed, payload: selectedOption} = await this.showPopup("SelectionPopup", {
        "title": "Active Language",
        list: multi_lang_list,
      })
      console.log(confirmed, selectedOption)

    }
  }

  class WBSampleButton2 extends PosComponent {
    setup () {
      super.setup()
      useListener('click', this.wb_button_click)
    }

    wb_button_click () {
      console.log('Helo Test')
    }
  }

  WBSampleButton.template = 'WBSampleButton'
  WBSampleButton2.template = 'WBSampleButton2'

  ProductScreen.addControlButton({
    component: WBSampleButton,
    position: ['before', 'OrderlineCustomerNoteButton']
  })
  ProductScreen.addControlButton({
    component: WBSampleButton2,
    position: ['before', 'NumpadWidget']
  })

  Registries.Component.add(WBSampleButton)
  Registries.Component.add(WBSampleButton2)
  return WBSampleButton, WBSampleButton2
})
