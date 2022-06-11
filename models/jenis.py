from odoo import api,fields,models

class jenis(models.Model):
    _name = 'warungku.jenis'
    _description = 'pemasok barang warungku'

    name = fields.Char(string='Jenis Barang')
    deskripsi = fields.Char(string='Keterangan Barang')
    letak = fields.Char(string='Letak Barang')
    barang_ids = fields.One2many(comodel_name='warungku.barang', inverse_name='jenis_id', string='Jenisnya')
    