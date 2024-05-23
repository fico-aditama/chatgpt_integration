# -*- coding: utf-8 -*-

from odoo import models, fields, api
import io
from PIL import Image
from rembg import remove 
import base64

class DocumentStudio(models.Model):
    _name = 'document.studio.template'
    _description = 'Document Studio Template'

    # Fitur 1: Proses gambar untuk menghapus latar belakang
    @api.depends('name')
    def action_process_image(self):
        for record in self:
            # Image processing logic to remove background
            pass

    # Fitur 2: Resize gambar
    @api.depends('name')
    def action_resize_image(self):
        for record in self:
            # Image resizing logic here
            pass

    # Fitur 3: Convert gambar ke PDF
    @api.depends('name')
    def action_convert_to_pdf(self):
        for record in self:
            # Image to PDF conversion logic here
            pass

    # Fitur 4: Ekstrak teks dari gambar
    @api.depends('name')
    def action_extract_text(self):
        for record in self:
            # Text extraction from image logic here
            pass

    # Fitur 5: Tambahkan watermark ke gambar
    @api.depends('name')
    def action_add_watermark(self):
        for record in self:
            # Add watermark to image logic here
            pass

    # Fitur 6: Flip gambar secara horizontal
    @api.depends('name')
    def action_flip_horizontal(self):
        for record in self:
            # Horizontal flipping logic here
            pass

    # Fitur 7: Putar gambar 90 derajat searah jarum jam
    @api.depends('name')
    def action_rotate_clockwise(self):
        for record in self:
            # Clockwise rotation logic here
            pass

    # Fitur 8: Konversi gambar ke grayscale
    @api.depends('name')
    def action_convert_to_grayscale(self):
        for record in self:
            # Grayscale conversion logic here
            pass

    # Fitur 9: Koreksi otomatis warna gambar
    @api.depends('name')
    def action_auto_correct_color(self):
        for record in self:
            # Automatic color correction logic here
            pass

    # Fitur 10: Segarkan histogram gambar
    @api.depends('name')
    def action_refresh_histogram(self):
        for record in self:
            # Refresh histogram logic here
            pass

    @api.depends('name')
    def action_process_image(self):
        for record in self:
            convert_image = remove(Image.open(io.BytesIO(base64.b64decode(record.name))))
            buff = io.BytesIO()
            convert_image.save(buff, format='png')
            record.processed_image = base64.b64encode(buff.getvalue()).decode('utf-8')
    
    def get_decoded_image(self):
        self.ensure_one()
        if self.processed_image:
            return base64.b64decode(self.processed_image)
        return False

    name = fields.Binary(string='Image')
    processed_image = fields.Binary(string='Processed Image')
    resized_image = fields.Binary(string='Resized Image')
    pdf_document = fields.Binary(string='PDF Document')
    extracted_text = fields.Text(string='Extracted Text')
    watermarked_image = fields.Binary(string='Watermarked Image')
    flipped_image = fields.Binary(string='Flipped Image')
    rotated_image = fields.Binary(string='Rotated Image')
    grayscale_image = fields.Binary(string='Grayscale Image')
    corrected_image = fields.Binary(string='Corrected Image')
    refreshed_image = fields.Binary(string='Refreshed Image')

