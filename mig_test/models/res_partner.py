from odoo import _, fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    to_mig = fields.Char()
