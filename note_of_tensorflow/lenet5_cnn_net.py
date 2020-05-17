
import tensorflow as tf
from tensorflow.keras import Sequential, layers
from tensorflow.keras import losses, optimizers

network = Sequential([ # 网络容器
    layers.Conv2D(6,kernel_size=3,strides=1), # 第一个卷积层, 6 个 3x3 卷积核
    layers.MaxPooling2D(pool_size=2,strides=2), # 高宽各减半的池化层
    layers.ReLU(), # 激活函数
    layers.Conv2D(16,kernel_size=3,strides=1), # 第二个卷积层, 16 个 3x3 卷积核
    layers.MaxPooling2D(pool_size=2,strides=2), # 高宽各减半的池化层
    layers.ReLU(), # 激活函数
    layers.Flatten(), # 打平层,方便全连接层处理
    layers.Dense(120, activation='relu'), # 全连接层,120 个节点
    layers.Dense(84, activation='relu'), # 全连接层,84 节点
    layers.Dense(10) # 全连接层,10 个节点
])
# build 一次网络模型,给输入 X 的形状,其中 4 为随意给的 batchsz10.4 LeNet-5 实战
network.build(input_shape=(4, 28, 28, 1))
# 统计网络信息
network.summary()

# 创建损失函数的类,在实际计算时直接调用类实例即可
criteon = losses.CategoricalCrossentropy(from_logits=True)
# 构建梯度记录环境
with tf.GradientTape() as tape:
    # 插入通道维度,=>[b,28,28,1]
    x = tf.expand_dims(x,axis=3)
    # 前向计算,获得 10 类别的概率分布,[b, 784] => [b, 10]
    out = network(x)
    # 真实标签 one-hot 编码,[b] => [b, 10]
    y_onehot = tf.one_hot(y, depth=10)
    # 计算交叉熵损失函数,标量
    loss = criteon(y_onehot, out)

# 自动计算梯度
grads = tape.gradient(loss, network.trainable_variables)
# 自动更新参数
optimizer.apply_gradients(zip(grads, network.trainable_variables))

# 记录预测正确的数量,总样本数量
correct, total = 0,0
for x,y in db_test: # 遍历所有训练集样本
    # 插入通道维度,=>[b,28,28,1]
    x = tf.expand_dims(x,axis=3)
    # 前向计算,获得 10 类别的预测分布,[b, 784] => [b, 10]
    out = network(x)
    # 真实的流程时先经过 softmax,再 argmax
    pred = tf.argmax(out, axis=-1)
    # 统计预测正确数量
    y = tf.cast(y, tf.int64)
    # 但是由于 softmax 不改变元素的大小相对关系,故省去
    correct += float(tf.reduce_sum(tf.cast(tf.equal(pred, y),tf.float32)))
    # 统计预测样本总数
    total += x.shape[0]
    # 计算准确率
    print('test acc:', correct/total)