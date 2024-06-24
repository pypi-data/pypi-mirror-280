# -*- coding: utf-8 -*-
from __future__ import annotations

import pytest

from codecov import github_client


def test_github_client_get(session, gh):
    session.register('GET', '/repos/a/b/issues', timeout=60, params={'a': 1})(json={'foo': 'bar'})

    assert gh.repos('a/b').issues().get(a=1) == {'foo': 'bar'}


def test_github_client_get_text(session, gh):
    session.register('GET', '/repos/a/b/issues', timeout=60, params={'a': 1})(
        text='foobar', headers={'content-type': 'application/vnd.github.raw+json'}
    )

    assert gh.repos('a/b').issues().get(a=1, use_text=True) == 'foobar'


def test_github_client_get_bytes(session, gh):
    session.register('GET', '/repos/a/b/issues', timeout=60, params={'a': 1})(
        text='foobar', headers={'content-type': 'application/vnd.github.raw+json'}
    )

    assert gh.repos('a/b').issues().get(a=1, use_bytes=True) == b'foobar'


def test_github_client_get_headers(session, gh):
    session.register('GET', '/repos/a/b/issues', timeout=60, params={'a': 1})(
        json={'foo': 'bar'},
        headers={'X-foo': 'yay'},
    )

    assert gh.repos('a/b').issues().get(a=1, headers={'X-foo': 'yay'}) == {'foo': 'bar'}


def test_github_client_post_non_json(session, gh):
    session.register('POST', '/repos/a/b/issues', timeout=60, json={'a': 1})()

    gh.repos('a/b').issues().post(a=1)


def test_json_object():
    obj = github_client.JsonObject({'a': 1})

    assert obj.a == 1


def test_json_object_error():
    obj = github_client.JsonObject({'a': 1})

    with pytest.raises(AttributeError):
        _ = obj.b


def test_github_client_get_error(session, gh):
    session.register('GET', '/repos')(
        json={'foo': 'bar'},
        status_code=404,
    )

    with pytest.raises(github_client.ApiError) as exc_info:
        gh.repos.get()

    assert str(exc_info.value) == "{'foo': 'bar'}"


def test_github_client_get_error_non_json(session, gh):
    session.register('GET', '/repos')(
        text='{foobar',
        headers={'content-type': 'text/plain'},
        status_code=404,
    )

    with pytest.raises(github_client.ApiError) as exc_info:
        gh.repos.get()

    assert str(exc_info.value) == "b'{foobar'"
