from mono_swirl import swirlFind
from mono_blur import blurFind
from mono_noise import noiseFind

if __name__ == '__main__':
    print("------------------jnd predict start--------------")
    for step_size in [0.01]:

        print("-------swirl predict start---------")
        swirlFind(step_size)
        print("---------blur predict start-------------")
        blurFind(step_size)
        print("--------noise predict  start-------------")
        noiseFind(step_size)

