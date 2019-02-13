def strip_suffix(text, suffix):
    if not text.endswith(suffix):
        return text
    return text[:len(text) - len(suffix)]


def strip_prefix(text, prefix):
    if not text.startswith(prefix):
        return text
    return text[len(prefix):]


class FilterModule(object):
    def filters(self):
        return {
            'kibana_strip_suffix': strip_suffix,
            'kibana_strip_prefix': strip_prefix,
        }
