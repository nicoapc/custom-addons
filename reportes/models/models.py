# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    pro_services = fields.Selection(
        string="Servicios Profesionales",
        selection=[
            ('0', "Implementación"),
            ('1', "Capacitación"),
            ('2', "Acompañamiento"),


        ]

    )
