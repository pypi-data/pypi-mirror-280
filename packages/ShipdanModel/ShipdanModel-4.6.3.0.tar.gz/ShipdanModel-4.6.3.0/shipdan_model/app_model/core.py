from django.db import models


class DeployRestTime(models.Model):
    """
    배포시 사용하는 데이터. 생성하지말고 finished_at을 변경하는 방식
    code
    - -3000인 경우 : 전체 서버 점검
    - -3001인 경우 : /api/diet에 대한 api만 사용불가
    """
    finished_at = models.DateTimeField()
    code = models.IntegerField(default=-3000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'core_deployresttime'


class AppVersion(models.Model):
    """
    모바일 앱 강제 버전 업데이트용 테이블
    장고 어드민에서 값 변경
    {year}_{month}_{version}순으로 해당 값보다 값이 작으면 강제 업데이트 시키는 화면 노출
    """
    ANDROID = 1
    IOS = 2
    APP_OS = (
        (ANDROID, 'android'),
        (IOS, 'ios')
    )

    app_os = models.IntegerField(choices=APP_OS)
    latest_version = models.CharField(max_length=10)
    required_version = models.CharField(max_length=10)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'core_appversion'


class AppTutorialSwitch(models.Model):
    """
    24.6.24 deprecated
    2022년에 사용한 모델
    """
    on = models.BooleanField(default=True)

    class Meta:
        db_table = 'core_apptutorialswitch'
