from django.db import models

CAT_FLO_TYPE = (
    ('iris-setosa', 'Iris-setosa'),
    ('iris-virginica', 'Iris-virginica'),
    ('iris-versicolor', 'Iris-versicolor'),
)


class RawFlower(models.Model):

    # Just a number for the sample
    PIN_ID = models.CharField(max_length=100)

    # Result: value in cm
    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()

    # The type of flower
    type_field = models.CharField(max_length=100, choices=CAT_FLO_TYPE)