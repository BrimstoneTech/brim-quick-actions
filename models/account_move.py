from odoo import models, _
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_quick_reset_to_draft(self):
        """
        BrimstoneTech Quick Actions:
        Cancels a posted invoice/bill and immediately resets it to draft
        in a single user click. Restricted to Accounting Manager role via
        the view-level groups attribute.
        """
        for move in self:
            if move.state != 'posted':
                raise UserError(
                    _('Only posted invoices or bills can be reset to draft using this action. '
                      'The document "%s" is currently in "%s" state.')
                    % (move.name, move.state)
                )

        # Use Odoo's standard safe method to handle cancellation and draft reset.
        # button_draft() in Odoo 17 internally handles the cancel step if needed.
        self.button_draft()
        return True
