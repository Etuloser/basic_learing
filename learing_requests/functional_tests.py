import requests


def test_requests_get():
    """
    获取一个名为 r 的 Response 对象
    :return: <class 'requests.models.Response'>
    """
    r = requests.get('https://api.github.com/events')
    print(r.json())
    return r


def test_requests_post():
    """
    :return: <class 'requests.models.Response'>
    """
    r = requests.post('http://httpbin.org/post', data={'key': 'value'})
    print(r.json())
    return r


def test_post_with_params():
    """
    httpbin.org/get?key=val
    以一个字符串字典来提供这些参数
    :return: <class 'requests.models.Response'>
    """
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get("http://httpbin.org/get", params=payload)
    print(r.url)
    return r


def test_complex_requests_post():
    """
    :return: <class 'requests.models.Response'>
    """
    import json
    url = 'https://api.github.com/some/endpoint'
    payload = {'some': 'data'}
    r = requests.post(url, data=json.dumps(payload))
    # 也可以用 json 参数直接传值
    # r = requests.post(url, json=payload)
    return r


def test_response():
    """
    :return: <class 'requests.models.Response'>
    """
    r = requests.get('https://api.github.com/events')
    # 响应内容
    print(r.text)
    # 二进制响应内容
    print(r.content)
    # JSON 响应内容
    print(r.json())
    # 原始响应内容，一般用不上
    print(r.raw)
    return r


def test_customized_header():
    """
    传递一个 dict 给 headers 参数就可以了
    :return: <class 'requests.models.Response'>
    """
    url = 'https://api.github.com/some/endpoint'
    headers = {'user-agent': 'my-app/0.0.1'}
    r = requests.get(url, headers=headers)
    return r


def test_header():
    """
    响应头可以看成一个特殊的字典
    {
    'content-encoding': 'gzip',
    'transfer-encoding': 'chunked',
    'connection': 'close',
    'server': 'nginx/1.0.4',
    'x-runtime': '148ms',
    'etag': '"e1ca502697e5c9317743dc078f67693f"',
    'content-type': 'application/json'
    }
    :return: <class 'requests.models.Response'>
    """
    r = test_customized_header()
    print(r.headers)
    print(r.headers['Content-Type'])
    print(r.headers.get('content-type'))
    return r


def test_response_status():
    """
    :return: <class 'requests.models.Response'>
    """
    r = requests.get('http://httpbin.org/get')
    print(r.status_code)
    # 内置的状态检查码
    print(r.status_code == requests.codes.ok)
    bad_r = requests.get('http://httpbin.org/status/404')
    print(bad_r.status_code)
    # 抛出异常
    print(bad_r.raise_for_status())
    return r


def test_cookie():
    # todo
    """
    :return:
    """
    url = 'http://example.com/some/cookie/setting/url'
    r = requests.get(url)
    print(r.cookies)


def main():
    test_cookie()
    print('exec finished')


if __name__ == '__main__':
    main()
