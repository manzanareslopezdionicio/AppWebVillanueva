class login:
    def __init__(self, usuario, password):
        self.usuario = usuario
        self.password = password
    def toDBCollection(self):
        return{
            'usuario' : self.usuario,
            'password' : self.password
        }
        