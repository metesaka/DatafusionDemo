# DatafusionDemo


# Reproduction Steps for the error:

0. (Note: The binary in the repo is for MacOS Arm64. If incompatible you can download [from here](https://github.com/seaweedfs/seaweedfs/releases))
1. Start the weed server : ```./weed server -filer=true -s3 -volume.max=20```
2. You should be able to access your [filer](http://localhost:8888/) and [s3](http://localhost:8333)
3. Populate your file store: 

    ``` python3 sendTPCH.py ```

    ``` python3 sendTPCH_s3.py ```
4. Check if files are loaded correctly: ``` python3 test.py ```