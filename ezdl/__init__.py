import numpy
device = numpy

def use(device):
    if device == 'gpu':
        try:
            import cupy
            device = cupy
        except Exception as e:
            print(e)

    elif device == 'cpu':
        device = numpy

    else:
        print('You can specify "gpu" or "cpu" as the argument.')

