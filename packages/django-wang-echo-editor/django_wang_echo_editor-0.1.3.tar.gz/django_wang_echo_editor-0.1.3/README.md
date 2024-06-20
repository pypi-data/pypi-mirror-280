# django_wang_echo_editor 富文本编辑器
- 封装了wangEditor富文本编辑器，支持本地图片上传和OSS存储
wangEditor官方文档：https://www.wangeditor.com/
- 基于python3.10，django4.2版本进行测试
- 仅仅为了自己开发测试使用，存在不可遇见的bug

## 安装

1. 安装django_wang_echo_editor 

```shell
pip install django_wang_echo_editor
```

2. 在settings文件INSTALLED_APPS中添加“wang_editor”

```text
INSTALLED_APPS = [
    ...
    wang_editor,
]
```

3. 在settings中添加静态文件路径

```text
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

4. 在urls中添加静态文件对应的路由

```text
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    ...
    path('wang_editor/', include('wang_editor.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

## 使用

1.在模型models中使用

```python
from django.db import models
from wang_editor.fields import WangEditorField


class Article(models.Model):
    content = WangEditorField()
```

2.使用本地上传图片

- 在settings中添加媒体文件路径

```text
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

- 在urls中添加媒体文件路径

```text
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

3.config配置

```python
WANG_EDITOR_CONFIG = {
    'upload': '',  # 本地服务器上传路径，以MEDIA_URL为基础
    'storage_backend': '',  # 使用OSS存储
    'custom_css': [],  # 自定义css
    'custom_js': [],  # 自定义js
    'origin_js': '',  # wangEditor的js文件,
    'toolbar_config': {},  # 工具栏配置
    'editor_config': {}  # 编辑器配置
}
```
- toolbar_config和editor_config的配置参考wangEditor官方文档
```text
https://www.wangeditor.com/
```
- 如果配置了storage_backend，则upload配置无效

4.支持图片和视频上传到OSS之类的存储
在配置文件中添加storage_backend配置，值为存储后端的类路径，如：

```python
WANG_EDITOR_CONFIG = {
    'storage_backend': 'wang_editor.backends.aliyun.AliyunOSSBackend'
}
```