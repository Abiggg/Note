
#加减乘除
# %%
import tensorflow as tf
a = tf.constant(5, dtype=tf.float32)
b = tf.constant(2, dtype=tf.float32)
c = a + b ## 加法
print(c)

# %%
import tensorflow as tf
a = tf.constant(5, dtype=tf.float32)
b = tf.constant(2, dtype=tf.float32)
c = a - b ## 减法
print(c)

#%%
import tensorflow as tf
a = tf.constant(5, dtype=tf.float32)
b = tf.constant(2, dtype=tf.float32)
c = a / b ## 除法
print(c)

# %%
import tensorflow as tf
a = tf.constant(5, dtype=tf.float32)
b = tf.constant(2, dtype=tf.float32)
c = a // b ## 除法取整
print(c)

# %%
import tensorflow as tf
a = tf.constant(5, dtype=tf.float32)
b = tf.constant(2, dtype=tf.float32)
c = a * b ## 乘法
print(c)

# %%
import tensorflow as tf
a = tf.constant(5, dtype=tf.float32)
b = tf.constant(2, dtype=tf.float32)
c = a ** b ## 乘方
print(c)

## 矩阵运算
# %%
import tensorflow as tf
a = tf.constant([[1,1,1], [1,1,1]], dtype=tf.int32)
b = tf.constant([[2,2], [2,2], [2,2]], dtype=tf.int32)
# 2*3 @ 3 * 2 = 2 * 2
c = tf.matmul(a, b)
d = a @ b
print(c)
print(d)

## 求导
# %%
x = tf.constant(2, dtype=tf.float32)
k = tf.constant(3, dtype=tf.float32)
b = tf.constant(4, dtype=tf.float32)
# y = (k**2) * x + k * x + b
# y = (3**2) * 2 + 3 * 2 + 4 =  28
y = tf.constant(28, dtype=tf.float32)

with tf.GradientTape() as tape:
    tape.watch([k]) ## 变量可以自动watch,常量得手动watch
    y = (k**2) * x + k * x + b

#dy_dk = 2 * k * x + x = 14
[dy_dk] = tape.gradient(y,[k])
print(dy_dk)

# %%
