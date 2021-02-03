import os

from file_helper import FileHelper, Api
import pytest
from unittest import mock

@pytest.fixture
def api():
    """Фикстура АПИ"""
    api = Api("api_key_secret")
    yield api
    api.close()


@pytest.fixture
def fh(api):
    # api = object()
    fh = FileHelper(api)
    return fh

class TestFileHelper:
    def test_init(self):
        api = object()
        fh = FileHelper(api)
        assert fh.api is api

    def test_remove_file(self, fh, temp_file):
        # filepath = temp_file()
        fh.remove_file(temp_file)  # Удаляем файл
        assert os.path.exists(temp_file) is False  # Проверяем существует  ли файл.

    @mock.patch('file_helper.os')
    def test_uses_unlink_for_remove(self, mocked_fh_os, fh):
        filepath = 'rewertyu'
        mocked_fh_os.path.isfile.return_value = True
        fh.remove_file(filepath)
        mocked_fh_os.unlink_assert_called_once_with(filepath)

    @mock.patch.object(FileHelper, "prepare_file", autospec=True)
    def test_upload_file(self, mocked_prepare_file):
        # используя autospec=True мы можем проверить что у нас работает правильно вызов внутри.
        fake_api = mock.MagicMock()
        # expected_data = object()
        # mocked_prepare_file.return_value = expected_data
        fake_filepath = "newagno"
        fh = FileHelper(fake_api)
        fh.upload_file(fake_filepath)
        fake_api.request.assert_called_once_with("POST", mocked_prepare_file.return_value)
        mocked_prepare_file.assert_called_once_with(fh, fake_filepath)


# 1.02.45 Остановился.
# 1.20