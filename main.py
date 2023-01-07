import qrcode

#Crear instancia de codigo QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size= 10,
    border = 4,
)

datos = input("Ingre el texto a codificar en QR: ")
nombre = input("Ingrese el nombre de la salida: ")
#llenamos con los datos
qr.add_data(datos)
qr.make(fit=True)

#Crea una imagen de acuerdo a la instancia
img = qr.make_image()
img.save(f"./salida/{nombre}.jpeg")
    

"""
Error de corrección
Un código QR tiene capacidad de corrección de errores para restaurar datos si el código está dañado o sucio
. Hay cuatro niveles de corrección de errores disponibles con esta biblioteca, que se almacenan en el  qrcode.constantsobjeto:

ERROR_CORRECT_L: Se pueden corregir aproximadamente un 7% o menos de errores.
ERROR_CORRECT_M: (predeterminado) Se pueden corregir aproximadamente un 15% o menos de errores.
ERROR_CORRECT_Q: Se pueden corregir aproximadamente un 25% o menos de errores.
ERROR_CORRECT_H: Se pueden corregir aproximadamente un 30% o menos de errores.
    Deben proporcionarse como valor de la  error_correctionpropiedad durante la creación del Código QR.

Tamaño del código QR
Puede cambiar el tamaño del código QR generado con la box_sizepropiedad.
"""