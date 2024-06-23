import uuid
from django.db import models

# Base Model
class BaseModel(models.Model):
    """
    BaseModel contains the common fields for all models.
    """
    created_at = models.DateTimeField('Created At', auto_now_add=True, null=True)
    updated_at = models.DateTimeField('Updated At', auto_now=True, null=True)

    class Meta:
        abstract = True

# NiceAuthRequest Model
class NiceAuthRequest(BaseModel):
    """
    NiceAuthRequest stores information for the authentication request.
    """
    AUTH_TYPE_CHOICES = [
        ('M', 'Mobile Authentication'),
        ('C', 'Card Verification Authentication'),
        ('X', 'Certificate Authentication'),
        ('U', 'Joint Certificate Authentication'),
        ('F', 'Financial Certificate Authentication'),
        ('S', 'PASS Certificate Authentication'),
    ]

    POPUPYN_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]

    request_no = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    enc_data = models.TextField(
        'Encrypted Data',
        help_text="Encrypted data for the request."
    )
    integrity_value = models.TextField(
        'Integrity Value',
        help_text="Integrity value for the request."
    )
    token_version_id = models.CharField(
        'Token Version ID',
        max_length=100,
        help_text="Token version ID used in the request."
    )
    key = models.CharField(
        'Key',
        max_length=32,
        help_text="Key for encryption."
    )
    iv = models.CharField(
        'Initialization Vector (IV)',
        max_length=32,
        help_text="Initialization Vector (IV) for encryption."
    )
    authtype = models.CharField(
        'Authentication Type',
        max_length=1,
        choices=AUTH_TYPE_CHOICES,
        null=True,
        blank=True,
        help_text="Type of authentication (e.g., M for mobile)."
    )
    popupyn = models.CharField(
        'Popup Flag',
        max_length=1,
        choices=POPUPYN_CHOICES,
        null=True,
        blank=True,
        help_text="Flag to indicate if popup is used (Y/N)."
    )
    return_url = models.URLField(
        'Return URL',
        max_length=200,
        null=True,
        blank=True,
        help_text="URL to return to after authentication."
    )
    redirect_url = models.URLField(
        'Redirect URL',
        max_length=200,
        null=True,
        blank=True,
        help_text="URL to redirect to after authentication."
    )
    is_verified = models.BooleanField(default=False, help_text="Verification status")

    class Meta:
        verbose_name = 'Nice Auth Request'
        verbose_name_plural = 'Nice Auth Requests'
        ordering = ['-created_at']


# NiceAuthResult Model
class NiceAuthResult(BaseModel):  # 상속받도록 수정
    request = models.OneToOneField(
        NiceAuthRequest,
        on_delete=models.CASCADE,
        verbose_name='Related Request',
        help_text="Reference to the related NiceAuthRequest."
    )
    result = models.JSONField(
        'Result',
        help_text="Result of the authentication request in JSON format."
    )
    request_no = models.UUIDField(
        'Request Number',
        help_text="Unique request number for the authentication request.",
        default=uuid.uuid4  # 기본값 추가
    )
    enc_data = models.TextField(
        'Encrypted Data',
        help_text="Encrypted data for the request.",
        default=''  # 기본값 추가
    )
    is_verified = models.BooleanField(
        default=False,
        help_text="Verification status"
    )
    birthdate = models.CharField(
        'Birthdate',
        max_length=8,
        blank=True,
        null=True,
        help_text='Birthdate of the user in YYYYMMDD format.'
    )
    gender = models.CharField(
        'Gender',
        max_length=1,
        blank=True,
        null=True,
        help_text='Gender of the user. 1 for male, 2 for female.'
    )
    di = models.CharField(
        'DI',
        max_length=255,
        blank=True,
        null=True,
        help_text='DI (Duplication Information) value.'
    )
    mobileco = models.CharField(
        'Mobile Carrier',
        max_length=1,
        blank=True,
        null=True,
        help_text='Mobile carrier code.'
    )
    receivedata = models.TextField(
        'Receive Data',
        blank=True,
        null=True,
        help_text='Additional data received from the authentication.'
    )
    mobileno = models.CharField(
        'Mobile Number',
        max_length=11,
        blank=True,
        null=True,
        help_text='Mobile number of the user.'
    )
    nationalinfo = models.CharField(
        'National Info',
        max_length=1,
        blank=True,
        null=True,
        help_text='National information code.'
    )
    authtype = models.CharField(
        'Authentication Type',
        max_length=1,
        blank=True,
        null=True,
        help_text='Type of authentication performed.'
    )
    sitecode = models.CharField(
        'Site Code',
        max_length=255,
        blank=True,
        null=True,
        help_text='Site code where the authentication was performed.'
    )
    utf8_name = models.CharField(
        'UTF8 Name',
        max_length=255,
        blank=True,
        null=True,
        help_text='UTF8 encoded name of the user.'
    )
    enctime = models.CharField(
        'Encryption Time',
        max_length=14,
        blank=True,
        null=True,
        help_text='Time when the data was encrypted in YYYYMMDDHHMMSS format.'
    )
    name = models.CharField(
        'Name',
        max_length=255,
        blank=True,
        null=True,
        help_text='Name of the user.'
    )
    resultcode = models.CharField(
        'Result Code',
        max_length=4,
        blank=True,
        null=True,
        help_text='Result code of the authentication.'
    )

    class Meta:
        verbose_name = 'Nice Auth Result'
        verbose_name_plural = 'Nice Auth Results'
        ordering = ['-created_at']  # ordering 필드 수정
