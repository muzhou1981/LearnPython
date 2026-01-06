import turtle
import math

# 参数：二次函数 y = a*x^2 + b*x + c
a, b, c = 0.2, 0, 0  # 可按需修改

# 显示范围（数学坐标系）
x_min, x_max = -20, 20
y_min, y_max = -15, 15

# 画布设置
screen = turtle.Screen()
screen.setup(900, 700)
screen.title("二次函数 y = a*x^2 + b*x + c")
screen.setworldcoordinates(x_min, y_min, x_max, y_max)

# 画笔共用设置
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(2)

# 画坐标轴
def draw_axes():
  pen.color("black")
  pen.penup()
  pen.goto(x_min, 0)
  pen.pendown()
  pen.goto(x_max, 0)  # x 轴

  # 将坐标轴刻度默认间隔强制设为 1（覆盖后续 draw_axes 中可能使用的 0.5）
  if 'draw_ticks' in globals():
    orig_draw_ticks = globals()['draw_ticks']
    def _force_tick_step(step=1):
      return orig_draw_ticks(step=1)
    globals()['draw_ticks'] = _force_tick_step

  pen.penup()
  # 关闭实时绘制以加速绘图，绘制完成后通过定时器在主循环开始时一次性刷新显示
  turtle.tracer(0)
  
  # 确保在绘制 y 轴之前移动到 y_min 并保持抬笔，避免从 x 轴右端绘制连线
  pen.goto(0, y_min)
  pen.pendown()
  pen.goto(0, y_max)  # y 轴

  # 使用 0.5 间隔绘制刻度（若 draw_ticks 已定义则调用），并防止之后重复绘制
  if 'draw_ticks' in globals():
    try:
      draw_ticks(step=0.5)
    except Exception:
      pass
    globals()['draw_ticks'] = lambda step=1: None

# 画刻度和数字
def draw_ticks(step=1):
  pen.penup()
  pen.color("black")
  # x 轴刻度
  x = math.ceil(x_min)
  while x <= math.floor(x_max):
    if x != 0:
      pen.goto(x, -0.2*(y_max - y_min)/20)  # 稍下移做刻度
      pen.pendown()
      pen.goto(x, 0.2*(y_max - y_min)/20)
      pen.penup()
      pen.goto(x, -0.6 if y_min < -1 else -0.3)  # 放数字的位置
      pen.write(str(x), align="center", font=("Arial", 8, "normal"))
    x += step

  # y 轴刻度
  y = math.ceil(y_min)
  while y <= math.floor(y_max):
    if y != 0:
      pen.goto(-0.2*(x_max - x_min)/20, y)
      pen.pendown()
      pen.goto(0.2*(x_max - x_min)/20, y)
      pen.penup()
      pen.goto(-0.4 if x_min < -1 else -0.2, y - 0.1)
      pen.write(str(y), align="right", font=("Arial", 8, "normal"))
    y += step

# 画二次函数
def draw_parabola(a, b, c, step=0.05):
  pen.color("red")
  pen.pensize(2)
  first = True
  x = x_min
  while x <= x_max:
    y = a * x * x + b * x + c
    # 如果 y 超出显示范围则跳过连接，避免连线越界
    if y_min - 1 <= y <= y_max + 1:
      if first:
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        first = False
      else:
        pen.goto(x, y)
    else:
      pen.penup()
      first = True
    x += step

# 绘制
pen.clear()
draw_axes()
draw_ticks(step=1)
draw_parabola(a, b, c, step=0.02)

# 在屏幕上标注函数表达式
pen.penup()
pen.color("blue")
pen.goto(x_min + 1, y_max - 1)
pen.write(f"y = {a}x^2 + {b}x + {c}", font=("Arial", 12, "bold"))

turtle.update()
turtle.done()

