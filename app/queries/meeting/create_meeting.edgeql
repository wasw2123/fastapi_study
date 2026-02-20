WITH
    url_code := <str>$url_code
SELECT (
    INSERT Meeting {
        url_code := url_code,
    }
) {url_code}