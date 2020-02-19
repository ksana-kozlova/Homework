'''2. Напишите параметризованный декоратор для классов,
 который будет считать и выводить время работы методов класса, имена которых переданы в параметрах декоратора.
Пример:
  @time_methods('inspect', 'finalize')
  class Spam:
      def __init__(self, s):
          self.s = s
      def inspect(self):
           sleep(self.s)
      def foo(self):
           return self.s

 a = Spam(2)
 a.inspect()  #  должно вывести сообщение о времени работы
 a.foo()  # ничего не выводить'''