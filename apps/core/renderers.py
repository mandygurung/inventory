from rest_framework.renderers import TemplateHTMLRenderer


class SerializerTemplateHTMLRenderer(TemplateHTMLRenderer):

    def get_template_context(self, data, renderer_context):
        data = super().get_template_context(data, renderer_context)

        data = {
            "users": list(data)
        }

        return data