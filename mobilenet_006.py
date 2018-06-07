import mxnet as mx




def mobilenet_bn(num_class):

    use_global_stats = False

    data = mx.symbol.Variable(name='data')
    conv1 = mx.symbol.Convolution(name='conv1', data=data , num_filter=32, pad=(1, 1), kernel=(3,3), stride=(2,2), no_bias=False)
    conv1_bn = mx.symbol.BatchNorm(name='conv1_bn', data=conv1 , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv1_scale = conv1_bn
    relu1 = mx.symbol.Activation(name='relu1', data=conv1_scale , act_type='relu')

    conv2_1_dw = mx.symbol.Convolution(name='conv2_1_dw', data=relu1 , num_filter=32, pad=(1, 1), kernel=(3,3), stride=(1,1), no_bias=False, num_group=32)
    conv2_1_dw_bn = mx.symbol.BatchNorm(name='conv2_1_dw_bn', data=conv2_1_dw , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv2_1_dw_scale = conv2_1_dw_bn
    relu2_1_dw = mx.symbol.Activation(name='relu2_1_dw', data=conv2_1_dw_scale , act_type='relu')

    conv2_1_sep = mx.symbol.Convolution(name='conv2_1_sep', data=relu2_1_dw , num_filter=64, pad=(0, 0), kernel=(1,1), stride=(1,1), no_bias=False)
    conv2_1_sep_bn = mx.symbol.BatchNorm(name='conv2_1_sep_bn', data=conv2_1_sep , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv2_1_sep_scale = conv2_1_sep_bn
    relu2_1_sep = mx.symbol.Activation(name='relu2_1_sep', data=conv2_1_sep_scale , act_type='relu')

    conv2_2_dw = mx.symbol.Convolution(name='conv2_2_dw', data=relu2_1_sep , num_filter=64, pad=(1, 1), kernel=(3,3), stride=(2,2), no_bias=False, num_group=64)
    conv2_2_dw_bn = mx.symbol.BatchNorm(name='conv2_2_dw_bn', data=conv2_2_dw , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv2_2_dw_scale = conv2_2_dw_bn
    relu2_2_dw = mx.symbol.Activation(name='relu2_2_dw', data=conv2_2_dw_scale , act_type='relu')

    conv2_2_sep = mx.symbol.Convolution(name='conv2_2_sep', data=relu2_2_dw , num_filter=128, pad=(0, 0), kernel=(1,1), stride=(1,1), no_bias=False)
    conv2_2_sep_bn = mx.symbol.BatchNorm(name='conv2_2_sep_bn', data=conv2_2_sep , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv2_2_sep_scale = conv2_2_sep_bn
    relu2_2_sep = mx.symbol.Activation(name='relu2_2_sep', data=conv2_2_sep_scale , act_type='relu')

    conv3_1_dw = mx.symbol.Convolution(name='conv3_1_dw', data=relu2_2_sep , num_filter=128, pad=(1, 1), kernel=(3,3), stride=(1,1), no_bias=False, num_group=128)
    conv3_1_dw_bn = mx.symbol.BatchNorm(name='conv3_1_dw_bn', data=conv3_1_dw , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv3_1_dw_scale = conv3_1_dw_bn
    relu3_1_dw = mx.symbol.Activation(name='relu3_1_dw', data=conv3_1_dw_scale , act_type='relu')

    conv3_1_sep = mx.symbol.Convolution(name='conv3_1_sep', data=relu3_1_dw , num_filter=128, pad=(0, 0), kernel=(1,1), stride=(1,1), no_bias=False)
    conv3_1_sep_bn = mx.symbol.BatchNorm(name='conv3_1_sep_bn', data=conv3_1_sep , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv3_1_sep_scale = conv3_1_sep_bn
    relu3_1_sep = mx.symbol.Activation(name='relu3_1_sep', data=conv3_1_sep_scale , act_type='relu')

    conv3_2_dw = mx.symbol.Convolution(name='conv3_2_dw', data=relu3_1_sep , num_filter=128, pad=(1, 1), kernel=(3,3), stride=(2,2), no_bias=False, num_group=128)
    conv3_2_dw_bn = mx.symbol.BatchNorm(name='conv3_2_dw_bn', data=conv3_2_dw , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv3_2_dw_scale = conv3_2_dw_bn
    relu3_2_dw = mx.symbol.Activation(name='relu3_2_dw', data=conv3_2_dw_scale , act_type='relu')

    conv3_2_sep = mx.symbol.Convolution(name='conv3_2_sep', data=relu3_2_dw , num_filter=256, pad=(0, 0), kernel=(1,1), stride=(1,1), no_bias=False)
    conv3_2_sep_bn = mx.symbol.BatchNorm(name='conv3_2_sep_bn', data=conv3_2_sep , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv3_2_sep_scale = conv3_2_sep_bn
    relu3_2_sep = mx.symbol.Activation(name='relu3_2_sep', data=conv3_2_sep_scale , act_type='relu')

    conv4_1_dw = mx.symbol.Convolution(name='conv4_1_dw', data=relu3_2_sep , num_filter=256, pad=(1, 1), kernel=(3,3), stride=(1,1), no_bias=False, num_group=256)
    conv4_1_dw_bn = mx.symbol.BatchNorm(name='conv4_1_dw_bn', data=conv4_1_dw , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv4_1_dw_scale = conv4_1_dw_bn
    relu4_1_dw = mx.symbol.Activation(name='relu4_1_dw', data=conv4_1_dw_scale , act_type='relu')

    conv4_1_sep = mx.symbol.Convolution(name='conv4_1_sep', data=relu4_1_dw , num_filter=256, pad=(0, 0), kernel=(1,1), stride=(1,1), no_bias=False)
    conv4_1_sep_bn = mx.symbol.BatchNorm(name='conv4_1_sep_bn', data=conv4_1_sep , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv4_1_sep_scale = conv4_1_sep_bn
    relu4_1_sep = mx.symbol.Activation(name='relu4_1_sep', data=conv4_1_sep_scale , act_type='relu')

    # 28x28 -> 14x14
    conv4_2_dw = mx.symbol.Convolution(name='conv4_2_dw', data=relu4_1_sep , num_filter=256, pad=(1, 1), kernel=(3,3), stride=(2,2), no_bias=False, num_group=256)
    conv4_2_dw_bn = mx.symbol.BatchNorm(name='conv4_2_dw_bn', data=conv4_2_dw , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv4_2_dw_scale = conv4_2_dw_bn
    relu4_2_dw = mx.symbol.Activation(name='relu4_2_dw', data=conv4_2_dw_scale , act_type='relu')

    conv4_2_sep = mx.symbol.Convolution(name='conv4_2_sep', data=relu4_2_dw , num_filter=512, pad=(0, 0), kernel=(1,1), stride=(1,1), no_bias=False)
    conv4_2_sep_bn = mx.symbol.BatchNorm(name='conv4_2_sep_bn', data=conv4_2_sep , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv4_2_sep_scale = conv4_2_sep_bn
    relu4_2_sep = mx.symbol.Activation(name='relu4_2_sep', data=conv4_2_sep_scale , act_type='relu')

    conv5_1_dw = mx.symbol.Convolution(name='conv5_1_dw', data=relu4_2_sep , num_filter=512, pad=(1, 1), kernel=(3,3), stride=(1,1), no_bias=False, num_group=512)
    conv5_1_dw_bn = mx.symbol.BatchNorm(name='conv5_1_dw_bn', data=conv5_1_dw , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv5_1_dw_scale = conv5_1_dw_bn
    relu5_1_dw = mx.symbol.Activation(name='relu5_1_dw', data=conv5_1_dw_scale , act_type='relu')

    conv5_1_sep = mx.symbol.Convolution(name='conv5_1_sep', data=relu5_1_dw , num_filter=512, pad=(0, 0), kernel=(1,1), stride=(1,1), no_bias=False)
    conv5_1_sep_bn = mx.symbol.BatchNorm(name='conv5_1_sep_bn', data=conv5_1_sep , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv5_1_sep_scale = conv5_1_sep_bn
    relu5_1_sep = mx.symbol.Activation(name='relu5_1_sep', data=conv5_1_sep_scale , act_type='relu')

    conv5_2_dw = mx.symbol.Convolution(name='conv5_2_dw', data=relu5_1_sep , num_filter=512, pad=(1, 1), kernel=(3,3), stride=(1,1), no_bias=False, num_group=512)
    conv5_2_dw_bn = mx.symbol.BatchNorm(name='conv5_2_dw_bn', data=conv5_2_dw , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv5_2_dw_scale = conv5_2_dw_bn
    relu5_2_dw = mx.symbol.Activation(name='relu5_2_dw', data=conv5_2_dw_scale , act_type='relu')

    conv5_2_sep = mx.symbol.Convolution(name='conv5_2_sep', data=relu5_2_dw , num_filter=512, pad=(0, 0), kernel=(1,1), stride=(1,1), no_bias=False)
    conv5_2_sep_bn = mx.symbol.BatchNorm(name='conv5_2_sep_bn', data=conv5_2_sep , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv5_2_sep_scale = conv5_2_sep_bn
    relu5_2_sep = mx.symbol.Activation(name='relu5_2_sep', data=conv5_2_sep_scale , act_type='relu')

    conv5_3_dw = mx.symbol.Convolution(name='conv5_3_dw', data=relu5_2_sep , num_filter=512, pad=(1, 1), kernel=(3,3), stride=(1,1), no_bias=False, num_group=512)
    conv5_3_dw_bn = mx.symbol.BatchNorm(name='conv5_3_dw_bn', data=conv5_3_dw , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv5_3_dw_scale = conv5_3_dw_bn
    relu5_3_dw = mx.symbol.Activation(name='relu5_3_dw', data=conv5_3_dw_scale , act_type='relu')

    conv5_3_sep = mx.symbol.Convolution(name='conv5_3_sep', data=relu5_3_dw , num_filter=512, pad=(0, 0), kernel=(1,1), stride=(1,1), no_bias=False)
    conv5_3_sep_bn = mx.symbol.BatchNorm(name='conv5_3_sep_bn', data=conv5_3_sep , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv5_3_sep_scale = conv5_3_sep_bn
    relu5_3_sep = mx.symbol.Activation(name='relu5_3_sep', data=conv5_3_sep_scale , act_type='relu')

    conv5_4_dw = mx.symbol.Convolution(name='conv5_4_dw', data=relu5_3_sep , num_filter=512, pad=(1, 1), kernel=(3,3), stride=(1,1), no_bias=False, num_group=512)
    conv5_4_dw_bn = mx.symbol.BatchNorm(name='conv5_4_dw_bn', data=conv5_4_dw , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv5_4_dw_scale = conv5_4_dw_bn
    relu5_4_dw = mx.symbol.Activation(name='relu5_4_dw', data=conv5_4_dw_scale , act_type='relu')

    conv5_4_sep = mx.symbol.Convolution(name='conv5_4_sep', data=relu5_4_dw , num_filter=512, pad=(0, 0), kernel=(1,1), stride=(1,1), no_bias=False)
    conv5_4_sep_bn = mx.symbol.BatchNorm(name='conv5_4_sep_bn', data=conv5_4_sep , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv5_4_sep_scale = conv5_4_sep_bn
    relu5_4_sep = mx.symbol.Activation(name='relu5_4_sep', data=conv5_4_sep_scale , act_type='relu')

    conv5_5_dw = mx.symbol.Convolution(name='conv5_5_dw', data=relu5_4_sep , num_filter=512, pad=(1, 1), kernel=(3,3), stride=(1,1), no_bias=False, num_group=512)
    conv5_5_dw_bn = mx.symbol.BatchNorm(name='conv5_5_dw_bn', data=conv5_5_dw , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv5_5_dw_scale = conv5_5_dw_bn
    relu5_5_dw = mx.symbol.Activation(name='relu5_5_dw', data=conv5_5_dw_scale , act_type='relu')

    conv5_5_sep = mx.symbol.Convolution(name='conv5_5_sep', data=relu5_5_dw , num_filter=512, pad=(0, 0), kernel=(1,1), stride=(1,1), no_bias=False)
    conv5_5_sep_bn = mx.symbol.BatchNorm(name='conv5_5_sep_bn', data=conv5_5_sep , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv5_5_sep_scale = conv5_5_sep_bn
    relu5_5_sep = mx.symbol.Activation(name='relu5_5_sep', data=conv5_5_sep_scale , act_type='relu')

    conv5_6_dw = mx.symbol.Convolution(name='conv5_6_dw', data=relu5_5_sep , num_filter=512, pad=(1, 1), kernel=(3,3), stride=(2,2), no_bias=False, num_group=512)
    conv5_6_dw_bn = mx.symbol.BatchNorm(name='conv5_6_dw_bn', data=conv5_6_dw , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv5_6_dw_scale = conv5_6_dw_bn
    relu5_6_dw = mx.symbol.Activation(name='relu5_6_dw', data=conv5_6_dw_scale , act_type='relu')

    conv5_6_sep = mx.symbol.Convolution(name='conv5_6_sep', data=relu5_6_dw , num_filter=1024, pad=(0, 0), kernel=(1,1), stride=(1,1), no_bias=False)
    conv5_6_sep_bn = mx.symbol.BatchNorm(name='conv5_6_sep_bn', data=conv5_6_sep , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv5_6_sep_scale = conv5_6_sep_bn
    relu5_6_sep = mx.symbol.Activation(name='relu5_6_sep', data=conv5_6_sep_scale , act_type='relu')

    conv6_dw = mx.symbol.Convolution(name='conv6_dw', data=relu5_6_sep , num_filter=1024, pad=(1, 1), kernel=(3,3), stride=(1,1), no_bias=False, num_group=1024)
    conv6_dw_bn = mx.symbol.BatchNorm(name='conv6_dw_bn', data=conv6_dw , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv6_dw_scale = conv6_dw_bn
    relu6_dw = mx.symbol.Activation(name='relu6_dw', data=conv6_dw_scale , act_type='relu')

    conv6_sep = mx.symbol.Convolution(name='conv6_sep', data=relu6_dw , num_filter=1024, pad=(0, 0), kernel=(1,1), stride=(1,1), no_bias=False)
    conv6_sep_bn = mx.symbol.BatchNorm(name='conv6_sep_bn', data=conv6_sep , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv6_sep_scale = conv6_sep_bn
    relu6_sep = mx.symbol.Activation(name='relu6_sep', data=conv6_sep_scale , act_type='relu')

    pool6 = mx.symbol.Pooling(name='pool6', data=relu6_sep , pooling_convention='full', global_pool=True, kernel=(1,1), pool_type='avg')
    fc7 = mx.symbol.Convolution(name='fc7', data=pool6 , num_filter=1024, pad=(0, 0), kernel=(1,1), stride=(1,1), no_bias=False)
    flatten = mx.symbol.Flatten(data=fc7, name='flatten')
    #softmax = mx.symbol.SoftmaxOutput(data=flatten, name='softmax')
    fc1 = mx.symbol.FullyConnected(data=flatten, num_hidden=num_class, name='fc1')
    return fc1


def mobilenet_nobn(num_class):

    use_global_stats = False

    data = mx.symbol.Variable(name='data')
    conv1 = mx.symbol.Convolution(name='conv1', data=data , num_filter=32, pad=(1, 1), kernel=(3,3), stride=(2,2), no_bias=False)
    # conv1_bn = mx.symbol.BatchNorm(name='conv1_bn', data=conv1 , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv1_scale = conv1
    relu1 = mx.symbol.Activation(name='relu1', data=conv1_scale , act_type='relu')

    conv2_1_dw = mx.symbol.Convolution(name='conv2_1_dw', data=relu1 , num_filter=32, pad=(1, 1), kernel=(3,3), stride=(1,1), no_bias=False, num_group=32)
    # conv2_1_dw_bn = mx.symbol.BatchNorm(name='conv2_1_dw_bn', data=conv2_1_dw , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv2_1_dw_scale = conv2_1_dw
    relu2_1_dw = mx.symbol.Activation(name='relu2_1_dw', data=conv2_1_dw_scale , act_type='relu')

    conv2_1_sep = mx.symbol.Convolution(name='conv2_1_sep', data=relu2_1_dw , num_filter=64, pad=(0, 0), kernel=(1,1), stride=(1,1), no_bias=False)
    # conv2_1_sep_bn = mx.symbol.BatchNorm(name='conv2_1_sep_bn', data=conv2_1_sep , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv2_1_sep_scale = conv2_1_sep
    relu2_1_sep = mx.symbol.Activation(name='relu2_1_sep', data=conv2_1_sep_scale , act_type='relu')

    conv2_2_dw = mx.symbol.Convolution(name='conv2_2_dw', data=relu2_1_sep , num_filter=64, pad=(1, 1), kernel=(3,3), stride=(2,2), no_bias=False, num_group=64)
    # conv2_2_dw_bn = mx.symbol.BatchNorm(name='conv2_2_dw_bn', data=conv2_2_dw , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv2_2_dw_scale = conv2_2_dw
    relu2_2_dw = mx.symbol.Activation(name='relu2_2_dw', data=conv2_2_dw_scale , act_type='relu')

    conv2_2_sep = mx.symbol.Convolution(name='conv2_2_sep', data=relu2_2_dw , num_filter=128, pad=(0, 0), kernel=(1,1), stride=(1,1), no_bias=False)
    # conv2_2_sep_bn = mx.symbol.BatchNorm(name='conv2_2_sep_bn', data=conv2_2_sep , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv2_2_sep_scale = conv2_2_sep
    relu2_2_sep = mx.symbol.Activation(name='relu2_2_sep', data=conv2_2_sep_scale , act_type='relu')

    conv3_1_dw = mx.symbol.Convolution(name='conv3_1_dw', data=relu2_2_sep , num_filter=128, pad=(1, 1), kernel=(3,3), stride=(1,1), no_bias=False, num_group=128)
    # conv3_1_dw_bn = mx.symbol.BatchNorm(name='conv3_1_dw_bn', data=conv3_1_dw , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv3_1_dw_scale = conv3_1_dw
    relu3_1_dw = mx.symbol.Activation(name='relu3_1_dw', data=conv3_1_dw_scale , act_type='relu')

    conv3_1_sep = mx.symbol.Convolution(name='conv3_1_sep', data=relu3_1_dw , num_filter=128, pad=(0, 0), kernel=(1,1), stride=(1,1), no_bias=False)
    # conv3_1_sep_bn = mx.symbol.BatchNorm(name='conv3_1_sep_bn', data=conv3_1_sep , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv3_1_sep_scale = conv3_1_sep
    relu3_1_sep = mx.symbol.Activation(name='relu3_1_sep', data=conv3_1_sep_scale , act_type='relu')

    conv3_2_dw = mx.symbol.Convolution(name='conv3_2_dw', data=relu3_1_sep , num_filter=128, pad=(1, 1), kernel=(3,3), stride=(2,2), no_bias=False, num_group=128)
    # conv3_2_dw_bn = mx.symbol.BatchNorm(name='conv3_2_dw_bn', data=conv3_2_dw , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv3_2_dw_scale = conv3_2_dw
    relu3_2_dw = mx.symbol.Activation(name='relu3_2_dw', data=conv3_2_dw_scale , act_type='relu')

    conv3_2_sep = mx.symbol.Convolution(name='conv3_2_sep', data=relu3_2_dw , num_filter=256, pad=(0, 0), kernel=(1,1), stride=(1,1), no_bias=False)
    # conv3_2_sep_bn = mx.symbol.BatchNorm(name='conv3_2_sep_bn', data=conv3_2_sep , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv3_2_sep_scale = conv3_2_sep
    relu3_2_sep = mx.symbol.Activation(name='relu3_2_sep', data=conv3_2_sep_scale , act_type='relu')

    conv4_1_dw = mx.symbol.Convolution(name='conv4_1_dw', data=relu3_2_sep , num_filter=256, pad=(1, 1), kernel=(3,3), stride=(1,1), no_bias=False, num_group=256)
    # conv4_1_dw_bn = mx.symbol.BatchNorm(name='conv4_1_dw_bn', data=conv4_1_dw , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv4_1_dw_scale = conv4_1_dw
    relu4_1_dw = mx.symbol.Activation(name='relu4_1_dw', data=conv4_1_dw_scale , act_type='relu')

    conv4_1_sep = mx.symbol.Convolution(name='conv4_1_sep', data=relu4_1_dw , num_filter=256, pad=(0, 0), kernel=(1,1), stride=(1,1), no_bias=False)
    # conv4_1_sep_bn = mx.symbol.BatchNorm(name='conv4_1_sep_bn', data=conv4_1_sep , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv4_1_sep_scale = conv4_1_sep
    relu4_1_sep = mx.symbol.Activation(name='relu4_1_sep', data=conv4_1_sep_scale , act_type='relu')

    # 28x28 -> 14x14
    conv4_2_dw = mx.symbol.Convolution(name='conv4_2_dw', data=relu4_1_sep , num_filter=256, pad=(1, 1), kernel=(3,3), stride=(2,2), no_bias=False, num_group=256)
    # conv4_2_dw_bn = mx.symbol.BatchNorm(name='conv4_2_dw_bn', data=conv4_2_dw , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv4_2_dw_scale = conv4_2_dw
    relu4_2_dw = mx.symbol.Activation(name='relu4_2_dw', data=conv4_2_dw_scale , act_type='relu')

    conv4_2_sep = mx.symbol.Convolution(name='conv4_2_sep', data=relu4_2_dw , num_filter=512, pad=(0, 0), kernel=(1,1), stride=(1,1), no_bias=False)
    # conv4_2_sep_bn = mx.symbol.BatchNorm(name='conv4_2_sep_bn', data=conv4_2_sep , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv4_2_sep_scale = conv4_2_sep
    relu4_2_sep = mx.symbol.Activation(name='relu4_2_sep', data=conv4_2_sep_scale , act_type='relu')

    conv5_1_dw = mx.symbol.Convolution(name='conv5_1_dw', data=relu4_2_sep , num_filter=512, pad=(1, 1), kernel=(3,3), stride=(1,1), no_bias=False, num_group=512)
    # conv5_1_dw_bn = mx.symbol.BatchNorm(name='conv5_1_dw_bn', data=conv5_1_dw , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv5_1_dw_scale = conv5_1_dw
    relu5_1_dw = mx.symbol.Activation(name='relu5_1_dw', data=conv5_1_dw_scale , act_type='relu')

    conv5_1_sep = mx.symbol.Convolution(name='conv5_1_sep', data=relu5_1_dw , num_filter=512, pad=(0, 0), kernel=(1,1), stride=(1,1), no_bias=False)
    # conv5_1_sep_bn = mx.symbol.BatchNorm(name='conv5_1_sep_bn', data=conv5_1_sep , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv5_1_sep_scale = conv5_1_sep
    relu5_1_sep = mx.symbol.Activation(name='relu5_1_sep', data=conv5_1_sep_scale , act_type='relu')

    conv5_2_dw = mx.symbol.Convolution(name='conv5_2_dw', data=relu5_1_sep , num_filter=512, pad=(1, 1), kernel=(3,3), stride=(1,1), no_bias=False, num_group=512)
    # conv5_2_dw_bn = mx.symbol.BatchNorm(name='conv5_2_dw_bn', data=conv5_2_dw , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv5_2_dw_scale = conv5_2_dw
    relu5_2_dw = mx.symbol.Activation(name='relu5_2_dw', data=conv5_2_dw_scale , act_type='relu')

    conv5_2_sep = mx.symbol.Convolution(name='conv5_2_sep', data=relu5_2_dw , num_filter=512, pad=(0, 0), kernel=(1,1), stride=(1,1), no_bias=False)
    # conv5_2_sep_bn = mx.symbol.BatchNorm(name='conv5_2_sep_bn', data=conv5_2_sep , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv5_2_sep_scale = conv5_2_sep
    relu5_2_sep = mx.symbol.Activation(name='relu5_2_sep', data=conv5_2_sep_scale , act_type='relu')

    conv5_3_dw = mx.symbol.Convolution(name='conv5_3_dw', data=relu5_2_sep , num_filter=512, pad=(1, 1), kernel=(3,3), stride=(1,1), no_bias=False, num_group=512)
    # conv5_3_dw_bn = mx.symbol.BatchNorm(name='conv5_3_dw_bn', data=conv5_3_dw , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv5_3_dw_scale = conv5_3_dw
    relu5_3_dw = mx.symbol.Activation(name='relu5_3_dw', data=conv5_3_dw_scale , act_type='relu')

    conv5_3_sep = mx.symbol.Convolution(name='conv5_3_sep', data=relu5_3_dw , num_filter=512, pad=(0, 0), kernel=(1,1), stride=(1,1), no_bias=False)
    # conv5_3_sep_bn = mx.symbol.BatchNorm(name='conv5_3_sep_bn', data=conv5_3_sep , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv5_3_sep_scale = conv5_3_sep
    relu5_3_sep = mx.symbol.Activation(name='relu5_3_sep', data=conv5_3_sep_scale , act_type='relu')

    conv5_4_dw = mx.symbol.Convolution(name='conv5_4_dw', data=relu5_3_sep , num_filter=512, pad=(1, 1), kernel=(3,3), stride=(1,1), no_bias=False, num_group=512)
    # conv5_4_dw_bn = mx.symbol.BatchNorm(name='conv5_4_dw_bn', data=conv5_4_dw , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv5_4_dw_scale = conv5_4_dw
    relu5_4_dw = mx.symbol.Activation(name='relu5_4_dw', data=conv5_4_dw_scale , act_type='relu')

    conv5_4_sep = mx.symbol.Convolution(name='conv5_4_sep', data=relu5_4_dw , num_filter=512, pad=(0, 0), kernel=(1,1), stride=(1,1), no_bias=False)
    # conv5_4_sep_bn = mx.symbol.BatchNorm(name='conv5_4_sep_bn', data=conv5_4_sep , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv5_4_sep_scale = conv5_4_sep
    relu5_4_sep = mx.symbol.Activation(name='relu5_4_sep', data=conv5_4_sep_scale , act_type='relu')

    conv5_5_dw = mx.symbol.Convolution(name='conv5_5_dw', data=relu5_4_sep , num_filter=512, pad=(1, 1), kernel=(3,3), stride=(1,1), no_bias=False, num_group=512)
    # conv5_5_dw_bn = mx.symbol.BatchNorm(name='conv5_5_dw_bn', data=conv5_5_dw , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv5_5_dw_scale = conv5_5_dw
    relu5_5_dw = mx.symbol.Activation(name='relu5_5_dw', data=conv5_5_dw_scale , act_type='relu')

    conv5_5_sep = mx.symbol.Convolution(name='conv5_5_sep', data=relu5_5_dw , num_filter=512, pad=(0, 0), kernel=(1,1), stride=(1,1), no_bias=False)
    # conv5_5_sep_bn = mx.symbol.BatchNorm(name='conv5_5_sep_bn', data=conv5_5_sep , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv5_5_sep_scale = conv5_5_sep
    relu5_5_sep = mx.symbol.Activation(name='relu5_5_sep', data=conv5_5_sep_scale , act_type='relu')

    conv5_6_dw = mx.symbol.Convolution(name='conv5_6_dw', data=relu5_5_sep , num_filter=512, pad=(1, 1), kernel=(3,3), stride=(2,2), no_bias=False, num_group=512)
    # conv5_6_dw_bn = mx.symbol.BatchNorm(name='conv5_6_dw_bn', data=conv5_6_dw , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv5_6_dw_scale = conv5_6_dw
    relu5_6_dw = mx.symbol.Activation(name='relu5_6_dw', data=conv5_6_dw_scale , act_type='relu')

    conv5_6_sep = mx.symbol.Convolution(name='conv5_6_sep', data=relu5_6_dw , num_filter=1024, pad=(0, 0), kernel=(1,1), stride=(1,1), no_bias=False)
    # conv5_6_sep_bn = mx.symbol.BatchNorm(name='conv5_6_sep_bn', data=conv5_6_sep , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv5_6_sep_scale = conv5_6_sep
    relu5_6_sep = mx.symbol.Activation(name='relu5_6_sep', data=conv5_6_sep_scale , act_type='relu')

    conv6_dw = mx.symbol.Convolution(name='conv6_dw', data=relu5_6_sep , num_filter=1024, pad=(1, 1), kernel=(3,3), stride=(1,1), no_bias=False, num_group=1024)
    # conv6_dw_bn = mx.symbol.BatchNorm(name='conv6_dw_bn', data=conv6_dw , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv6_dw_scale = conv6_dw
    relu6_dw = mx.symbol.Activation(name='relu6_dw', data=conv6_dw_scale , act_type='relu')

    conv6_sep = mx.symbol.Convolution(name='conv6_sep', data=relu6_dw , num_filter=1024, pad=(0, 0), kernel=(1,1), stride=(1,1), no_bias=False)
    # conv6_sep_bn = mx.symbol.BatchNorm(name='conv6_sep_bn', data=conv6_sep , use_global_stats=use_global_stats, fix_gamma=False, eps=0.000100,momentum=0.9)
    conv6_sep_scale = conv6_sep
    relu6_sep = mx.symbol.Activation(name='relu6_sep', data=conv6_sep_scale , act_type='relu')

    pool6 = mx.symbol.Pooling(name='pool6', data=relu6_sep , pooling_convention='full', global_pool=True, kernel=(1,1), pool_type='avg')
    fc7 = mx.symbol.Convolution(name='fc7', data=pool6 , num_filter=1024, pad=(0, 0), kernel=(1,1), stride=(1,1), no_bias=False)
    flatten = mx.symbol.Flatten(data=fc7, name='flatten')
    #softmax = mx.symbol.SoftmaxOutput(data=flatten, name='softmax')
    fc1 = mx.symbol.FullyConnected(data=flatten, num_hidden=num_class, name='fc1')
    return fc1