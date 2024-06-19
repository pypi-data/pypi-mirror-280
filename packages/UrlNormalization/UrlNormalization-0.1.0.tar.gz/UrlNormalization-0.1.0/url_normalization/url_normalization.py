import posixpath
import re
from urllib.parse import urlparse, urlunparse, quote, unquote, parse_qsl, urlencode, unquote_plus
import idna
import validators

from url_normalization.exceptions import NoNetLocException, InvalidNetlocException, \
    NoSchemeException, InvalidURLException, InvalidSchemeException

DEFAULT_CHARSET = "utf-8"
DEFAULT_SCHEME = 'https'
DEFAULT_SCHEME_PORT = {
    "ftp": 21,
    "ftps": 990,
    "git": 9418,
    "http": 80,
    "https": 443,
    "rtsp": 554,
    "sftp": 22,
    "ssh": 20,
    "telnet": 23
}


def normalize_url(url):
    parsed_url = parse_url(url)
    norm_scheme = normalize_scheme(parsed_url)
    norm_netloc = normalize_netloc(norm_scheme)
    norm_path = normalize_path(norm_netloc)
    norm_query_params = normalize_query_params(norm_path)
    norm_frag = normalize_fragment(norm_query_params)
    unparsed_url = unparse_url(norm_frag)

    return unparsed_url


def has_scheme(url):
    # Using regex to detect if url starts with anything followed by ://
    scheme_regex = r'^.+://'

    if not re.match(scheme_regex, url):
        return False
    return True


def has_well_formed_scheme(url):
    # Using regex instead of whitelist of schemes
    # Scheme names consist of a sequence of characters beginning with a
    # letter and followed by any combination of letters, digits, plus
    # ("+"), period ("."), or hyphen ("-").
    scheme_regex = r'^[a-zA-Z][a-zA-Z0-9+\-.]*://'

    if not re.match(scheme_regex, url):
        return False
    return True


def add_default_scheme(url, scheme=DEFAULT_SCHEME):
    url = url.lstrip("://")
    return f"{scheme.lower()}://{url}"


def recursive_percent_decode(blob):
    curr_blob = blob
    decoded_blob = unquote(blob)
    while decoded_blob != curr_blob:
        curr_blob = decoded_blob
        decoded_blob = unquote(decoded_blob)

    return decoded_blob


def recursive_percent_decode_plus(blob):
    blob = blob.replace("+", "%20")
    curr_blob = blob
    decoded_blob = unquote(blob)
    while decoded_blob != curr_blob:
        curr_blob = decoded_blob
        decoded_blob = unquote(decoded_blob)

    return decoded_blob


def parse_url(url):
    # TODO: trim whitespaces and useless chars before validating
    # url invalid, handle scheme issues
    if not has_scheme(url):
        # no scheme so add default
        url = add_default_scheme(url)
    else:
        # has scheme
        if not has_well_formed_scheme(url):
            # scheme not well-formed
            raise InvalidSchemeException()

    # Parse the URL into components
    parsed_url = urlparse(url)

    return parsed_url


def unparse_url(parsed_url):
    # Reconstruct the URL
    return urlunparse(parsed_url)


def normalize_scheme(parsed_url):
    # Check if the scheme is missing
    if not parsed_url.scheme:
        raise NoSchemeException()

    # Lowercase scheme
    parsed_url = parsed_url._replace(scheme=parsed_url.scheme.lower())

    return parsed_url


def normalize_netloc(parsed_url, strip_userinfo=False, strip_port=True, charset=DEFAULT_CHARSET):
    if not parsed_url.netloc:
        raise NoNetLocException()

    # lowercase hostname
    userinfo_username = parsed_url.username
    userinfo_password = parsed_url.password
    hostname = parsed_url.hostname
    port = parsed_url.port

    # IDNA encode hostname
    try:
        if hostname is not None:
            # strip useless "." characters if any
            hostname = hostname.strip(".")
            # to lowercase
            hostname = hostname.lower()
            idna_encoded_hostname = idna.encode(hostname)
        else:
            idna_encoded_hostname = ""
    except idna.IDNAError as e:
        # failed to IDNA encode hostname probably due to some invalid hostname characters
        raise InvalidNetlocException()

    # reconstruct netloc (userinfo:hostname:port)
    encoded_netloc = idna_encoded_hostname.decode(charset)
    if not strip_userinfo and (userinfo_username is not None or userinfo_password is not None):
        userinfo = f"{userinfo_username or ''}"
        userinfo += "@" if userinfo_password is None else ""
        userinfo += f":{userinfo_password}@" if userinfo_password is not None else ""
        encoded_netloc = userinfo + encoded_netloc

    if strip_port and port is not None:
        # remove default port based on scheme
        if parsed_url.scheme not in DEFAULT_SCHEME_PORT.keys():
            encoded_netloc += f":{parsed_url.port}"
        else:
            if port != DEFAULT_SCHEME_PORT.get(parsed_url.scheme):
                encoded_netloc += f":{parsed_url.port}"

    parsed_url = parsed_url._replace(netloc=encoded_netloc)

    return parsed_url


def normalize_path(parsed_url, to_lowercase=False):
    if parsed_url.path:
        # decode percent encoded characters to avoid double percent encoding
        decoded_path = recursive_percent_decode(parsed_url.path)

        # dot segments path normalization
        escaped_dot_segments_path = posixpath.normpath(decoded_path)
        # handle special case where path starts with "//" which normpath doesn't handle
        if escaped_dot_segments_path.startswith("//"):
            escaped_dot_segments_path = f"/{escaped_dot_segments_path.lstrip('/')}"
        if to_lowercase:
            lowercase_path = escaped_dot_segments_path.lower()
            # percent encoding
            # unicode chars will be utf-8 encoded then percent encoded
            encoded_path = quote(lowercase_path, "~:/?#[]@!$&'()*+,;=")
        else:
            # percent encoding
            # unicode chars will be utf-8 encoded then percent encoded
            encoded_path = quote(escaped_dot_segments_path)

        parsed_url = parsed_url._replace(path=encoded_path)

    return parsed_url


def normalize_query_params(parsed_url):
    params = [
        "=".join([quote(recursive_percent_decode_plus(t)) for t in q.split("=", 1)])
        for q in parsed_url.query.split("&")
    ]
    joined_params = "&".join(params) if params else ""
    parsed_url = parsed_url._replace(query=joined_params)

    return parsed_url


def normalize_fragment(parsed_url):
    if parsed_url.fragment:
        parsed_url = parsed_url._replace(fragment='')

    return parsed_url
