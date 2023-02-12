from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title='Cortex APP',
      default_version='v1',
      description='Swagger UI for REST API',
      contact=openapi.Contact(name='Telegram', url='https://t.me/SerNikolasFlamel'),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
