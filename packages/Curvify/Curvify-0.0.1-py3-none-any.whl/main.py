"""
A  module for ploting Curves

.. module:: Curve

.. moduleauthor:: Cjenf

"""

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np


class Parabola:
    """Represents a Parabolic 


    Args:
        x(np.ndarray): x-coordinates of the ndarray
        a(int): a parameter of the parabola
        b(int): b parameter of the parabola
        h(int): h parameter of the parabola
        k(int): k parameter of the parabola
        direction(str): direction of the parabola
        directrix(bool): directrix of the parabola

    Returns:
        None
    
    """
    def __init__(
            self, 
            x: np.ndarray,
            a: int,
            b: int, 
            h:int,
            k:int,
            direction:str,
            directrix: bool
    ) -> None:
        
        self._x = x
        self._a = a
        self._b = b
        self._h=h
        self._k=k
        self._direction=direction
        if self._direction in ["up/down", "up", "down"]:
            self._y = a * (x - h)**2 + k
            if h and k==0:
                self._c=0
            else:
                self._c=(h**2/k)/4
        elif self._direction in ["left/right","left" ,"right"]:
            self._y = np.sqrt(a*(x - h) / a)+k
            self._yf = -np.sqrt(a*(x - h) / a)+k
            print(self._yf)
            if h and k==0:
                self._c=0
            else:
                self._c=(h**2/k)/4
        
        self._d = directrix
    
    def draw(self) -> None:
        """Draws the parabola"""
        if self._direction in ["up/down", "up", "down"]:
            plt.plot(self._x, self._y, label="Parabola")
            
        elif self._direction in ["left/right","left" ,"right"]:
            plt.plot(self._x, self._y, label="Parabola")
            plt.plot(self._x, self._yf, label="Parabola")
       
        if self._d:
            if self._direction in ["up/down", "up", "down"]:
                self.d_=self._k-self._c
                plt.axhline(self.d_, color='#706666', label="Directrix")
                
            elif self._direction in ["left/right","left" ,"right"]:
                self.d_=self._h-self._c
                plt.axvline(self.d_, color='#706666', label="Directrix")
                
        plt.show()

    @property
    def vertex(self) -> tuple:
        """Returns the vertex of the parabola"""
        return (self._h, self._k)

    @property
    def focus(self) -> tuple:
        """Returns the focus of the parabola"""
        if self._direction in ["up/down", "up", "down"]:
            return (self._h, self._k + self._c)
        elif self._direction in ["left/right","left" ,"right"]:
            return (self._h+self._c, self._k)

    @property
    def directrix(self) -> tuple: 
        """Returns the directrix of the parabola"""
        if self._direction in ["up/down", "up", "down"]:
            return self._d
        elif self._direction in ["left/right","left" ,"right"]:
            return self._d
    @property
    def axis_equation(self) -> str:
        """Returns the axis equation of the parabola"""
        if self._direction in ["up/down", "up", "down"]:
            return "x-{}=0".format(self._h)
        elif self._direction in ["left/right","left" ,"right"]:
            return "y-{}=0".format(self._k)
        
    @property
    def latus_rectum(self) -> int:
        """Returns the latus rectum of the parabola"""
        return 4*abs(self._c)
    
class Hyperbola:
    """Represents a Hyperbola
    

    Args:
        x(np.ndarray): x-coordinates of the ndarray
        a(int): a parameter of the hyperbola
        b(int): b parameter of the hyperbola
        h(int): h parameter of the hyperbola
        k(int): k parameter of the hyperbola
        direction(str): direction of the hyperbola

    Returns:
        None
    
    """
    def __init__(
            self, 
            x: np.ndarray,
            a: int,
            b: int, 
            h:int,
            k:int,
            direction: str
        ) -> None:

        self._x = x
        self._a = a
        self._b = b
        self._h=h
        self._k=k
        self._direction = direction

        
        self._y1 = k + b * np.sqrt(1 + ((x - h) / a)**2)
        self._y2 = k - b * np.sqrt(1 + ((x - h) / a)**2)
        

    def draw(self) -> None:
        """
        Draws the hyperbola
        """
        if self._direction=="up/down" | "up" | "down":
            plt.plot(self._x, self._y1)
            plt.plot(self._x, self._y2)
            plt.show()
        elif self._direction=="right/left" | "left" | "right":
            plt.plot(self._y1, self._x)
            plt.plot(self._y2, self._x)
            plt.show()

    def center(self) -> tuple:
        """Returns the center of the hyperbola"""
        return (self._h, self._k)
    
    def vertex(self) -> tuple:
        """Returns the vertex of the hyperbola"""
        return (self._h,self._k +self._b),(self._h, self._k - self._b) if self._direction=="left/right" else (self._h+self._b,self._k),(self._h-self._b,self._k)
    def focus(self) -> tuple:
        """Returns the focus of the hyperbola"""
        focal_length = np.sqrt(self._a**2 + self._b**2)
        return (self._h + focal_length, self._k ), (self._h-focal_length, self._k) if self._direction=="left/right" else (self._h, self._k + focal_length),(self._h, self._k - focal_length)
    
    def transverse_axis_length(self) -> int:
        """Returns the transverse axis length of the hyperbola"""
        return self._a*2
    
    def conjugate_axis_length(self) -> int:
        """Returns the conjugate axis length of the hyperbola"""
        return self._b*2
    

class ellipse:
    """Represents an ellipse


    Args:
        center_x(int): x-coordinate of the center
        center_y(int): y-coordinate of the center
        x_width(int): width of the ellipse
        y_height(int): height of the ellipse
        
    Returns:
        None
    """
    def __init__(
            self, 
            center_x: int,
            center_y: int,
            x_width: int, 
            y_height:int,
        ) -> None:

        self._center_x = center_x
        self._center_y = center_y
        self._x_width = x_width
        self._y_height = y_height

        ellipse = Ellipse(
                (
                center_x, 
                center_y
            ), 
            x_width, 
            y_height, 
            edgecolor='b',
            facecolor='none'
        )
        
        fig, ax = plt.subplots()
        ax.add_patch(ellipse)

        ax.set_xlim(center_x - x_width / 2 - 1, center_x + x_width / 2 + 1)
        ax.set_ylim(center_y - y_height / 2 - 1, center_y + y_height / 2 + 1)
    
    def draw(self) -> None:
        """
        Draws the ellipse
        """
        plt.show()
    @property
    def center(self) -> tuple:
        """Returns the center of the ellipse"""
        return (self._center_x, self._center_y)