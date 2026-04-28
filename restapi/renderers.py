from rest_framework.renderers import JSONRenderer

class EnvelopeJSONRenderer(JSONRenderer):
    """
    Custom JSON Renderer that wraps all responses in a standard envelope.
    This ensures that HTML forms in the Browsable API still get the raw data
    and can pre-populate fields correctly, while actual JSON responses get wrapped.
    """
    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = 200
        if renderer_context and "response" in renderer_context:
            status_code = renderer_context["response"].status_code

        # If data is already wrapped (e.g. from a custom view override), don't double-wrap
        if isinstance(data, dict) and "status" in data and "data" in data:
            return super().render(data, accepted_media_type, renderer_context)

        # Build the envelope
        if status_code >= 400:
            envelope = {
                "status": "error",
                "message": "An error occurred." if status_code >= 500 else "Validation failed.",
                "data": data
            }
        else:
            envelope = {
                "status": "success",
                "message": "Request successful.",
                "data": data
            }

        return super().render(envelope, accepted_media_type, renderer_context)
