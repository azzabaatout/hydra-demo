import torchvision
import torchvision.transforms as transforms
import tensorflow_datasets as tfds

# For CIFAR-10
transform_cifar = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.4914, 0.4822, 0.4465), (0.247, 0.243, 0.261))
])

cifar_trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                              download=True, transform=transform_cifar)
cifar_testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                             download=True, transform=transform_cifar)

# For MNIST
transform_mnist = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

mnist_trainset = torchvision.datasets.MNIST(root='./data', train=True,
                                            download=True, transform=transform_mnist)
mnist_testset = torchvision.datasets.MNIST(root='./data', train=False,
                                           download=True, transform=transform_mnist)

# For CIFAR-10
cifar_trainset, cifar_testset = tfds.load('cifar10', split=['train', 'test'], as_supervised=True)

# For MNIST
mnist_trainset, mnist_testset = tfds.load('mnist', split=['train', 'test'], as_supervised=True)
