from keg.testing import ContextManager
import pytest

from keg_mail_ta.app import KegMailTestApp


def pytest_configure(config):
    KegMailTestApp.testing_prep()


@pytest.fixture(scope='class', autouse=True)
def auto_app_context():
    with ContextManager.get_for(KegMailTestApp).app.app_context():
        yield
