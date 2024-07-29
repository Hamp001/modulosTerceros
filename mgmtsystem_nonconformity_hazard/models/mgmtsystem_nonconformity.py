# Copyright 2024 - TODAY, Kaynnan Lemes <kaynnan.lemes@escodoo.com.br>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class MgmtsystemNonconformity(models.Model):

    _inherit = "mgmtsystem.nonconformity"

    hazard_ids = fields.Many2many("mgmtsystem.hazard", string="Risk Analysis")
