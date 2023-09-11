from django.db import models
from django.contrib.auth.models  import User
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.utils.text import slugify
from datetime import datetime as dt
# Create your models here.


# first arg for databse , sevond one for admin page

class Profile(models.Model):
    doctor_specialist_list = (
        ("جلديه","جلديه"),
        ("عظام","عظام"),
        ("اسنان","اسنان"),
        ("باطنه","باطنه"),
        )
    
    gender_list = (
        ("M","Male"),
        ("F","Female")
        )
    
    user     = models.OneToOneField(User , verbose_name=_("user") , on_delete=models.CASCADE)
    
    name     = models.CharField(_('ألاسم : '),max_length=50)
    
    subtitle = models.CharField(_("نبذه عنك"),max_length=50)
    
    address  = models.CharField(_("محافظتك"),max_length=50)
    
    address_detail = models.CharField(_("عنوانك"),max_length=50)
    
    number_phone   = models.CharField(_("الهاتف"),max_length=50)
    
    working_hours  = models.CharField(_("عدد ساعات عملك "),max_length=50)
    
    wating_time    = models.IntegerField(_("مده الانتظار"),blank=True,null=True)
    
    who_i      = models.TextField(_('منا انا : '),max_length=250,blank=True,null=True)
    
    price      = models.IntegerField(_('سعر الكشف : '),blank=True,null=True)
    
    image      = models.ImageField(upload_to='media/profile_photos',blank=True,null=True)
    
    doctor     =  models.CharField(_("دكتور؟"),choices=doctor_specialist_list , max_length=50,blank=True,null=True)
    
    specialist =  models.CharField(_("تخصصك"),max_length=50,blank=True,null=True)
    
    jous_time  =  models.DateTimeField(_(" "),auto_now_add=True,null=True)
    
    gender     =  models.CharField(_("جنسك"),max_length=50,choices=gender_list)
    
    slug       = models.SlugField(_('slug'),blank=True,null=True)
    
    facebook   = models.CharField(_("حساب الفيس"),max_length=50,blank=True,null=True)
    
    twitter    = models.CharField(_("حساب تويتر"),max_length=50,blank=True,null=True)
    
    Google     = models.CharField(_("حساب جوجل"),max_length=50,blank=True,null=True)
  
    # auto_now the time of last update proceess
    # auto_now_add created time

    
    def save(self,*args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username) 
        super (Profile ,self).save(*args , **kwargs)
    
   
        
    class Meta:
        verbose_name = ('Profile')
        verbose_name_plural = ('Profiles')
        
    def __str__(self):
        return '%s' %(self.user.username)
        
def create_profile(sender , **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])
        
post_save.connect(create_profile , sender = User)
        
    
    
