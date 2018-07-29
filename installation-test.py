#import 
import tensorflow as tf

sess = tf.Session()

hello = tf.constant('Hello from  tensor')

print(sess.run(hello))


a = tf.constant(20)
b = tf.constant(2)
print('a +b ={0}'.format(sess.run(a + b)))