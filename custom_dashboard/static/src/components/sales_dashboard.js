/** @odoo-module */
import { registry } from "@web/core/registry"
import { KpiCard } from './kpi_card/kpi_card';
import { loadJS } from '@web/core/assets';
const { Component, onWillStart, useRef, onMounted } = owl

export class SalesDashboard extends Component {
    setup(){
        this.chartRefs = {
            chartTopProducts: useRef("chart-top-products"),
            chartTopSales: useRef("chart-top-sales"),
            chart1: useRef("chart-1"),
            chart2: useRef("chart-2"),
            chart3: useRef("chart-3"),
            chart4: useRef("chart-4"),
            chart5: useRef("chart-5"),
            chart6: useRef("chart-6"),
            chart7: useRef("chart-7"),
            chart8: useRef("chart-8"),
            chart9: useRef("chart-9"),
            chart10: useRef("chart-10"),
        }

        onWillStart(async ()=>{
            'https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.min.js'
        }) onMounted(()=>{
            const data = [
                { year: 2010, count: 10 },
                { year: 2011, count: 20 },
                { year: 2012, count: 15 },
                { year: 2013, count: 25 },
                { year: 2014, count: 22 },
                { year: 2015, count: 30 },
                { year: 2016, count: 28 },
              ];
              const colors = [
                'rgba(255, 99, 132, 0.2)', // Red
                'rgba(54, 162, 235, 0.2)', // Blue
                'rgba(255, 206, 86, 0.2)', // Yellow
                'rgba(75, 192, 192, 0.2)', // Green
                'rgba(153, 102, 255, 0.2)', // Purple
                'rgba(255, 159, 64, 0.2)', // Orange
                'rgba(220, 20, 60, 0.2)', // Crimson
                'rgba(0, 128, 128, 0.2)', // Teal
                'rgba(128, 0, 128, 0.2)', // Indigo
                'rgba(255, 215, 0, 0.2)', // Gold
            ];
            
              const createChart = (ref, type, data, backgroundColor) => {
                new Chart(ref.el, {
                    type: type,
                    data: {
                        labels: data.map(row => row.year),
                        datasets: [{
                            label: 'Acquisitions by year',
                            data: data.map(row => row.count),
                            backgroundColor: backgroundColor,
                            borderColor: 'rgba(0, 0, 0, 0.1)', 
                            borderWidth: 1, 
                        }]
                    }
                });
            }

            createChart(this.chartRefs.chartTopProducts, 'bar', data, colors[0]);
            createChart(this.chartRefs.chartTopSales, 'line', data, colors[1]);
            createChart(this.chartRefs.chart1, 'pie', data, colors[2]);
            createChart(this.chartRefs.chart2, 'doughnut', data, colors[3]);
            createChart(this.chartRefs.chart3, 'radar', data, colors[4]);
            createChart(this.chartRefs.chart4, 'polarArea', data, colors[5]);
            createChart(this.chartRefs.chart5, 'bubble', data, colors[6]);
            createChart(this.chartRefs.chart6, 'scatter', data, colors[7]);
            createChart(this.chartRefs.chart7, 'bar', data, colors[8]);
            createChart(this.chartRefs.chart8, 'line', data, colors[9]);
                        
        })
    }
}

SalesDashboard.template = 'custom_dashboard.SalesDashboard';
SalesDashboard.components = { KpiCard }
registry.category('actions').add('custom_dashboard.sales_dashboard', SalesDashboard)
