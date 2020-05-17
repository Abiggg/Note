import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import sys
sys.path.append("..")

from comm import load_data
from tensorflow import keras
from tensorflow.keras import layers, optimizers, datasets


(x,y), (x_val, y_val) = load_data()
x = tf.convert_to_tensor(x, dtype = tf.float32) / 255
y = tf.convert_to_tensor(y, dtype = tf.int32)
y = tf.one_hot(y,depth=10)
print(x.shape,y.shape)
train_dateset = tf.data.Dataset.from_tensor_slices((x,y))
train_dateset = train_dateset.batch(200)

model = keras.Sequential([
    layers.Dense(512, activation = 'relu'),
    layers.Dense(256, activation = 'relu'),
    layers.Dense(128, activation = 'relu'),
    layers.Dense(10)
])

opt = optimizers.SGD(learning_rate=0.001)

def train_epoch(epo):
    for step, (x,y) in enumerate(train_dateset):
        with tf.GradientTape() as tape:
            x = tf.reshape(x, (-1, 28*28))
            out = model(x)
            out_check = tf.argmax(out, 1)
            y_check = tf.argmax(y, 1)
            correct = tf.reduce_sum(tf.cast(tf.equal(out_check, y_check), dtype=tf.int32)).numpy()
            correct = correct / y_check.shape[0]
            loss = tf.reduce_sum(tf.square(out-y))/out.shape[0]
        grads = tape.gradient(loss, model.trainable_variables)
        opt.apply_gradients(zip(grads, model.trainable_variables))

        if step % 100 == 0:
            print(epo, step, 'loss:',loss.numpy(), "correct:", correct)

def train():
    for epoch in range(30):
        train_epoch(epoch)

if __name__ == '__main__':
    train()