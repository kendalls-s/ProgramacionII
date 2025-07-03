#Clase Boleto
class BoletoAvion :
    def __init__(self,valor,impuesto_salida,salida,llegada,ciudad,cliente):
        self.valor = valor
        self.impuesto_salida = impuesto_salida  
        self.salida = salida
        self.llegada = llegada
        self.ciudad = ciudad
        self.cliente = cliente

    @property
    def preciopagar(self):
        return self.impuesto_salida + self.valor
    
    
    def __str__(self):
        x = "Cliente: "+ str(self.cliente)+"\nCiudad: "+ str(self.ciudad)+"\nValor: "+str(self.valor)+"\nImpuesto: "+str(self.impuesto_salida)+"\nLlegada: "+self.llegada+"\nSalida: "+self.salida    
        return(x)
    
#Clase cliente 
class Cliente:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre}, {self.direccion}, {self.telefono}"

#Clase Ciudad
class Ciudad :
    def __init__(self, salida_destino, hora_actual):
        self.salida_destino = salida_destino
        self.hora_actual = hora_actual
    
    def __str__(self):
        return f"{self.salida_destino}, {self.hora_actual}"



class BoletoEjecutivo(BoletoAvion):
    def __init__(self, valor_boleto, impuesto_salida, hora_salida, hora_llegada, ciudad, cliente):
        super().__init__(valor_boleto, impuesto_salida, hora_salida, hora_llegada, ciudad, cliente)
        self.alimentos = [] 

    def agregar_alimento(self, alimento):
        self.alimentos.append(alimento)

    def total_alimento(self):
        total=0
        for producto in self.alimentos:
            total = total + producto.precio
        return total
    

    @property
    def precio_pagar(self):
        return self.valor+ self.total_alimento()+self.impuesto_salida


class BoletoClienteFrecuente(BoletoAvion):
    def __init__(self, valor_boleto, impuesto_salida, hora_salida, hora_llegada, ciudad, cliente, descuento):
        super().__init__(valor_boleto, impuesto_salida, hora_salida, hora_llegada, ciudad, cliente)
        self.descuento = descuento  

    @property
    def precio_pagar(self):
        return self.valor+ self.impuesto_salida - (self.valor * self.descuento)



class AlimentoExtra:
    def __init__(self, codigo, descripcion, precio):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio



    
            