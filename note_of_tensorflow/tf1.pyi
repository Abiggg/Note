
# %%
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
assert tf.__version__.startswith('2.')

a = tf.constant(2.)
b = tf.constant(4.)
c = a + b
print(c)
## run
print("run:", tf.Session().run(c))

# %%
