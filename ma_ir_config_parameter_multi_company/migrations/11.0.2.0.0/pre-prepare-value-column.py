

def migrate(cr, version):
     
     

     
    cr.execute("ALTER TABLE ir_config_parameter ADD COLUMN value VARCHAR")
