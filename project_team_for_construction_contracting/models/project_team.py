from odoo import fields, models, api


class ProjectTeams(models.Model):
    """ here we can create different types of project teams in our company.
     based on the project team we can be chosen on the project,
     Project team can be set on Job order / Work order.
     Project team can be chosen on the job costing sheet."""

    _name = 'project.teams'
    _description = "Project Teams"
    _rec_name = "label"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    reference = fields.Char(string="Reference",
                            readonly=True, required=True,
                            copy=False, default='New')
    name = fields.Char(string="Name")
    label = fields.Char(compute='compute_name')
    project_manager_id = fields.Many2one('res.users', string="Project Manager")
    site_engineer_id = fields.Many2one('hr.employee', string="Site Engineer/Supervisor")
    project_teams_line_ids = fields.One2many('team.members.line',
                                             'project_teams_line_id')
    project_teams_line_ids_2 = fields.One2many('security.guard.line',
                                               'project_teams_line_id_2')
    project_teams_line_ids_3 = fields.One2many('store.officer.line',
                                               'project_teams_line_id_3')
    internal_notes = fields.Html(string="Internal Notes")

    @api.model
    def create(self, vals):
        if vals.get('reference', 'New') == 'New':
            vals['reference'] = self.env['ir.sequence'].next_by_code(
                'project.teams') or 'New'
        result = super(ProjectTeams, self).create(vals)
        return result

    @api.depends('reference', 'name')
    def compute_name(self):
        for rec in self:
            rec.label = rec.reference + "/ " + rec.name


class ProjectTeamsLine(models.Model):
    """ here we can choose the different types of members in the project teams like
    store officer,security guards """

    _name = 'team.members.line'
    _description = 'Team Members'

    employee_id = fields.Many2one('hr.employee', string="Name")
    login_id = fields.Char(string="Login")
    language_id = fields.Selection(string="Language", related='employee_id.lang')
    company_id = fields.Many2one('res.company', string="Company",
                                 default=lambda self: self.env.user.company_id)
    project_teams_line_id = fields.Many2one('project.teams')
    latest_authentication = fields.Text(string="Latest Authentication")
    is_two_factor_authentication = fields.Boolean(string="Two Factor Authentication")

    @api.onchange('employee_id')
    def _onchange_employee_id(self):
        login = self.employee_id.user_id.login
        self.login_id = login


class ProjectTeamsLine3(models.Model):
    """ here we can choose the different types of members in the project teams like
    store officer,security guards """

    _name = 'store.officer.line'
    _description = 'Store Officers'

    employee_id = fields.Many2one('hr.employee', string="Name")
    login_id = fields.Char(string="Login")
    language_id = fields.Selection(string="Language", related='employee_id.lang')
    company_id = fields.Many2one('res.company', string="Company",
                                 default=lambda self: self.env.user.company_id)
    project_teams_line_id_3 = fields.Many2one('project.teams')
    latest_authentication = fields.Text(string="Latest Authentication")
    is_two_factor_authentication = fields.Boolean(string="Two Factor Authentication")

    @api.onchange('employee_id')
    def _onchange_employee_id(self):
        login = self.employee_id.user_id.login
        self.login_id = login


class ProjectTeamsLine2(models.Model):
    """ here we can choose the different types of members in the project teams like
    store officer,security guards """

    _name = 'security.guard.line'
    _description = 'Security Guard'

    employee_id = fields.Many2one('hr.employee', string="Name")
    login_id = fields.Char(string="Login", )
    language_id = fields.Selection(string="Language", related='employee_id.lang')
    company_id = fields.Many2one('res.company', string="Company",
                                 default=lambda self: self.env.user.company_id)
    project_teams_line_id_2 = fields.Many2one('project.teams')
    latest_authentication = fields.Text(string="Latest Authentication")
    is_two_factor_authentication = fields.Boolean(string="Two Factor Authentication")

    @api.onchange('employee_id')
    def _onchange_employee_id(self):
        login = self.employee_id.user_id.login
        self.login_id = login
