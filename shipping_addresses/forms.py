from tkinter.tix import Form


from django.forms import ModelForm
from .models import ShippingAddress

class ShippingAddressForm(ModelForm):
    class Meta:
        model = ShippingAddress #se genera un formulario con nuestro model ShippingAddres
        fields = [   #y indicamos con fields que campos queremos usar
            'line1', 'line2', 'city', 'state', 'country', 'codpost', 'reference'
        ]
        # DICCIONARIO PARA MODIFICAR EL LABEL DE NUESTROS INPUTS
        #Se modifica en este caso line1 el cual es el input y se pone la modoficacion en este caso calle que es el label
        labels = {
            'line1': 'Direccion:',
            'line2': 'Telefono:',
            'city': 'Pais',
            'state': 'Ciudad:',
            'country': 'Localidad',
            'codpost': 'Codigo Postal:',
            'reference': 'Agregar Otra Informacion:'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    #literalmente es la forma de agregar estilos al formulario Atributo Widget
                                                #Es un diccionario y almacena los inputs del diccionario 
        self.fields['line1'].widget.attrs.update({
            'class': 'form-control'

        })        

        self.fields['line2'].widget.attrs.update({
            'class': 'form-control'

        })          

        self.fields['city'].widget.attrs.update({
            'class': 'form-control'

        })  

        self.fields['state'].widget.attrs.update({
            'class': 'form-control'

        })  

        self.fields['country'].widget.attrs.update({
            'class': 'form-control'

        })  

        self.fields['codpost'].widget.attrs.update({
        'class': 'form-control',
        'placeholder': '000000' 
        
         })  

        self.fields['reference'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'EMPRESA/CONJUNTO , APARTAMENTO/PISO'

        })  

