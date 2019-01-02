from api.models import App, User, AppGrp
from api.serializers import AppSerializer, UserSerializer, AppGrpSerializer
# from rest_framework import generics
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.pagination import PageNumberPagination
import os, time, re, urllib3, base64, json, subprocess
from git import *


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

#deploy
class DeployAct(object):
    def __init__(self, app_seq, app_name, module, gitlab_id, git_url, short_id, branch, env, type):
        self.base_path = '/Users/brande/PycharmProjects/cookbook_and_code/ops_backend/data/'
        self.scripts_path = self.base_path + 'scripts/'
        self.workspace = self.base_path + 'workspace/'
        self.log_path = self.base_path + 'logs/'
        self.app_name = app_name
        self.module = module
        self.gitlab_id = gitlab_id
        self.git_url = git_url
        self.short_id = short_id
        self.branch = branch
        self.env = env
        self.type = type
        self.tag = module + '-' + branch + '-' + short_id + '-' + str(app_seq + 1)
        #workspace
        self.app_workspace = self.workspace + self.app_name
        #package_path
        self.package_path = self.base_path + 'package/' + self.app_name + '/' + self.tag + '/'
        #log_info
        self.package_log_path = self.log_path + '/package/' + self.app_name + '/'
        self.package_log = self.package_log_path + self.tag + '.log'
        #scpits_info
        self.package_sh = self.scripts_path + 'package.sh'

    def init_repo(self):
        if not os.path.exists(self.app_workspace):
            os.chdir(self.workspace)
            os.system('/usr/bin/git clone {0}'.format(self.git_url))
        repo = Repo(self.app_workspace)
        git = repo.git
        git.clean('-xdf')
        git.checkout('-f', 'master')
        git.pull('--rebase')
        git.checkout('-f', self.short_id)


    def pack_repo(self):
        os.system('mkdir -p {0};mkdir -p {1}'.format(self.package_path, self.package_log_path))
        with open(self.package_log, 'w') as log_file:
            CompletedProcess = subprocess.run(self.package_sh + ' {0} {1} {2} {3} {4} {5}'.format(
                self.app_name, self.module, self.app_workspace, self.package_path, self.env, self.type)
                , shell=True, stdout=log_file, stderr=log_file, check=False)
        print(CompletedProcess)
        pass

    def release_repo(self):
        pass



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
