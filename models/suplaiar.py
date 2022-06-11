from odoo import api,fields,models

class suplaiar(models.Model):
    _name = 'warungku.suplaiar'
    _description = 'pemasok barang warungku'

    name = fields.Char(string='Nama Perusahaan')
    cp = fields.Char(string='Contact_Person')
    no_tlp = fields.Char(string='No_tlp')
    alamat = fields.Char(string='Alamat')
    barang_ids = fields.One2many(comodel_name='warungku.barang',inverse_name='pemasok',string='Barangnya')
    

      