from url_normalization.exceptions import InvalidURLException, InvalidSchemeException
from url_normalization.url_normalization import parse_url, unparse_url, normalize_scheme

EXPECTED_DATA = {
    "://example.com": "https://example.com",
    "//example.com": "https://example.com",
    "/example.com": "https://example.com",
    "example.com": "https://example.com",
    "http://example.com:80/test/path/": "http://example.com:80/test/path/",
    "http://example.com/test%20path/?q=value": "http://example.com/test%20path/?q=value",
    "HTTP://example.com//path///to/resource": "http://example.com//path///to/resource",
    "HTTPS://example.com/path?param=%20value%20": "https://example.com/path?param=%20value%20",
    "ftp://münchen.de/path?#": "ftp://münchen.de/path",
    "http://sub1.sub2.example.com/path": "http://sub1.sub2.example.com/path",
    "//WwW.Example.COM/A/B?z=alpha&y=beta#Fragment": "https://WwW.Example.COM/A/B?z=alpha&y=beta#Fragment",
    "https://user:pass@www.example.com:8080/path;param?query1=val1&query2=val2#frag": "https://user:pass@www.example.com:8080/path;param?query1=val1&query2=val2#frag",
    "file:///C:/path/to/file/../anotherfile": "invalid",
    "test://example.com": "invalid",
    "1test://example.com": "invalid",
    "+test.example.com": "invalid",
    "/test://example.com": "invalid",
    "123": "invalid",
    "": "invalid",
    "t tp://www.example.com": "invalid",
    "htt$p://www.example.com": "invalid",
    "http=>://www.example.com": "invalid",
    "http:??www.example.com": "invalid",
    "ftp:://www.example.com": "invalid",
    "http:/\www.example.com": "invalid",
    "http:/www.example.com": "invalid",
    "ht*tp://www.example.com": "invalid",
    "10.0.0.1": "https://10.0.0.1",
    "http://127.0.0.1:80/test/A/B?a=1&b=2": "http://127.0.0.1:80/test/A/B?a=1&b=2"
}


def test_normalize_scheme():
    for url, expected in EXPECTED_DATA.items():
        try:
            result = unparse_url(normalize_scheme(parse_url(url)))
        except InvalidURLException:
            result = "invalid"
        except InvalidSchemeException:
            result = "invalid"

        assert result == expected
