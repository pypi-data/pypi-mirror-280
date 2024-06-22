#  Copyright: Contributors to the sts project
#  GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

import logging
from time import sleep

from sts import iscsi
from sts.utils.logchecker import check_all

iscsiadm = iscsi.IscsiAdm()


def test_setup(variables: iscsi.ConfVars) -> None:
    iscsi.cleanup()
    iscsi.setup(variables)
    assert True


def test_login_logout() -> None:
    for i in range(1, 300):
        logging.info(f'Iteration {i}')
        assert iscsiadm.node_login().rc == 0
        sleep(0.1)
        assert iscsiadm.node_logoutall().rc == 0
    assert check_all()


def test_cleanup() -> None:
    iscsi.cleanup()
