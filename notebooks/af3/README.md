# AF3 学习

## 案例学习

### dataclasses

1. frozen: instance 属性不可变，否则 FrozenInstanceError
   1. 但是可以通过类方法修改属性
2. slots
   1. 启用 slots 可以提高内存效率，尤其是当创建大量实例时
   2. 启用 slots 后，实例只能有定义在 **slots** 中的属性，不能动态添加新属性。
3. kw_only
   1. 强制类的构造函数只能通过关键字参数传递参数 -> 强了代码的可读性

```python
import dataclasses
@dataclasses.dataclass(frozen=True, slots=True, kw_only=True)

# 默认工厂函数
from dataclasses import dataclass, field

@dataclass
class Point:
    x: int
    y: int
    history: list = field(default_factory=list)  # 默认空列表

p1 = Point(1, 2)
p1.history.append('moved')
print(p1.history)  # 输出：['moved']

# 替换
dataclasses.replace(p1, x=3)
```

### typing

```python
# 常与 Any Optional 结合
typing.cast(CLS, instance)
```

- Protocol: 类方法

```python
class RowLookup(Protocol):

  def get_row_by_key(
      self,
      key: int,
      column_name_map: Mapping[str, str] | None = None,
  ) -> Mapping[str, Any]:
    ...
```

### time

```python
print(f'Processing chain {chain.id}')
process_chain_start_time = time.time()

...

print(
    f'Processing chain {chain.id} took'
    f' {time.time() - process_chain_start_time:.2f} seconds',
)
```

### absl

```python
from absl import app, flags

# 创建命令行标志
FLAGS = flags.FLAGS
flags.DEFINE_string("name", "World", "Name to greet")

def main(argv):
    # 通过标志获取命令行参数的值
    print(f"Hello, {FLAGS.name}!")

# 在 Jupyter 中运行时，可以不调用 app.run()，只需要调用 main
main([])  # 输出：Hello, World!
```

### frozenset

- 不可变集合，可哈希

```python
frozenset()

# 交集
print(fs1 & fs2)  # 输出: frozenset({3, 4})
# 并集
print(fs1 | fs2)  # 输出: frozenset({1, 2, 3, 4, 5, 6})
# 差集
print(fs1 - fs2)  # 输出: frozenset({1, 2})
# 对称差
print(fs1 ^ fs2)  # 输出: frozenset({1, 2, 5, 6})
```

### NamedTuple

```python
from typing import NamedTuple

class Person(NamedTuple):
    name: str
    age: int
    gender: str

# 实例化 NamedTuple
p1 = Person(name='Bob', age=25, gender='Male')
print(p1)            # 输出: Person(name='Bob', age=25, gender='Male')
print(p1.name)       # 输出: Bob
print(p1.age)        # 输出: 25
```

### 魔法方法

- __post_init__: 是一个特殊的魔法方法，主要用于 dataclasses 模块中的类（Python 3.7+）。当使用 dataclass 装饰器创建数据类时，__post_init__ 允许在 类实例化后 执行一些自定义的初始化逻辑。

- __getstate__: 在对象被序列化（pickle.dump() 或 pickle.dumps()）时，Python 会调用对象的 __getstate__ 方法，获取对象的状态。


### functools

- cached_property: @cached_property 装饰的方法只会在第一次访问时执行计算，并将结果缓存起来。
  - 与 @property 的区别: 每次访问时都会重新计算属性值。
  - cached_property 将缓存存储在对象的 __dict__ 字典中。
  - 每个对象的缓存是独立的，不会影响其他对象。
  - 可以使用 del 删除缓存，让属性重新计算。

```python
del obj.value     # 删除缓存
print(obj.value)  # 输出: Calculating... 42（重新计算）
```

- @functools.lru_cache(maxsize=128) 是 Python 中的一个装饰器，用于缓存函数的返回结果，从而提高程序的性能。
  - 当缓存中的数据量超过指定的 maxsize（最大缓存大小）时，会自动删除最久未使用的数据。
  - maxsize 参数控制缓存的容量，如果设置为 None，表示无限缓存。
  - 缓存效果：fibonacci 被调用多次，但对于相同的参数，返回结果直接从缓存获取，而不会重新计算。
  - 使用 cache_info() 和 cache_clear() 方法查看缓存状态或清空缓存。

```python
import functools

@functools.lru_cache(maxsize=2)
def square(x):
    return x * x

square(2)
square(3)
square(2)

print(square.cache_info())  # 查看缓存状态
square.cache_clear()        # 清空缓存
print(square.cache_info())
```
