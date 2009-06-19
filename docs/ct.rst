.. ct_restv_api_reference:

Category Tree REST API v0.1
===========================

.. automodule:: meaningtoolws.ct


Client
------

.. autoclass:: meaningtoolws.ct.Client()
    :members:
    :show-inheritance:

    Meaningtool Category Tree REST API v0.1 Client


    .. attribute:: ct_key

         *Meaningtool Category Tree Key* identifying the *Meaningtool Category
         Tree* associated with the requests made from this ``Client``.


    .. automethod:: meaningtoolws.ct.Client.__init__

        :Parameters:

            ct_key
                *Meaningtool Category Tree Key* identifying the *Meaningtool
                Category Tree* associated with the requests made from this
                ``Client``.


    .. automethod:: meaningtoolws.ct.Client.get_categories

        Wrapper around the Categorizing_ REST API method.

        :Parameters:

            source
                Determines where and how should Meaningtool read the text input.
                Possible values are:

                ``'text'``
                    The input text is sent along with this request, in
                    another parameter named ``input``.

                ``'url'``
                    The input text is available at the URL specified in
                    another parameter named ``input``.

            input
                Input data to be categorized. The meaning of this value is
                determined by the value specified in another parameter named ``source``.

            url_hint
                When the value of another parameter named ``source`` is ``'text'``,
                providing the URL from where you fetched that text here could help in the
                categorization of that input. Otherwise, this value is ignored.

            additionals
                A list of additional data to return along with the categories
                for the input text. Possible values are:

                ``'top-terms'``
                    Include a list of overall top terms found in the text that
                    where relevant to the categorization.

                ``'classifiers'``
                    Include a list of the classifiers in the Category Tree that
                    were involved in this categorization together with its
                    overall score in the categorization.

                ``'classifiers-top-terms'``
                    Include a list of top terms found in each classifier that
                    appeared in the input text together with its score within
                    the classifier.

            content_language
                This value determines the language of any text Meaningtool will
                try to read from input text. If you don't specify this,
                Meaningtool will try to guess the language.

        :Raises:
            A ``ResultError`` when the Meaningtool Result status is not
            ``'ok'``.

        :Returns:
            A ``Result`` when Meaningtool Result status is ``'ok'``.


    .. automethod:: meaningtoolws.ct.Client.get_tags

        Wrapper around the Tagging_ REST API method.

        :Parameters:

            source
                Determines where and how should Meaningtool read the text input.
                Possible values are:

                ``'text'``
                    The input text is sent along with this request, in
                    another parameter named ``input``.

                ``'url'``
                    The input text is available at the URL specified in
                    another parameter named ``input``.

            input
                Input data to be categorized. The meaning of this value is
                determined by the value specified in another parameter named ``source``.

            url_hint
                When the value of another parameter named ``source`` is ``'text'``,
                providing the URL from where you fetched that text here could help in the
                categorization of that input. Otherwise, this value is ignored.

            content_language
                This value determines the language of any text Meaningtool will
                try to read from input text. If you don't specify this,
                Meaningtool will try to guess the language.

        :Raises:
            A ``ResultError`` when the Meaningtool Result status is not
            ``'ok'``.

        :Returns:
            A ``Result`` when the Meaningtool Result status is ``'ok'``.


.. _Categorizing: http://meaningtool.com/docs/ws/rest/v0.1/index.html#categorizing
.. _Tagging: http://meaningtool.com/docs/ws/rest/v0.1/index.html#tagging


Results
-------

.. autoclass:: meaningtoolws.ct.Result()
    :members:
    :show-inheritance:

    Wrapper around a `Meaningtool Result`_.

    .. attribute:: meaningtoolws.ct.Result.status_errno

        A number (``int``) uniquely identifying an error scenario. When this number is
        different than ``0`` something wrong has happened, otherwise everything
        succeeded.

        You can lookup what does this error number mean later in the `Errors Reference`_.

    .. attribute:: meaningtoolws.ct.Result.status_message

        Detailed and human-readable message (``unicode``) about what just happened (E.g,
        ``'wrong ct_key'`` or ``'successfully categorized'``).

    .. attribute:: meaningtoolws.ct.Result.data

        The actual requested resource (``dict``).


.. autoclass:: meaningtoolws.ct.ResultError()
    :members:
    :show-inheritance:


.. _Meaningtool Result: http://meaningtool.com/docs/ws/rest/v0.1/index.html#meaningtool-results.
.. _Errors Reference: http://meaningtool.com/docs/ws/rest/v0.1/index.html#errors-reference
