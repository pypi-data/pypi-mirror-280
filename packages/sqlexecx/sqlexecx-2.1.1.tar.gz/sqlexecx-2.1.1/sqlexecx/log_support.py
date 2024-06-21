from sqlexecutorx.log_support import logger, do_sql_log, do_save_log, batch_sql_log, db_ctx_log


def insert_log(function: str, table: str, **kwargs):
    logger.debug("Exec func 'sqlexecx.%s' \n\t Table: '%s', kwargs: %s" % (function, table, kwargs))


def save_log(function: str, select_key: str, table: str, **kwargs):
    logger.debug("Exec func 'sqlexecx.%s', 'select_key': %s \n\t Table: '%s', kwargs: %s" % (function, select_key, table, kwargs))


def sql_log(function: str, sql: str, *args, **kwargs):
    logger.debug("Exec func '%s' \n\tsql: %s \n\targs: %s \n\tkwargs: %s" % (function, sql.strip(), args, kwargs))


def do_sql_log(function: str, sql: str, *args):
    logger.debug("Exec func '%s' \n\t sql: %s \n\t args: %s" % (function, sql, args))

#
# def db_ctx_log(action, connection):
#     logger.debug("%s connection <%s>..." % (action, hex(id(connection))))

