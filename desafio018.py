import math
ang = float(input('Diga um ângulo: '))
sin = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(' O ângulo {} possui: Seno = {:.1f}, Coseno = {:.1f} e a Tangente = {:.1f}. ' .format(ang, sin, cos, tan))
