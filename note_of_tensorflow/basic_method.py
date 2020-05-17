# v2.0
# %%
import tensorflow as tf
a = tf.constant(2.)
b = tf.constant(4.)
c = a + b
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
e = tf.constant([2,2], dtype=tf.float32)
c = a * b ## 乘法
f = a * e ## 乘法
print(c)
print(f)

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
import tensorflow as tf 

# 构建待优化变量
x = tf.constant(1.)
w1 = tf.constant(2.)
b1 = tf.constant(1.)
w2 = tf.constant(2.)
b2 = tf.constant(1.)

with tf.GradientTape(persistent=True) as tape:
	# 非tf.Variable类型的张量需要人为设置记录梯度信息
	tape.watch([w1, b1, w2, b2])
	# 构建2层网络
	y1 = x * w1 + b1	
	y2 = y1 * w2 + b2

# 独立求解出各个导数
# dy2    dy1    dy2
# --- *  --- =  ---
# dy1    dw1    dw1
dy2_dy1 = tape.gradient(y2, [y1])[0]
dy1_dw1 = tape.gradient(y1, [w1])[0]
dy2_dw1 = tape.gradient(y2, [w1])[0]

# 验证链式法则
print(dy2_dy1 * dy1_dw1)
print(dy2_dw1)

# 卷积
# %%
import  tensorflow as tf
x = tf.random.normal([1,5,5,1]) # 模拟输入，3通道，高宽为5
# 需要根据[k,k,cin,cout]格式创建，4个卷积核
w = tf.random.normal([3,3,1,1])
# 步长为1, padding为1,
out = tf.nn.conv2d(x,w,strides=1,padding = 'VALID')
print(out.shape)

# %%
import  tensorflow as tf
y = 2
y_onehot = tf.one_hot(y, depth=10)
print(y_onehot)

# %%
import  tensorflow as tf
x = tf.constant([[1., 1.], [2., 2.]])
print(tf.reduce_mean(x))
print(tf.reduce_mean(x, 0))
print(tf.reduce_mean(x, 1))

# %%
import  tensorflow as tf
x = tf.constant([0.1, 0.8, 0.1])
x1 = tf.constant([0., 1., 0.])
x2 = tf.constant([1., 0., 0.])
print(tf.reduce_mean(tf.square(x1-x)))
print(tf.reduce_mean(tf.square(x2-x)))

# %%
