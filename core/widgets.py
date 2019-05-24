from django.forms import widgets
from django.template import loader
from django.utils.safestring import mark_safe

class emaCSSImageInput(widgets.FileInput):
    template_name = 'widgets/image-input.html'

    def get_context(self, name, value, attrs=None):
        return {'widget': {
            'name': name,
            'value': value,
        }}

    def render(self, name, value, attrs=None):
        context = self.get_context(name, value, attrs)
        template = loader.get_template(self.template_name).render(context)
        return mark_safe(template)

class emaCSSFileInput(widgets.FileInput):
    template_name = 'widgets/file-input.html'

    def get_context(self, name, value, attrs=None):
        return {
            'widget': {
                'name': name,
                'value': value,
            }
        }

    def render(self, name, value, attrs=None):
        context = self.get_context(name, value, attrs)
        template = loader.get_template(self.template_name).render(context)
        return mark_safe(template)


class emaCSSTextInput(widgets.Textarea):
    template_name = 'widgets/text-input.html'

    def get_context(self, name, value, attrs):
        context = super(emaCSSTextInput, self).get_context(name, value, attrs)
        context['widget']['attrs']['max_length'] = 2000
        return context
        """
        return {
            'widget': {
                'name': name,
                'value': value,
                'attrs': attrs,
            }
        }
        """

    def render(self, name, value, attrs):
        context = self.get_context(name, value, attrs)
        template = loader.get_template(self.template_name).render(context)
        return mark_safe(template)