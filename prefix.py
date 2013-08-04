# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class hospital_prefix(osv.osv):
    _name = "hospital.prefix"
    _description = "Prefix"
    _columns = {
        "name": fields.char("Prefix",size=32, required=True),
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
