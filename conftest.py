# выполняеться в самом начале, ложем сюда текстуру test_file она будет доступна во всех наших тестовых файлах

import pytest


@pytest.fixture # отмечаем что это фикстура. Она нам возвращает временную директорию tmp_path
def temp_file(tmp_path):
    f = tmp_path / 'filename'  # Создаем файл
    f.write_text("CONTENT")
    return f