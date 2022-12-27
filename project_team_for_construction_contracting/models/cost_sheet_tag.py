from random import randint

from odoo import fields, models, api


class CostSheetTags(models.Model):
    """ we can create tags that related to job orders,projects, and we can pick color
     according to our need  also we can set unique name for tags if it is not unique a
    warning will show """

    _name = "cost.sheet.tags"
    _description = "Cost Sheet Tags"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    def _get_default_color(self):
        return randint(1, 11)

    name = fields.Char('Name', required=True)
    color = fields.Integer(string='Color', default=_get_default_color)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists!"),
    ]

