from odoo import fields, models, api


class ProjectTeamProject(models.Model):
    _inherit = 'project.project'

    project_teams_id = fields.Many2one('project.teams', string='Project Team')
    site_engineer_id = fields.Many2one('hr.employee', string="Site Engineer/Supervisor")
    project_teams_line_ids = fields.One2many('team.members.line.inherit',
                                             'project_teams_line_id', readonly=True)
    project_teams_line_ids_2 = fields.One2many('security.guard.line.inherit',
                                               'project_teams_line_id_2', readonly=True)
    project_teams_line_ids_3 = fields.One2many('store.officer.line.inherit',
                                               'project_teams_line_id_3', readonly=True)

    @api.onchange('project_teams_id')
    def _onchange_project_teams(self):
        manager = self.project_teams_id.project_manager_id
        engineer = self.project_teams_id.site_engineer_id
        self.user_id = manager
        self.site_engineer_id = engineer
        for rec in self:
            lines = [(5, 0, 0)]
            for line in self.project_teams_id.project_teams_line_ids:
                val = {
                    'employee_id': line.employee_id,
                    'login_id': line.login_id,
                    'company_id': line.company_id,

                }

                lines.append((0, 0, val))
                rec.project_teams_line_ids = lines

            lines = [(5, 0, 0)]
            for line in self.project_teams_id.project_teams_line_ids_2:
                val = {
                    'employee_id': line.employee_id,
                    'login_id': line.login_id,
                    'company_id': line.company_id,

                }
                lines.append((0, 0, val))
                rec.project_teams_line_ids_2 = lines

            lines = [(5, 0, 0)]
            for line in self.project_teams_id.project_teams_line_ids_3:
                val = {
                    'employee_id': line.employee_id,
                    'login_id': line.login_id,
                    'company_id': line.company_id,

                }
                lines.append((0, 0, val))
                rec.project_teams_line_ids_3 = lines


class ProjectTeamsLineInherit(models.Model):
    """Here automatically add the team members by choosing the corresponding project """

    _name = 'team.members.line.inherit'
    _description = 'Team Members'

    employee_id = fields.Many2one('hr.employee', string="Name")
    login_id = fields.Char(string="Login")
    language_id = fields.Selection(string="Language", related='employee_id.lang')
    company_id = fields.Many2one('res.company', string="Company",
                                 )
    project_teams_line_id = fields.Many2one('project.project')
    latest_authentication = fields.Text(string="Latest Authentication")
    is_two_factor_authentication = fields.Boolean(string="Two Factor Authentication")


class ProjectTeamsLineInherit3(models.Model):
    """Here automatically add the Store Officers by choosing the corresponding project """
    _name = 'store.officer.line.inherit'
    _description = 'Store Officers'

    employee_id = fields.Many2one('hr.employee', string="Name")
    login_id = fields.Char(string="Login")
    language_id = fields.Selection(string="Language", related='employee_id.lang')
    company_id = fields.Many2one('res.company', string="Company")
    project_teams_line_id_3 = fields.Many2one('project.project')
    latest_authentication = fields.Text(string="Latest Authentication")
    is_two_factor_authentication = fields.Boolean(string="Two Factor Authentication")


class ProjectTeamsLineInherit2(models.Model):
    """Here automatically add the Security Guard by choosing the corresponding project """
    _name = 'security.guard.line.inherit'
    _description = 'Security Guard'

    employee_id = fields.Many2one('hr.employee', string="Name")
    login_id = fields.Char(string="Login", )
    language_id = fields.Selection(string="Language", related='employee_id.lang')
    company_id = fields.Many2one('res.company', string="Company")
    project_teams_line_id_2 = fields.Many2one('project.project')
    latest_authentication = fields.Text(string="Latest Authentication")
    is_two_factor_authentication = fields.Boolean(string="Two Factor Authentication")
