# -*- coding: utf-8 -*-
from odoo import http
import json
from datetime import datetime

class CustomPos(http.Controller):

    @http.route('/pos/rpc/example', auth="user", type="json")
    def pos_example(self, **kwargs):
        result = http.request.env['res.lang'].search_read()
        return result 


    @http.route('/pos/rpc/example1', auth="user", type="http", website=True)
    def pos_example1(self, **kwargs):
        # Convert result to JSON format
        result = http.request.env['res.lang'].search_read()

        # Convert datetime objects to string representation
        for item in result:
            for key, value in item.items():
                if isinstance(value, datetime):
                    item[key] = value.strftime("%Y-%m-%d %H:%M:%S")

        # Return JSON response
        return http.Response(json.dumps(result), content_type='application/json;charset=utf-8')
