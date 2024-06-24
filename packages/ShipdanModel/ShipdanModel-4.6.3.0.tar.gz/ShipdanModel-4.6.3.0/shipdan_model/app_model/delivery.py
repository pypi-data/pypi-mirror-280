from django.db import models


class Delivery(models.Model):
    """
    2024.6.24
    price외에 [invoice_no, company_code, item_name, address, estimate, complete] 사용하지 않음
    """
    invoice_no = models.TextField(help_text='운송장번호')
    company_code = models.TextField(blank=True, help_text='택배사 코드')
    item_name = models.TextField(help_text='상품 이름', blank=True)
    address = models.TextField(help_text='주소', blank=True)
    estimate = models.TextField(help_text='배송 예정시간', blank=True)
    complete = models.BooleanField(default=False)
    price = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'delivery_delivery'


class DeliveryLog(models.Model):
    """
    2024.6.24 deprecated
    2022년 12월 이후로 사용하지 않음. 기존에는 Delivery별 로그를 저장하려고 했으나, 새벽배송의 특징상 log를 받을 수 없음.
    """
    UNDEFINED = 0
    DELIVERY_PREPARATION = 1
    COLLECTION_COMPLETED = 2
    DELIVERY_PROGRESS = 3
    BRANCH_ARRIVAL = 4
    DELIVERY_DEPARTURE = 5
    DELIVERY_ARRIVAL = 6
    DELIVERY_ERROR = -99
    LEVELS = (
        (UNDEFINED, '미정'),
        (DELIVERY_PREPARATION, '배송준비'),
        (COLLECTION_COMPLETED, '집하완료'),
        (DELIVERY_PROGRESS, '배송진행'),
        (BRANCH_ARRIVAL, '지점도착'),
        (DELIVERY_DEPARTURE, '배송출발'),
        (DELIVERY_ARRIVAL, '배송도착'),
        (DELIVERY_ERROR, '배송스캔오류'),
    )
    LEVEL_DICT = {
        UNDEFINED: '미정',
        DELIVERY_PREPARATION: '배송준비',
        COLLECTION_COMPLETED: '집하완료',
        DELIVERY_PROGRESS: '배송진행',
        BRANCH_ARRIVAL: '지점도착',
        DELIVERY_DEPARTURE: '배송출발',
        DELIVERY_ARRIVAL: '배송도착',
        DELIVERY_ERROR: '배송스캔오류',
    }

    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, related_name='logs')
    level = models.IntegerField(choices=LEVELS, default=UNDEFINED)
    time = models.DateTimeField(null=True, blank=True)
    telno = models.TextField(blank=True, default='')
    manPic = models.TextField(blank=True, default='')
    manName = models.TextField(blank=True, default='')
    remark = models.TextField(blank=True, default='')
    where = models.TextField(blank=True, default='')
    kind = models.TextField(blank=True, default='')

    class Meta:
        db_table = 'delivery_deliverylog'


class PossibleAddress(models.Model):
    """
    24.6.24 deprecated
    원래는 데이터로 저장을 하려다가 팀프래시에 요청하는 방식으로 변경함에 따라 사용하지 않음.
    """
    zonecode = models.CharField(max_length=10, verbose_name='우편번호')
    sido = models.CharField(max_length=10, verbose_name='도/시 이름')
    sigungu = models.CharField(max_length=10, verbose_name='시/군/구 이름')
    bcode = models.PositiveBigIntegerField(unique=True, verbose_name='법정동코드')
    bname = models.CharField(max_length=20, verbose_name='법정동/법정리 이름', blank=True, null=True)
    roadAddress = models.CharField(max_length=50, verbose_name='도로명', blank=True, null=True)
    is_possible = models.BooleanField(default=True)

    class Meta:
        db_table = 'delivery_possibleaddress'


class DeliveryPolicy(models.Model):
    """
    장고 어드민에서 배송비 관련 처리 변경.
    24.6.24 현재 값
    {"delivery_price": 3000, "delivery_free_criteria_price": 40000}
    """
    data = models.JSONField(default=dict)  # 추후 기획 변동 가능성 고려 > 유동적 설계
    target = models.CharField(max_length=255)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        db_table = 'delivery_deliverypolicy'
