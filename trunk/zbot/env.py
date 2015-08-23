#coding:utf-8

class Env:
    @classmethod
    def load(cls,config):
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        
        from mako.lookup import TemplateLookup
        cls.get_template = TemplateLookup(
            directories=config.MAKO_TEMPLATE_DIR,
            module_directory=config.MAKO_MODULE_DIR,
            output_encoding='utf-8'
        ).get_template
        
        import logging.config
        logging.config.fileConfig(config.LOGGING_CONFIG)

        from zspy.filesys import makedirs
        makedirs(config.BSDDB_ENV)
        
        import bsddb
        db_env = bsddb.db.DBEnv()
        db_env.open(config.BSDDB_ENV,
            bsddb.db.DB_INIT_MPOOL |
            bsddb.db.DB_INIT_TXN |
            bsddb.db.DB_RECOVER |
            bsddb.db.DB_CREATE|
            bsddb.db.DB_THREAD|
            bsddb.db.DB_LOG_AUTOREMOVE
        )
        cls.db_env=db_env

        
