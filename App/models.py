from django.db import models

class Record(models.Model):
  PRODUCTS = (
    ('Large Fruit', 'Large Fruit'),
    ('Medium Fruit', 'Medium Fruit'),
    ('Small Fruit', 'Small Fruit'),
    ('Parfait', 'Parfait'),
    ('Grilled Wrap', 'Grilled Wrap'),
    ('Spicy Wrap', 'Spicy Wrap'),
    ('Kale Salad', 'Kale Salad'),
    ('Market Salad', 'Market Salad'),
    ('Southwest Salad', 'Southwest Salad'),
    ('Cobb Salad', 'Cobb Salad'),
    ('Side Salad', 'Side Salad'),
  )

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
  
  product = models.CharField(max_length=100, choices=PRODUCTS)
  quantity = models.CharField(max_length=100, choices=QUANTITYS)
  done = models.BooleanField(default=False)
  date = models.DateField()
  # creation_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.product} - {self.date}"
  
class Production(models.Model):
  product = models.ForeignKey(Record, on_delete=models.CASCADE)
  quantity = models.CharField(max_length=100)
  done = models.BooleanField(default=False)
  date = models.DateField()
  # creation_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.product} - {self.date}"