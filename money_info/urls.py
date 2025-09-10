from rest_framework import routers

from . import views


router = routers.SimpleRouter()

router.register(r'types', views.TypeAPIViewSet)
router.register(r'statuses', views.StatusAPIViewSet)
router.register(r'categories', views.CategoryAPIViewSet)
router.register(r'subcategories', views.SubCategoryAPIViewSet)

urlpatterns = router.urls
