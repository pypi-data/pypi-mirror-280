from url_normalization.url_normalization import parse_url, normalize_fragment, unparse_url, normalize_scheme

EXPECTED_DATA = {
    "http://example.com:80/test/path/": "http://example.com:80/test/path/",
    "http://example.com/test%20path/?q=value": "http://example.com/test%20path/?q=value",
    "http://example.com//path///to/resource": "http://example.com//path///to/resource",
    "http://example.com/path?param=%20value%20": "http://example.com/path?param=%20value%20",
    "http://münchen.de/path?#": "http://münchen.de/path",
    "http://sub1.sub2.example.com/path": "http://sub1.sub2.example.com/path",
    "//WwW.Example.COM/A/B?z=alpha&y=beta#Fragment": "https://WwW.Example.COM/A/B?z=alpha&y=beta",
    "https://user:pass@www.example.com:8080/path;param?query1=val1&query2=val2#frag": "https://user:pass@www.example.com:8080/path;param?query1=val1&query2=val2"
}


def test_normalize_fragment():
    for url, expected in EXPECTED_DATA.items():

        result = unparse_url(normalize_scheme(normalize_fragment(parse_url(url))))
        assert result == expected
        