import tensorflow as tf
#
# Check if GPU is available
print("GPU Available:", tf.config.list_physical_devices('GPU'))
# import tensorflow as tf
# tf.config.list_physical_devices('GPU')
# import tensorflow as tf
# tf.test.is_built_with_cuda()