from enum import Enum

class OrderStatus(Enum) : #Estado de la orden
    CREATED = 'CREATED'
    PAYED = 'PAYED'
    COMPLETED = 'COMPLETED'
    CANCELED = 'CANCELED'

#lista de tuplas
choices = [(tag, tag.value) for tag in OrderStatus ]