class Foo:
    def foo(self):
        print('foo')

   
class Bar(Foo):
    def bar(self):
        print('bar')


bar = Bar()
bar.foo()
bar.bar()
