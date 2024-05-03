from django.db import models

# Create your models here.

class StartUp_Model(models.Model):
    
    countries_ids = [
    ("001", "Algeria"),
    ("002", "Angola"),
    ("003", "Benin"),
    ("004", "Botswana"),
    ("005", "Burkina Faso"),
    ("006", "Burundi"),
    ("007", "Cameroon"),
    ("059", "Canary Islands"),
    ("008", "Cape Verde"),
    ("009", "Central African Republic"),
    ("010", "Chad"),
    ("057", "Congo"),
    ("012", "Cote d'Ivoire"),
    ("013", "Democratic Republic of the Congo"),
    ("014", "Djibouti"),
    ("015", "Egypt"),
    ("016", "Equatorial Guinea"),
    ("017", "Eritrea"),
    ("018", "Ethiopia"),
    ("019", "Gabon"),
    ("056", "Gambia"),
    ("020", "Ghana"),
    ("021", "Guinea"),
    ("022", "Guinea-Bissau"),
    ("023", "Kenya"),
    ("024", "Lesotho"),
    ("025", "Liberia"),
    ("026", "Libya"),
    ("027", "Madagascar"),
    ("028", "Malawi"),
    ("029", "Mali"),
    ("030", "Mauritania"),
    ("058", "Mauritius"),
    ("032", "Morocco"),
    ("033", "Mozambique"),
    ("034", "Namibia"),
    ("035", "Niger"),
    ("036", "Nigeria"),
    ("038", "Rwanda"),
    ("040", "Sao Tome and Principe"),
    ("041", "Senegal"),
    ("042", "Seychelles"),
    ("043", "Sierra Leone"),
    ("044", "Somalia"),
    ("045", "South Africa"),
    ("060", "South Sudan"),
    ("046", "Sudan"),
    ("047", "Swaziland"),
    ("048", "Tanzania"),
    ("049", "Togo"),
    ("051", "Tunisia"),
    ("052", "Uganda"),
    ("011", "Union of Comoros"),
    ("053", "Western Sahara"),
    ("054", "Zambia"),
    ("055", "Zimbabwe")
]

    Startup_name = models.CharField(max_length=100)
    country_id = models.CharField(choices= countries_ids , max_length=20)
    About = models.TextField(max_length=1000)
    HQ_city = models.CharField(max_length=20)
    HQ_country = models.CharField(max_length=20) #country
    industry = models.CharField(max_length=30)
    sub_industry = models.CharField(max_length=100)
    founded = models.IntegerField()
    no_of_employees = models.CharField(max_length=10)
    latest_stage = models.CharField(max_length=20)
    investors = models.CharField(max_length=100 , blank= True , null= True)
    total_raised = models.CharField(max_length=20 , blank= True , null= True)
    business_model = models.CharField(max_length=30 , blank= True , null= True)
    Startup_ID = models.IntegerField()
    Extra_data = models.TextField(max_length=1000 , blank= True , null= True)
    Attached_files = models.FileField(blank= True , null= True)



