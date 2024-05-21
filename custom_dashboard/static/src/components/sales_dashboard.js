/** @odoo-module */
import {registry} from "@web/core/registry"
const { Component } = owl

export class SalesDashboard extends Component {
    setup(){
        
    }
}

SalesDashboard.template = "custom_dashboard.SalesDashboard"
registry.category("actions").add("custom_dashboard.sales_dashboard", SalesDashboard)