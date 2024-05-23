/** @odoo-module */
import { registry } from '@web/core/registry'
const { Component } = owl

export class SalesDashboard extends Component {
    constructor() {
        super(...arguments)
        this.salesData = []
    };

    async willStart(startDate, endDate) {
        const salesData = await this.rpc({
            model: 'sale.order',
            method: 'search_read',
            args: [
                [
                    ['date_order', '>=', startDate],
                    ['date_order', '<=', endDate]
                ],
                ['id', 'name', 'amount_total']
            ]
        })

        this.salesData = salesData.records
        // this.renderChart()
        console.log(salesData);
    };

    renderChart() {
        // Add your chart rendering logic here, e.g., using Chart.js
        // Example:
        const ctx = document.getElementById('sales-chart').getContext('2d')
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: this.salesData.map(record => record.name),
                datasets: [
                    {
                        label: 'Sales Amount',
                        data: this.salesData.map(record => record.amount_total),
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 1
                    }
                ]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        })
    };

    mounted() {
        document.getElementById('filter-button').addEventListener('click', () => {
            const startDate = document.getElementById('start-date').value
            const endDate = document.getElementById('end-date').value
            if (startDate && endDate) {
                this.willStart(
                    Date(startDate),
                    Date(endDate)
                )
            }
            console.log(startDate);
        })
    };

}

SalesDashboard.template = 'custom_dashboard.SalesDashboard'
registry.category('actions').add('custom_dashboard.sales_dashboard', SalesDashboard)
