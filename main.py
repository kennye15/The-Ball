from kivy.app import App
from kivy.graphics import Color, Line, Rectangle, Ellipse
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

class WidgetsExample(GridLayout):
    count = 0
    count_enabled = BooleanProperty(False)
    my_text = StringProperty(str(int(count)))
    slider_value_txt = StringProperty("value")
    text_input_str = StringProperty("foo")

    def on_button_click1(self):
        if self.count_enabled:
            self.count += 1
            self.my_text = str(int(self.count))

    def on_button_click2(self):
        if self.count_enabled:
            self.count -= 1
            self.my_text = str(int(self.count))

    def on_button_click3(self, widget):
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True

    def on_button_click4(self, widget):
        print("Switch: " + str(widget.active))

    def on_button_click5(self, widget):
        print("Slider: " + str(int(widget.value)))
        self.slider_value_txt = str(int(widget.value))

    def on_text_validate(self, widget):
        self.text_input_str = widget.text

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass
    # def build(self):
        # self.icon = "Logo.png"
        # image = Loader.image('mysprite.png')

class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample3(Widget):
    pass

class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(point=(100, 100, 400, 500), wiqth=2)
            Color(0, 1, 0)
            Line(circle=(400, 100, 80), wiqth=2)
            Line(rectangle=(700, 500, 150, 100), wiqth=5)
            Rectangle(pos=(700, 200), size=(150, 100))

class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)
        self.vy = dp(3)
        with self.canvas:
            self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))
        Clock.schedule_interval(self.update, 1/60)  # from kivy.properties import Clock

    def on_size(self, *args):
        self.ball.pos = (self.center_x-self.ball_size/2, self.center_y-self.ball_size/2)

    def update(self, dt):
        x, y = self.ball.pos

        x += self.vx
        y += self.vy

        # self.ball_size / self.width
        # self.vx = - self.vx
        if y + self.ball_size > self.height:
            y = self.height-self.ball_size
            self.vy = -self.vy
        if x + self.ball_size > self.width:
            x = self.width-self.ball_size
            self.vx = -self.vx
        if y < 0:
            y = 0
            self.vy = -self.vy
        if x < 0:
            x = 0
            self.vx = -self.vx
        self.ball.pos = (x, y)

TheLabApp().run()