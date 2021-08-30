import tensorflow as tf
from tensorflow.keras import layers

# 查看版本

print(tf.__version__)
print(tf.keras.__version__)

# 2.构建简单模型

model = tf.keras.Sequential()

model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))