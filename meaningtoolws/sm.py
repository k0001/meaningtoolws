# -*- coding: utf-8 -*-

# Copyright (c) 2009, Popego Corporation <contact [at] popego [dot] com>
# All rights reserved.
#
# This file is part of the Meaningtool Web Services Python Client project
#
# See the COPYING file distributed with this project for its licensing terms.

"""
Meaningtool Semantic Map REST API v0.1 client

Official documentation for the REST API v0.1 can be found at
http://meaningtool.com/docs/ws/rest/v0.1
"""

import re
import urllib
import urllib2

try:
    import json
except ImportError:
    import simplejson as json


MT_BASE_URL = u"http://ws.meaningtool.com/rest/v0.1"
_re_url = re.compile(ur"^https?://.+$")


class Result(object):
    def __init__(self, status_errno, status_message, data):
        super(Result, self).__init__()
        self.status_errno = status_errno
        self.status_message = status_message
        self.data = data

    def __repr__(self):
        return u"<%s - %s>" % (self.__class__.__name__, self.status_message)


class ResultError(Result, Exception):
    def __init__(self, status_errno, status_message, data):
        Result.__init__(self, status_errno, status_message, data)
        Exception.__init__(self, u"%d: %s" % (status_errno, status_message))

    def __repr__(self):
        return u"<%s - %d: %s>" % (self.__class__.__name__, self.status_errno, self.status_message)


class Client(object):
    def __init__(self, sm_key):
        self.sm_key = sm_key
        self._base_url = u"%s/%s" % (MT_BASE_URL, sm_key)

    def __repr__(self):
        return u"<%s - sm_key: %s>" % (self.__class__.__name__, self.sm_key)

    def _req_base(self, method, url, data, headers):
        if method == "GET":
            req = urllib2.Request(u"%s?%s" % (url, urllib.urlencode(data)))
        elif method == "POST":
            req = urllib2.Request(url, urllib.urlencode(data))
        else:
            raise ValueError(u"HTTP Method '%s' not supported" % method)
        req.add_header("Content-Type", "application/x-www-form-urlencoded")
        req.add_header("Accept-Charset", "utf-8")
        for k,v in headers:
            req.add_header(k, v)
        try:
            resp = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            if e.code >= 500:
                raise
            return resp.read()

    def _req_json(self, method, url, data, headers):
        headers.append(("Accept", "application/json"))
        return self._req_base(method, url, data, headers)

    def _parse_result_base(self, result_dict):
        status = result_dict["status"]
        status_errno = result_dict["errno"]
        status_message = result_dict["message"]
        data = result_dict["data"]
        if status == "ok":
            return Result(status_errno, status_message, data)
        else:
            raise ResultError(status_errno, status_message, data)

    def _parse_result_json(self, raw):
        return self._parse_result_base(json.loads(raw, encoding="utf8"))

    # default request/parse methods
    _req = _req_json
    _parse_result = _parse_result_json

    def get_categories(self, source, input, url_hint=None, additionals=None, content_language=None):
        url = u"%s/categories" % self._base_url
        data = {}
        headers = []

        if not source in (u"text", u"url"):
            raise ValueError(u"source")
        data["source"] = source.encode("utf8")

        data["input"] = input.encode("utf8")

        if url_hint:
            if not _re_url.match(url_hint):
                raise ValueError(u"url_hint")
            data["url_hint"] = url_hint.encode("utf8")

        if additionals:
            for i in additionals:
                if not i in (u"top-terms", u"classifiers", u"classifiers-top-terms"):
                    raise ValueError(u"additionals")
            additionals = u",".join(set(additionals))
            data["additionals"] = additionals.encode("utf8")

        if content_language:
            content_language = content_language[:2].lower()
            if not len(content_language) == 2:
                raise ValueError(u"content_language")
            headers.append(("Content-Language", content_language.encode("ascii")))

        # Even if POST, it's idempotent as GET.
        return self._parse_result(self._req("POST", url, data, headers))

    def get_tags(self, source, input, url_hint=None, content_language=None):
        url = u"%s/tags" % self._base_url
        data = {}
        headers = []

        if not source in (u"text", u"url"):
            raise ValueError(u"source")
        data["source"] = source.encode("utf8")

        data["input"] = input.encode("utf8")

        if url_hint:
            if not _re_url.match(url_hint):
                raise ValueError(u"url_hint")
            data["url_hint"] = url_hint.encode("utf8")

        if content_language:
            content_language = content_language[:2].lower()
            if not len(content_language) == 2:
                raise ValueError(u"content_language")
            headers.append(("Content-Language", content_language.encode("ascii")))

        # Even if POST, it's idempotent as GET.
        return self._parse_result(self._req("POST", url, data, headers))
