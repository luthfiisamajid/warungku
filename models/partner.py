from odoo import api, fields, models


class Partner(models.Model):
    _name = 'warungku.partner'
    _description = 'human description'

    name = fields.Char(string='Name')
    alamat = fields.Char(string='Alamat')
    no_tlp = fields.Char(string='No_tlp')   
    foto = fields.Char(string='Foto')

    



class Pegawai(models.Model):
    _inherit = 'warungku.partner'
    _description = 'list pegawai'
    _name = 'warungku.pegawai'

    name = fields.Char(string='Name')
    jabatan = fields.Char(string='Jabatan')
    gaji = fields.Integer(string='Gaji')
    bonus = fields.Integer(string='Bonus')
    menikah = fields.Boolean(string='Menikah')


class Customer(models.Model):
    _name = 'warungku.customer'
    _description = 'customer description'

    name = fields.Char(string='Name')
    level = fields.Char(string='Level')
    menikah = fields.Boolean(string='Menikah')
    
    
    
    
    
    


