from url_normalization.exceptions import InvalidURLException, InvalidSchemeException
from url_normalization.url_normalization import parse_url, unparse_url, normalize_scheme, normalize_netloc, \
    normalize_path

EXPECTED_DATA = {
    "http://example.com/path%20with%20spaces/and/special%20chars%20%26": "http://example.com/path%20with%20spaces/and/special%20chars%20%26",
    "http://example.com/path%2520with%2520spaces/and/special%2520chars%2520%2526": "http://example.com/path%20with%20spaces/and/special%20chars%20%26",
    "http://example.com/path%252520with%252520spaces/and/special%252520chars%252520%252526": "http://example.com/path%20with%20spaces/and/special%20chars%20%26",
    "http://example.com/café/menu/日本語": "http://example.com/caf%C3%A9/menu/%E6%97%A5%E6%9C%AC%E8%AA%9E",
    "http://example.com/привет/こんにちは@details": "http://example.com/%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82/%E3%81%93%E3%82%93%E3%81%AB%E3%81%A1%E3%81%AF%40details",
    "http://example.com/a/b/../c/./d.html": "http://example.com/a/c/d.html",
    "http://example.com/././a/b/../../c/d/./": "http://example.com/c/d",
    "http://example.com/a/.../b/../c/./d": "http://example.com/a/.../c/d",
    "http://example.com/a/%2E%2E/b/%2E/c": "http://example.com/b/c"
}


def test_normalize_path():
    for url, expected in EXPECTED_DATA.items():
        result = unparse_url(normalize_path(parse_url(url)))
        assert result == expected
