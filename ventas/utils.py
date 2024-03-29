from django.forms.utils import ErrorList
from django.http import JsonResponse
from django.views.generic.edit import ModelFormMixin


class LiErrorList(ErrorList):
    def __str__(self):
        return self.as_lis()

    def as_lis(self):
        if not self: return ''
        return '<ul class="errorlist">%s</ul>' % ''.join(
            ['<li class="text-danger">%s</li>' % e for e in self])


class BaseInlineModelFormMixin(ModelFormMixin):
    inline_initial = []
    inline_prefix = None
    inlines = []

    def get_inline_initial(self):
        return self.inline_initial.copy()

    def get_inline_form_class(self):
        pass
        # for inline in self.inlines:
        #     setattr(self, 'inline')

    def get_inline_prefix(self):
        return self.inline_prefix

    def get_form_inline(self, inline_form_class=None):
        if inline_form_class is None:
            inline_form_class = self.get_inline_form_class()
        return inline_form_class(**self.get_form_inline_kwargs())

    def get_form_inline_kwargs(self):
        kwargs = {
            'initial': self.get_inline_initial(),
            'prefix': self.get_inline_prefix(),
            'error_class': LiErrorList
        }

        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs


class JSONResponseMixin:
    def render_to_json_response(self, context, **response_kwargs):
        return JsonResponse(
            self.get_data(context),
            **response_kwargs
        )

    def get_data(self, context):
        return context
