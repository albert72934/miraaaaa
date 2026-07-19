import pygame
import constantes

class Personaje():
    
  def __init__(self , x , y, imagen ):

      self.imagen = imagen
      self.forma = pygame.Rect(0, 0, constantes.ancho_personaje, constantes.alto_personaje)
      
      self.forma.center = (x,y)

  def movimiento(self,delta_x, delta_y):
      self.forma.x = self.forma.x + delta_x
      self.forma.y = self.forma.y + delta_y
  
  def dibujo(self,interfaz):
      interfaz.blit (self.imagen, self.forma)
       # pygame.draw.rect (interfaz, constantes.color_personaje,rect = self.forma )
