from openerp import fields, models


class ResCompany(models.Model):

    """override company to add currency update"""

    def _multi_curr_enable(self, field_name, arg):
        "check if multi company currency is enabled"
        result = {}
        if not self.env['ir.model.fields'].search([('name', '=', 'company_id'), ('model', '=', 'res.currency')]):
            enable = 0
        else:
            enable = 1
        for company in self:
            result[company.id] = enable
        return result

    def button_refresh_currency(self):
        """Refrech  the currency !!for all the company
        now"""
        currency_updater_obj = self.env['currency.rate.update']
        try:
            currency_updater_obj.run_currency_update()
        except Exception as e:
            raise e
         
        return True

    def write(self, vals):
        """handle the activation of the currecny update on compagnies.
        There are two ways of implementing multi_company currency,
        the currency is shared or not. The module take care of the two
        ways. If the currency are shared, you will only be able to set
        auto update on one company, this will avoid to have unusefull cron
        object running.
        If yours currency are not share you will be able to activate the
        auto update on each separated company"""
        save_cron = {}
        for company in self:
            if 'auto_currency_up' in vals:
                enable = company.multi_company_currency_enable
                compagnies = self.search()
                activate_cron = 'f'
                value = vals.get('auto_currency_up')
                if not value:
                    for comp in compagnies:
                        if comp.auto_currency_up:
                            activate_cron = 't'
                            break
                    save_cron.update({'active': activate_cron})
                else:
                    for comp in compagnies:
                        if comp.id != company.id and not enable:
                            if comp.multi_company_currency_enable:
                                raise Exception('Yon can not activate auto currency ' +
                                                'update on more thant one company with this ' +
                                                'multi company configuration')
                    for comp in compagnies:
                        if comp.auto_currency_up:
                            activate_cron = 't'
                            break
                    save_cron.update({'active': activate_cron})

        if 'interval_type' in vals:
            save_cron.update({'interval_type': vals.get('interval_type')})
        if save_cron:
            self.env['currency.rate.update'].save_cron(save_cron)

        return super(ResCompany, self).write(vals)

    _inherit = "res.company"

         
    auto_currency_up = fields.Boolean('Automatical update of the currency this company')
    services_to_use = fields.One2many(
            'currency.rate.update.service',
            'company_id',
            'Currency update services'
        )
         
    interval_type = fields.Selection(
            [
                ('days', 'Day(s)'),
                ('weeks', 'Week(s)'),
                ('months', 'Month(s)')
            ],
            'Currency update frequence',
            help="""changing this value will
                                                 also affect other compagnies"""
        )
         
         
    multi_company_currency_enable = fields.Boolean(
        compute=_multi_curr_enable,
        method=True,
        type='boolean',
        string="Multi company currency",
        help='if this case is not check you can' +
        ' not set currency is active on two company'
    )

