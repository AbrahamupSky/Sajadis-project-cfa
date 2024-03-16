from django.db import models

class Record(models.Model):
  
  QUANTITYS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19'),
    ('20', '20'),
  )

  Large_Fruit = models.CharField(max_length=20, choices=QUANTITYS)
  Medium_Fruit= models.CharField(max_length=20, choices=QUANTITYS)
  Small_Fruit = models.CharField(max_length=20, choices=QUANTITYS)
  Parfait = models.CharField(max_length=20, choices=QUANTITYS)
  Grilled_Wrap = models.CharField(max_length=20, choices=QUANTITYS)
  Spicy_Wrap = models.CharField(max_length=20, choices=QUANTITYS)
  Kale_Salad = models.CharField(max_length=20, choices=QUANTITYS)
  Market_Salad = models.CharField(max_length=20, choices=QUANTITYS)
  Southwaest_Salad = models.CharField(max_length=20, choices=QUANTITYS)
  Cobb_Salad = models.CharField(max_length=20, choices=QUANTITYS)
  Side_Salad = models.CharField(max_length=20, choices=QUANTITYS)

  done = models.BooleanField(default=False)
  date = models.DateField()
  # creation_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return str(f'{self.date} - {self.done}')