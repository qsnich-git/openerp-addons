# -*- coding: utf-8 -*-

from openerp.osv import osv, fields
import datetime

class hospital_patient(osv.osv):
    def _compute_age(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for id in ids:
            data = self.browse(cr, uid, [id])[0] # select * from hospital_patient where id=[id]
            #data.dob data type = string ?
            ymd = data.dob.split('-')
 
            yy = int(ymd[0])
            mm = int(ymd[1])
            dd = int(ymd[2])
            
            birthday = datetime.date(yy,mm,dd)
            now = datetime.date.today()
            now_dd = now.day
            now_mm = now.month
            now_yy = now.year
    
            lastyear = datetime.date(now_yy,mm,dd)
            if lastyear > now:
                last_yy = now_yy - 1
                lastyear = datetime.date(last_yy,mm,dd)
            # count yearage
            yearage = lastyear.year - birthday.year
    
            # count monthage
            if now_mm >= mm:
                if now_mm - mm > 1:
                    monthage = now_mm - mm
                elif now_mm - mm == 1:
                    if now_dd > dd:
                        monthage = 1
                    else:
                        monthage = 0
                else:
                    if yearage == 0 and now_mm == mm and now_dd < dd:
                        monthage = 11
                    else:
                        monthage = 0
            else:
                if now_dd > dd:
                    monthage = 12 + now_mm - mm
                else:
                    monthage = 11 + now_mm - mm
    
            # count dayage
            if now_dd > dd:
                last_mm = now_mm
            else:
                last_mm = now_mm - 1

            lastmonth = datetime.date(now_yy,last_mm,dd)
    
            dayage = now - lastmonth
    
            agestr = str(yearage) + ' ปี ' + str(monthage) + ' เดือน ' + str(dayage.days) + ' วัน'   
            res[id] = agestr
        return res

    _name = 'hospital.patient'
    _description = 'Patient Info.'
    _columns = {
        'name': fields.char('HN', size=13, required=True),
        'firstname': fields.char('First Name', size=64, required=True),
        'lastname': fields.char('Last Name', size=64, required=True),
        'prefix_id': fields.many2one('hospital.prefix', 'Prefix', required=True),
        'active': fields.boolean('Active'),
        'sex': fields.selection([('0','Unisex'),('1','Male'),('2','Female')], 'Sex', required=True),
        'dob': fields.date('Date of Birth', required=True),
        'age': fields.function(_compute_age, string='Age', type='char'),
    }
    _defaults = {
        'active': True,
        'sex': '0',
    }

