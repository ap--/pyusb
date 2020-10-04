import pytest
import utils


@pytest.fixture(
    scope="class",
    params=["libusb1", "libusb0", "openusb"]
)
def backend(request):
    m = pytest.importorskip("usb.backend.%s" % request.param)
    b = m.get_backend()
    if b is None:
        pytest.skip("backend %s not available" % request.param)
    request.cls.backend = b
    yield


@pytest.fixture(scope="class")
def my_device(request, backend):
    dev = utils.find_my_device(backend)
    if dev is None:
        pytest.skip("test_device not available")
    request.cls.dev = dev
    yield
