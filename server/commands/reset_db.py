'''
Faraday Penetration Test IDE
Copyright (C) 2013  Infobyte LLC (http://www.infobytesec.com/)
See the file 'doc/LICENSE' for the license information

'''
from server.models import db

def reset_db_all():
    # It might be  required to do a cascade delete to correctly the
    # vulnerability table
    for table in ('vulnerability', 'vulnerability_template', 'comment',
                  'faraday_user'):
        try:
            db.engine.execute('DROP TABLE {} CASCADE'.format(table))
        except:
            pass
    db.drop_all()
    db.create_all()

