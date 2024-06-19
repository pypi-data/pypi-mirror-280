from url_normalization.exceptions import InvalidURLException, InvalidSchemeException
from url_normalization.url_normalization import parse_url, unparse_url, normalize_scheme, normalize_netloc, \
    normalize_path, normalize_query_params

EXPECTED_DATA = {
    "http://example.com/?param1=val1&param2=val2": "http://example.com/?param1=val1&param2=val2",
    "http://example.com/test?Ç=Ç": "http://example.com/test?%C3%87=%C3%87",
    "http://example.com/page?Name=John%20Doe&Age=30": "http://example.com/page?Name=John%20Doe&Age=30",
    "http://example.com/path?param1=value%26value&param2=anotherValue": "http://example.com/path?param1=value%26value&param2=anotherValue",
    "http://example.com/api?param=value%26info%3D50%2525%20off": "http://example.com/api?param=value%26info%3D50%25%20off",
    "http://example.com/page?search=%2520query": "http://example.com/page?search=%20query",
    "https://example.com/search?q=OpenAI%20GPT": "https://example.com/search?q=OpenAI%20GPT",
    "https://example.com/product?id=%2531%2520%2532%2533": "https://example.com/product?id=1%2023",
    "https://example.com/api?data=%25252520Hello%25252520World": "https://example.com/api?data=%20Hello%20World",
    "https://example.com/query?message=Hello%2BWorld%26param%3D%2520+encoded": "https://example.com/query?message=Hello%2BWorld%26param%3D%20%20encoded"
}


def test_normalize_path():
    for url, expected in EXPECTED_DATA.items():
        result = unparse_url(normalize_query_params(parse_url(url)))
        assert result == expected
