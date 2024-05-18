# -*- coding: utf-8 -*-

from odoo import models, fields, api
from openai import OpenAI
import json

client = OpenAI(api_key='')

class ChatGPT(models.Model):
    _name = 'chatgpt.message'
    _description = 'chatgpt_integration.chatgpt_integration'

    name = fields.Text()
    message = fields.Text(string='Request Message')
    response = fields.Text(string='Response', readonly=True)


    def action_send_message(self):
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
            {"role": "user", "content": self.message}
        ]
        )
        response_text = json.loads(response.choices[0].message.content)
        print(response_text)
        if response_text['jawaban']:
            self.response = response_text['jawaban']
        elif response_text['Jawaban']:
            self.response = response_text['Jawaban']
        else:
            self.response = response_text
