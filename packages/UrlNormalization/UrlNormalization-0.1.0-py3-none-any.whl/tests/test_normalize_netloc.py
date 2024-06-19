from url_normalization.exceptions import InvalidURLException, InvalidSchemeException
from url_normalization.url_normalization import parse_url, unparse_url, normalize_scheme, normalize_netloc

EXPECTED_DATA = {
    "http://example.com:80/test/path/": "http://example.com/test/path/",
    "http://example.com/test%20path/?q=value": "http://example.com/test%20path/?q=value",
    "HTTP://example.com//path///to/resource": "http://example.com//path///to/resource",
    "HTTPS://example.com/path?param=%20value%20": "https://example.com/path?param=%20value%20",
    "ftp://münchen.de:21/path?#": "ftp://xn--mnchen-3ya.de/path",
    "https://пример.испытание": "https://xn--e1afmkfd.xn--80akhbyknj4f",
    "http://sub1.sub2.example.com/path": "http://sub1.sub2.example.com/path",
    "https://WwW.Example.COM/A/B?z=alpha&y=beta#Fragment": "https://www.example.com/A/B?z=alpha&y=beta#Fragment",
    "https://user:pass@www.example.com:8080/path;param?query1=val1&query2=val2#frag": "https://user:pass@www.example.com:8080/path;param?query1=val1&query2=val2#frag",
    "https://127.0.0.1:443/test/A/B?a=1&b=2": "https://127.0.0.1/test/A/B?a=1&b=2",
    "http://user@example.com": "http://user@example.com",
    "http://:password@example.com": "http://:password@example.com",
    "https://:@example.com": "https://:@example.com"
}


def test_normalize_netloc():
    for url, expected in EXPECTED_DATA.items():
        result = unparse_url(normalize_netloc(parse_url(url), strip_userinfo=False, strip_port=False))
        assert result == expected
