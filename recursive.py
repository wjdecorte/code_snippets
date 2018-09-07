"""
Recursive Function for replacing variables with values (standard python string formatting)
"""


def format_string(string_value, context_value):
    """
    Needs to be completed (see str_formatter repo)
    """
    pass


def replace_variables(data, ctx):
    """
    Iterate over data that could have nested dictionaries and lists to
    replace variables with values contained in context
    :param data: input data
    :param ctx: key/value pairs
    :return:
    """
    if isinstance(data, dict):
        for k, v in data.iteritems():
            if isinstance(v, basestring):
                data[k] = format_string(v, ctx)
            else:
                replace_variables(v, ctx)
    elif isinstance(data, list):
        for v in data:
            if isinstance(v, basestring):
                data[data.index(v)] = format_string(v, ctx)
            else:
                replace_variables(v, ctx)
    elif isinstance(data, basestring):
        data = format_string(data, ctx)
    return data
