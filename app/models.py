from django.db import models

 


# 瀹氫箟涓�涓簲鐢ㄧ被妯″瀷.
class Application(models.Model):   #鏂板缓涓�绫荤户鎵胯嚜models.Model,鏈夊鍚嶅拰骞撮緞,杩欓噷鐢ㄥ埌浜嗕袱绉岶ield.
	name =models.CharField(max_length=30)
	age =models.IntegerField()

# 瀹氫箟涓�涓枃绔犵被妯″瀷
class Article(models.Model):
	title =models.CharField(u'鏍囬',max_length=256)
	content =models.TextField(u'鍐呭')
	pub_time =models.DateTimeField(u'鍙戝竷鏃堕棿',auto_now_add=True,editable=True)
	update_time =models.DateTimeField(u'鏇存柊鏃堕棿',auto_now=True,null=True)

	def __str__(self):
		return self.title



# 瀹氫箟涓�涓綔鑰呯被妯″瀷
from django.utils.encoding import python_2_unicode_compatible
@python_2_unicode_compatible
#姝ゅ鍏煎python2
class Autor(models.Model):
	name =models.CharField(u'濮撳悕',max_length=256)
	sex =models.CharField(u'鎬у埆',max_length=5)
	info =models.TextField(u'绠�浠�')
	birth_time =models.DateTimeField(u'鍑虹敓骞存湀',editable=True)
	update_time =models.DateTimeField(u'鏇存柊鏃堕棿',auto_now=True,null=True)

	def __str__(self):
		return self.title


# 瀹氫箟鐢ㄦ埛绫绘ā鍨�
from django.utils.encoding import python_2_unicode_compatible
@python_2_unicode_compatible
#姝ゅ鍏煎python2
class User(models.Model):
	user_name =models.CharField(u'濮撳悕',max_length=256)
	user_longi =models.CharField(u'经度',max_length=25,null=True)
	user_lati =models.CharField(u'纬度',max_length=25,null=True)
	user_forbid = models.NullBooleanField(u'是否黑名单',null=True)
	user_photo= models.CharField(u'头像',max_length=256,null=True)
	user_descripe= models.CharField(u'描述',max_length=256,null=True)
	user_password =models.CharField(u'瀵嗙爜',max_length=16)
	user_email =models.EmailField(u'閭',max_length=30)
	user_sex =models.TextField(u'鎬у埆',max_length=5,null=True)
	user_addr =models.CharField(u'绠�浠�',max_length=256,null=True)
	user_birth =models.DateTimeField(u'鍑虹敓骞存湀',editable=True,null=True,auto_now_add=True)
	user_sign=models.CharField(u'签名',max_length=256,null=True)
	user_intro=models.CharField(u'介绍',max_length=512,null=True)

	#update_time =models.DateTimeField(u'鏇存柊鏃堕棿',auto_now=True,null=True)

	def __str__(self):
		return self.title