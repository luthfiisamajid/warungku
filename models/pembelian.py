from odoo import api, fields, models


class pembelian(models.Model):
    _name = 'warungku.pembelian'
    _description = 'Detail Pembelian'

    name = fields.Char(string='Kode Pembelian')
    tanggal = fields.Datetime(string='Tanggal Pembelian',default=fields.Datetime.now)

    barangdetail_ids = fields.One2many(comodel_name='warungku.barang_pembelian',
                                 inverse_name='order_id',
                                  string='Detail Barang')

    total_pembelian = fields.Integer(compute='_compute_total_pembelian', string='Total Pembelian')

    @api.model
    def _compute_total_pembelian(self):
        for record in self:
            total=sum(self.env['warungku.barang_pembelian'].search([('order_id','=',record.id)]).mapped('jumlah_harga'))
            record.total_pembelian=total



class barang_pembelian(models.Model):
    _name = 'warungku.barang_pembelian'
    _description = 'Detail Barang Pembelian'

    name = fields.Char(string='Kode Pembelian')
    barang_id = fields.Many2one(comodel_name='warungku.barang', 
                                string='List Barang',
                                domain=[('stok','<','20')])

    order_id = fields.Many2one(comodel_name='warungku.pembelian', string='Order')
    

    harga = fields.Integer(compute='_compute_harga', string='harga')

    @api.depends('barang_id')
    def _compute_harga(self):
        for record in self:
            record.harga = record.barang_id.harga

    qty = fields.Integer(string='Quantity')
    jumlah_harga = fields.Integer(compute='_compute_jumlah_harga', string='Jumlah Harga')
    
    @api.depends('qty','harga')
    def _compute_jumlah_harga(self):
        for record in self:
            record.jumlah_harga=record.qty*record.harga

    
    
    

