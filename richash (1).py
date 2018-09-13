import tensorflow as tf
x1=tf.([1,2,3,4])
x2=tf.([5,6,7,8])

result=tf.multiply(x1,x2)

with tf.session()as sess:
	output=sess.run(result)
