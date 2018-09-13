import tensorflow as tf
#video code 

#build a graph
'''node1=tf.constant(3.0,tf.float32)
node2=tf.constant(4.0
#print(node1,node2)   #abstract tensor....only operations are created...no actual operations or running
#launch the graph in session
sess=tf.Session()'''



'''a=tf.constant(5.0)
b=tf.constant(6.0)
c=a*b
sess=tf.Session()
File_writer=tf.summary.FileWriter('C://Users//Richa Sharma//Desktop//pythonall//tensorfloww//graph',sess.graph)
print(sess.run(c))'''

#first  method
'''print(sess.run([node1,node2]))   #evaluate the tensor
sess.close()

#second method......error show
with tf.Session as sess:
	output=sess.run([node1,node2])
	print(output)'''


'''a=tf.placeholder(tf.float32)     # the value is provided later in case of placeholder
b=tf.placeholder(tf.float32)
adder_node=a+b
sess=tf.Session()
print(sess.run(adder_node,{a:[1,3],b:[2,4]}))'''


#model parameters
W=tf.Variable([.3],tf.float32)
b=tf.Variable([-.3],tf.float32)

#Inputs and Outputs
x=tf.placeholder(tf.float32)
linear_model=W * x + b
y=tf.placeholder(tf.float32)

#loss function
squared_delta=tf.square(linear_model-y)
loss=tf.reduce_sum(squared_delta)


#optimize
optimizer=tf.train.GradientDescentOptimizer(0.01)  #0.01 is the learning rate(steps in which u change your variable)
train=optimizer.minimize(loss)

init=tf.global_variables_initializer()
sess=tf.Session()
sess.run(init)

for i in range(1000):
	sess.run(train,{x:[1,2,3,4],y:[0,-1,-2,-3]})

print(sess.run([W,b]))
#print(sess.run(loss,{x:[1,2,3,4],y:[0,-1,-2,-3]}))





