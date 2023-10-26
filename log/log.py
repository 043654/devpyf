import logging
from utils.Common import Commons

path = Commons.getFilePath()
logpath = path + "\\log"
logging.basicConfig(format='%(asctime)s - %(filename)s - %(funcName)s -[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.DEBUG,
                    filename=logpath + 'run.log',
                    )
logging.debug('debug级别，一般用来打印一些调试信息，级别最低')
logging.info('info级别，一般用来打印一些正常的操作信息')
logging.warning('waring级别，一般用来打印警告信息')
logging.error('error级别，一般用来打印一些错误信息')
logging.critical('critical级别，一般用来打印一些致命的错误信息，等级最高')


logging.info('2322222222222222222222222222222222222222222222222222222222222222222222222')