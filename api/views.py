from api.models import App, User, AppGrp
from api.serializers import AppSerializer, UserSerializer, AppGrpSerializer
# from rest_framework import generics
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.pagination import PageNumberPagination
import time, re, urllib3, base64, json



#自定义类

#gitlab
class GitLabAct(object):
    def __init__(self, gitlab_id):
        self.gitlab_id = gitlab_id
        self.token = 'DKqR6HK-ktaiWUiRM4xF'
        self.url = 'http://gitlab.corp.fruitday.com/api/v4/projects/'

    def get_modules(self):
        url = self.url + self.gitlab_id + '/repository/files/pom.xml?ref=master'
        http = urllib3.PoolManager()
        try:
            response = http.request('GET', url, headers={'PRIVATE-TOKEN': self.token})
            if response.status == 200:
                content = bytes.decode(base64.b64decode(json.loads(bytes.decode(response.data))['content']))
                modules_list = re.findall('<module>(.*)</module>', content)
                return modules_list
            else:
                return []
        except Exception as e:
            return []
                # '发生错误: 无法获取Modules' + e.__str__()

#自定义视图

#gitlab
def gitlab_get_modules(request):
    if request.method == 'GET':
        gitlab_id = request.GET.get('gitlab_id')
        git = GitLabAct(gitlab_id)
        modules = json.dumps(git.get_modules())
        # if modules:
        #     modules = json.dumps(modules)
        return HttpResponse(modules, content_type="application/json")
        # else:
        #     return HttpResponse('can not find file pom.xml', status=404)
    return HttpResponse('wrong request method', status=400)


#自定义分页类
class AppGrpPageNumberPagination(PageNumberPagination):
    page_size = 5
    # max_page_size = 5
    page_size_query_param = 'size'
    page_query_param = 'page'

class AppPageNumberPagination(PageNumberPagination):
    # max_page_size = 5
    page_size_query_param = 'size'
    page_query_param = 'page'



#restful api
class AppGrpViewSet(viewsets.ModelViewSet):
    queryset = AppGrp.objects.all()
    serializer_class = AppGrpSerializer
    pagination_class = AppGrpPageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name',)


class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    pagination_class = AppPageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'type', 'group', )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', )


#测试试图

def test(request):
    print(request.POST)
    print('*'*12)
    print(request.META)
    time.sleep(3)
    return HttpResponse('ok')
