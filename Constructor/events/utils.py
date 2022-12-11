class MyMixin(object):
    mixin_title = ''

    def get_mixin_title(self, s):
        if isinstance(s, str):
            return s.upper()
        else:
            return s.title.upper()
